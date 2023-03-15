# Creating_dataset
This folder provides a guide on how to prepare the dataset for training the Donut model to parse and process receipts. 

Here we will use two types of document parsing methods: OCR-based and non-OCR based.

## OCR-based vs Non-OCR based Document Parsing
| Method        |	Pros                        |	                           Cons |
| ------------- | --------------------------------- | --------------------------------- |
| OCR-based	| - Quick and easy to use.<br>- Can recognize characters in different languages. |	- Accuracy is dependent on the quality of the image.<br>- May fail to recognize certain fonts or styles of text.<br>- Cannot recognize handwriting or images. <br>- Requires defining OCR boxes, which can be time-consuming.|
| Non-OCR based	| - Can recognize handwriting or images.<br>- More accurate and reliable than OCR.<br>- Easier to prepare data for training, as no special API or box definitions are required. <br>- May be more robust to varying image quality and font styles. |	- Requires computing resources: Fine-tuning a pre-trained model like Donut may require significant computing resources, such as GPU-enabled servers or cloud computing services.<br>- Limited to specific types of documents.|

For non-OCR based document parsing, we will need to create pairs of data points and images and extract the necessary information in a .json file. In this case, we require the total sum of the receipt, the name of the vendor, the taxpayer's number of the vendor, the date, time, and receipt number.

For ease of use, the code will create two folders within the "data" folder: "img" that contains the images and "key" that contains the .json files. The images will be named 000.jpg, 001.jpg, and so on, and the corresponding .json files will be named 000.json, 001.json, and so on.

In the code "data_extraction_with_OCR.py," we will use Tesseract to extract the date, time, and taxpayer number. Then, in "vendor_extraction_with_DONUT.ipyb," we will use the "naver-clova-ix/donut-base-finetuned-cord-v2" model to add the vendor name to the .json files. However, it may be challenging to extract the total and receipt number automatically, so we may need to input those manually or adjust the code to recognize them automatically.

##Summary
This folder provides a step-by-step guide on how to prepare the dataset for training the Donut model using non-OCR based document parsing. By following these instructions, you can extract the necessary information from receipts and streamline the expense reporting process.