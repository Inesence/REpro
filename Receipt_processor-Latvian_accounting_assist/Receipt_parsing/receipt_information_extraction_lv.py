# -*- coding: utf-8 -*-
"""Receipt_information_extraction_LV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J9bXv9BJkX6JeSNKE0amLEvkBtMTahoi

# Receipt Information Extraction for Latvian Accounting with Donut

## Preparation

First we clone the Donut repository from GitHub onto your local machine or virtual environment. This step is necessary to access the Donut code and files for the next steps. We install the required Python dependencies for Donut using pip. This command installs the Donut package and its dependencies.
"""

!git clone https://github.com/clovaai/donut.git
!cd donut && pip install .

"""## Uploading your images

When taking photos of your receipts, it's important to follow certain guidelines to ensure the best possible results. Although Donut is a powerful tool that can extract information from low-quality photos, following these guidelines will improve the accuracy and quality of the results:

1. Have  a background taht contrasts with the receipt (f.ex. black background for white paper receipt)

2. Capture the entire receipt: Make sure that the entire receipt is visible in the photo, including any edges or corners that may contain important information.

3. Ensure good lighting: Take photos in a well-lit area or use additional lighting if necessary. Avoid taking photos in dimly lit or shadowy areas.

4. Minimize reflections and glare: Position the camera perpendicular to the receipt and avoid capturing any reflections or glare on the receipt.

5. Ensure sharpness and clarity: Take clear and focused photos to ensure all text and details are legible.

6. Use high resolution: Take photos at a high resolution to capture all necessary details.

Now create a folder and place all your receipt images inside it. Then, zip the folder containing the images and upload it to your desired location.

Once the folder is uploaded, you will need to extract its contents.
"""

!unzip /content/img.zip -d /content/img

"""## Information extraction 

Next we load Donut model finetuned by Inesence on 220 Latvian receipts, which reads in the images from a folder named "img", and generates a text sequence for each image. The resulting text is processed and saved as JSON files in a new folder called "keys". 
"""

import torch
import re
import json
from PIL import Image
import os
from transformers import DonutProcessor, VisionEncoderDecoderModel


# Load our model from Hugging Face
processor = DonutProcessor.from_pretrained("inesence/donut-base-finetuned-Latvian-receipts")
model = VisionEncoderDecoderModel.from_pretrained("inesence/donut-base-finetuned-Latvian-receipts")

# Create keys folder
os.mkdir("/content/keys")

# Define image folder
folder = "/content/img/"

nr=0

# xtract information and save it to JSON files
for files in os.listdir(folder):
          image = Image.open(files).convert("RGB")
          pixel_values = processor(image, return_tensors="pt").pixel_values
          
          task_prompt = "<s>"
          decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt")["input_ids"]

          device = "cuda" if torch.cuda.is_available() else "cpu"
          model.to(device)

          outputs = model.generate(pixel_values.to(device),
                                        decoder_input_ids=decoder_input_ids.to(device),
                                        max_length=model.decoder.config.max_position_embeddings,
                                        early_stopping=True,
                                        pad_token_id=processor.tokenizer.pad_token_id,
                                        eos_token_id=processor.tokenizer.eos_token_id,
                                        use_cache=True,
                                        num_beams=1,
                                        bad_words_ids=[[processor.tokenizer.unk_token_id]],
                                        return_dict_in_generate=True,
                                        output_scores=True,)


          sequence = processor.batch_decode(outputs.sequences)[0]
          sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
          sequence = re.sub(r"<.*?>", "", sequence, count=1).strip()  # remove first task start token
          #print(sequence)
          output=processor.token2json(sequence)
          print(output)

          # Save the 'new_dict' dictionary to a JSON file
          with open(f'/content/keys/{nr:03d}.json', 'w') as f:
              json.dump(output, f, ensure_ascii=False) 
          nr+=1

"""## Download extracted information

Now we zip up the extracted information from the receipts and download it to our device.
"""

!zip -r /content/keys.zip /content/keys

from google.colab import files
files.download('/content/keys.zip')