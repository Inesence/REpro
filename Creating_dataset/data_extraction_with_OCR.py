# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 15:27:36 2023

@author: Inese
"""

import pytesseract
import cv2
import re
import json
import os


# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image_path):
    """
    Extracts text from image and returns it.
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray)
    return extracted_text


def find_amounts(text):
    """
    Finds amounts in the text and returns them.
    """
    amounts = re.findall(r'\d+\.\d{2}\b', text)
    floats = [float(amount) for amount in amounts]
    unique = list(dict.fromkeys(floats))
    
    return unique


def find_date(text):
    """
    Finds date in the text and returns it.
    """
    date_pattern = (
    r"\b\d{1,2}/\d{1,2}/\d{4}\b|"  # dd/mm/yyyy
    r"\b\d{1,2}/\d{1,2}/\d{2}\b|"  # dd/mm/yy
    r"\d{1,2}-\d{1,2}-\d{4}|"  # dd-mm-yyyy
    r"\d{4}-\d{1,2}-\d{1,2}" # yyyy-mm-dd
    r"\d{1,2}\.\s*\d{1,2}\.\s*\d{4}|"  # dd.mm.yyyy (with possible space after the second dot)
    r"\d{1,2}\.\s*\d{1,2}\.\s*\d{2}"  # dd.mm.yy (with possible space after the second dot)
    )
    date = re.findall(date_pattern, text)
    return date


def find_pvn_number(text):
    """
    Finds PVN number in the text and returns it.
    """
    patternpvn = r"\d{11}\b"
    matchespvn = re.findall(patternpvn, text)
    pvnnr = matchespvn[0] if matchespvn and len(matchespvn) > 0 else None
    return pvnnr

def find_time(text):
     """
    Finds time in the text and returns it.
    """
     time_pattern = r"\s(\d{2}\:\d{2})"
     time = re.findall(time_pattern, text)
     return time


def extract_info_from_image(image_path, count):
    """
    Extracts information from the image and saves it to a JSON file.
    """
    
    extracted_text = extract_text_from_image(image_path)
    
    amounts = find_amounts(extracted_text)
    summa = max(amounts) if amounts and len(amounts) > 0 else None
    date = find_date(extracted_text)
    pvnnr = find_pvn_number(extracted_text)
    time = find_time(extracted_text)

    data = {
        "PVN_maksataja_numurs": f"{pvnnr}",
        "datums": f"{date}",
        "laiks": f"{time}",
        "summa": f"{summa}",
        "receipt_nr": ""
    }
    
    # Write the information to a JSON file
    json_filename = "{:03d}.json".format(count)
    with open(f"data/key/{json_filename}", "w") as f:
        json.dump(data, f)
        

def process_images_in_folder(folder_path):
    count = 0
        # create the "data" folder if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # create the "key" and "img" subfolders inside the "data" folder
    if not os.path.exists("data/key"):
        os.makedirs("data/key")
    
    if not os.path.exists("data/img"):
        os.makedirs("data/img")
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            image_path = os.path.join(folder_path, filename)
            extract_info_from_image(image_path, count)
            img = cv2.imread(image_path)
            cv2.imwrite(f"data/img/{count:03d}.jpg", img)
            count += 1
        

folder_path = r''
process_images_in_folder(folder_path)