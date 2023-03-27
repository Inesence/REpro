# Receipt Processing Automation for Accounting
Receipt Processing Automation for Accounting is a powerful tool designed to streamline accounting processes through automation and machine learning. By leveraging cutting-edge AI technology, REpro can accurately extract key data points from receipts, organize expenses, and generate accounting reports that make receipt processing a breeze.

## Purpose and Benefits
The purpose of this project is to automate the time-consuming and error-prone task of receipt processing for self-employed individuals and small companies. With REpro, users can easily extract important data from receipts and generate accurate accounting reports, saving time and reducing errors. The benefits of using REpro include increased efficiency, improved accuracy, and better financial record keeping.

## Features
REpro offers several key features that make receipt processing easy and efficient:

 - Automated receipt parsing: REpro can automatically extract key information from receipts, including dates, vendor names, registration number, total, and receipt number. This eliminates the need for manual data entry, saving you time and reducing errors.
 - Data processing: REpro uses algorithms to sort and concatenate information ready to be entered in monthly and yearly accounting reports.
 - Report auto-fill: REpro then automatically fills your spreadsheet report that is to be submitted to clients and the government.

** This specific code is designed for Latvian expense reporting for self-employed individuals and small companies. The output of REpro is an organized and easy-to-read Excel file filled with your expenses, grouped by month in separate sheets. The template we used is based on a free resource we found online several years ago, but unfortunately, we are unable to locate the original source at this time.** 
If you don't need this specific functionality, you can use the pipeline as a template and create your own pipeline for your application. If you need any additional information to be extracted from receipts, you can head over to [Inesence/REpro/Finetuning_Donut_model](https://github.com/Inesence/REpro/tree/main/Finetuning_Donut_model) to fine-tune and create your own receipt parsing model.

## Getting Started
To get started with REpro, follow these simple steps:

1. Take photos of your receipts on your phone.
2. Upload the photos to your computer and zip them.
3. Open the file `Receipt_information_extraction_LV.ipnyb` in Google Colab.
4. Download the resulting keys.zip file from Google Colab.
5. Unzip the file on your device and check if the parsed information is correct.
6. Enter your Excel template `file template.xlsx` and keys paths ready (right-click on the folder--> properties, copy it from there).
7. Run `Automated_receipt_processing.py`.
8. If additional receipts come up, run steps 1-5 Add_receipts.py and enter the name of the existing Excel file.
9. Finally, you can submit the completed excel report to your clients or government agencies.

## Limitations and Known Issues

There are some limitations and known issues with REpro that users should be aware of:

 - REpro is currently designed for Latvian expense reporting for self-employed individuals and small companies.
 - Users may need to fine-tune the model to extract additional information from receipts.
 - REpro may not work well with low-quality images or poorly formatted receipts.

## Future Developments
We are committed to improving REpro and make it more user-friendly. We are currently working on developing a standalone application for REpro that will make the process even simpler and more streamlined. Our goal is to create an intuitive and user-friendly experience that will save you time and effort while ensuring accurate and efficient processing of your receipts.

## Support
If you have any questions or encounter any issues with REpro, please don't hesitate to reach out for assistance. We are committed to providing prompt and effective support to help you make the most of our tool.

## Conclusion
REpro is a powerful solution for streamlining accounting processes and reducing the burden of receipt processing. By leveraging the latest advancements in automation and machine learning, it eliminates the need for manual data entry, saving time and reducing errors. 

 If you have any feedback or suggestions for improving the tool, please don't hesitate to let us know. 