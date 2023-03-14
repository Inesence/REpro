# Repository Description: Receipt Parsing and Processing with Donut Model

This repository contains a project aimed at organisations and companies that do not have extensive computing power or IT knowledge to parse and process receipts for expense reporting. The project involves finetuning the Donut model on a custom to extract relevant information from receipts, and then importing this information into an automated report.

## Project Overview
The project is organized into two folders:

1. **Creating_dataset**: In this folder, you will learn how to create a dataset from the receipts you want to process. If there is no existing application or model that suits your needs, this folder will guide you through the process of creating a dataset to finetune the Donut model for your specific requirements. By extracting information for reporting, you will save time and effort in the future.

2. **Finetuning_Donut_model**: In this folder, we will use a [guide](https://www.philschmid.de/fine-tuning-donut) written by Phillip Schmitt to finetune the Donut model. The guide will be executed in Google Colab because it can use GPU RAM, which is particularly useful if your computing resources are limited. This will make the process faster and more efficient while also protecting your laptop from crashing.

3. **Receipt_processor-Latvian_accounting_assist** : This folder contains a receipt processing pipeline for accounting in Latvia. It uses the finetuned Donut model to extract information from receipts, process the extracted data, and automate report building in Excel. The model will be continuously finetuned and improved as more receipts are collected.



## Summary

This project provides a step-by-step guide for creating a dataset, finetuning the Donut model, and automating the process of report building. By using this project, organizations and companies with limited computing power or IT knowledge can easily extract the necessary information from receipts and simplify their expense reporting.