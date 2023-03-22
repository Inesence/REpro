# Finetuning Donut model on your data
Now that you have prepared your data, you can use it to finetune Donut to your specific receipt and output needs.

## Memory Requirements
To train the model on your data, you will need a significant amount of GPU or CPU. If you do not have access to these resources, you can use a freely available tool like Google Colab to train the model on a smaller dataset, such as 200 of your image and key pairs.

## Uploading Your Data to GitHub
The fastest and easiest way to upload your data to Google Colab is by cloning it from your GitHub repository. Here's a quick recap on how to upload your data to GitHub:

1. Create a GitHub account.
2. Create a new GitHub repository.
3. Download Git.
4. Right-click on the folder containing your data on your computer and select "Git Bash here".
 - If this is your first time using Git, you need to set up your Git username and email address by typing the following commands:
`git config --global user.email name.surname@example.com`
`git config --global user.name YourUsernameHere`
Be sure to replace "name.surname@example.com" with your email address and "YourUsernameHere" with your GitHub username.
5. Type "git init" to initialize your Git repository.
6. Type "git remote add origin https://github.com/YourUsername/YourRepository.git" to connect your local repository to your GitHub repository. Be sure to replace "YourUsername" and "YourRepository" with your GitHub account name and repository name, respectively.
7. Use "git add -A" to add all the files in your local repository to Git.
8. Use "git commit -m 'Added folder'" to commit your changes with a message indicating what you've added.
9. Finally, use "git push origin main" to push your changes to the main branch of your GitHub repository.

And that's it! Your repository is now available on GitHub.

## Finetuning Donut on Your Data

Now that your data is ready, you can finetune the Donut model to meet your specific needs. To do this, you can follow the [https://www.philschmid.de/fine-tuning-donut](guide by Philipp Schmid), but using your own data.
To make it easier for you, I've transformed his code to an ipynb format, which you can execute in Google Colab (file `Finetuning_Donut_for_receipt_parsing.ipynb`). Full credits for the original code go to [https://www.philschmid.de/fine-tuning-donut](Philipp Schmid).
