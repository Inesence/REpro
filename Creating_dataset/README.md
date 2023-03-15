# Creating_dataset
This folder provides a guide on how to prepare the dataset for training the Donut model to parse and process receipts. 

Here we will use two types of document parsing methods: OCR-based and non-OCR based.

## Taking photos of the receipts

1. Ensure good lighting: Take photos of the receipts in a well-lit area or use the phone's flash to illuminate the receipt. Poor lighting can make the text hard to read and result in inaccurate OCR results.

2. Position the camera correctly: Position the camera directly above the receipt and ensure that the entire receipt is in the frame. Keep the camera steady and avoid shaking or moving it while taking the photo.

3. Avoid shadows and glare: Make sure there are no shadows or glare on the receipt. Shadows can make the text hard to read, while glare can reflect light and obscure the text.

4. Keep the receipt flat and uncreased: Flatten the receipt and ensure that it is not creased or folded. Creases and folds can distort the text and make it difficult for Tesseract to recognize it.

5. Use high-resolution settings: Set the camera to capture photos at the highest possible resolution. Higher resolution photos will have more detail, making it easier for Tesseract to recognize the text.

6. Use a contrasting background: When taking photos of receipts, it's important to use a background that contrasts with the receipt itself. For example, if the receipt is white, use a dark background, and if the receipt is dark, use a light background. This will make the text stand out and be easier for Tesseract to recognize. Additionally, avoid using busy or patterned backgrounds that could interfere with the OCR process. A plain, uncluttered background will help ensure that the receipt is the main focus of the photo.

## OCR-based vs Non-OCR based Document Parsing
| Method        |	Pros                        |	                           Cons |
| ------------- | --------------------------------- | --------------------------------- |
| OCR-based	| - Quick and easy to use.<br>- Can recognize characters in different languages. |	- Accuracy is dependent on the quality of the image.<br>- May fail to recognize certain fonts or styles of text.<br>- Cannot recognize handwriting or images. <br>- For finetuning on your dataset requires defining OCR boxes, which can be time-consuming.|
| Non-OCR based	| - Can recognize handwriting or images.<br>- More accurate and reliable than OCR.<br>- Easier to prepare data for training, as no special API or box definitions are required. <br>- May be more robust to varying image quality and font styles. |	- Requires computing resources: Fine-tuning a pre-trained model like Donut may require significant computing resources, such as GPU-enabled servers or cloud computing services.<br>- Limited to specific types of documents.|

## Preparing your dataset for finetuning **Donut**
For non-OCR based document parsing with [Donut](https://huggingface.co/docs/transformers/model_doc/donut), we will need to create pairs of data points and images and extract the necessary information in a .json file. In this case, we require the **total sum** of the receipt, **the name of the vendor**, **the taxpayer's number of the vendor**, **the date**, **time**, and **receipt number**.

For ease of implementation, we will create two folders within the "data" folder:
- "img" that contains the images and 
- "key" that contains the .json files. 

The images will be named 000.jpg, 001.jpg, and so on, and the corresponding .json files will be named 000.json, 001.json, and so on.

In the code "data_extraction_with_OCR.py," we will use Tesseract to extract the date, time, and taxpayer number. 
Then, in "vendor_extraction_with_DONUT.ipyb," we will use the ["naver-clova-ix/donut-base-finetuned-cord-v2" model](https://huggingface.co/naver-clova-ix/donut-base-finetuned-cord-v2)  to add the vendor name to the .json files. 

However, it may be challenging to extract the total sum and receipt number automatically, so we may need to input those manually or if you feel up to the challange you adjust the code to recognize them automatically.

## data_extraction_with_OCR.py

This code uses the pytesseract library to extract information from photos and create JSON files. Before running the code, you need to install `pytesseract` and set the path to the Tesseract executable using the `pytesseract.pytesseract.tesseract_cmd` variable in line 16. You also need to specify the path to the image folder by setting the `folder_path` variable, and then execute the `process_images_in_folder(folder_path) function` in line 122.

This code will create **data** folder with renamed image files in **img** subfolder and corresponding json files in **key** subfolder.

## Summary
This folder provides a step-by-step guide on how to prepare the dataset for training the Donut model using non-OCR based document parsing. By following these instructions, you can extract the necessary information from receipts and streamline the expense reporting process.
