# JuniorIS
# Nepali-English Numeral Recognition

This is a machine learning program that can recognize Nepali and English numerals using image classification techniques. It is trained on a dataset of labeled images of Nepali and English numerals. The models have used Nepali numerals from dataset Ashok Kumar's Devanagari Character Dataset which you can find it in Kaggle. The link is: https://www.kaggle.com/datasets/ashokpant/devanagari-character-dataset. The English Dataset is taken from MNIST.
## Features
1) Recognition of Nepali and English numerals.
2) Takes input of 28 * 28 image format in jpg and png.
3) Ability to classify numerals from 0 to 9 in both Nepali and English languages.
4) User-friendly command-line interface for easy usage.
5) Proper user-interface through the use of Gradio.app but only for Nepali Model.

## Installation

1) You can git clone this repository
2) Download Devanagiri Character Dataset from Kaggle through this link: https://www.kaggle.com/datasets/ashokpant/devanagari-character-dataset built by Ashok Kumar. 
3) Install the required dependencies. This program uses Python and the following libraries:
TensorFlow
Keras
OpenCV
Numpy
Matplotlib
Gradio

## Usage
1) The main file being used here is JuniorIS (1).ipnyb. The recognition.ipnyb and test.ipnyb are initial files where I was testing out functions. 
1) After downloading the necessary materials, copy path of the nepali numerals' dataset and paste put it in for the value of "data_dir" in block 3. 
2) I have included a folder in the repository named "Test cases" where i have few images of 28 * 28 to be tested with the program. You can simply copy the image's path and paste it in block 66's "img_path" variable. I created these test images using JSpaint: https://jspaint.app/ If you wish to create your own test cases, scale the dimensions of the image to width: 28 and length: 28 in the "attribute" section found in "Image" in the toolbar. 
3) You can then download the image and use it's path or the already made test cases to classify what digit of which language it is.
4)  To run this program simply run the jupiter notebook or the JuniorIS (1).ipynb file.  

# Credit

I have used tensorflow's tutorials and documentations for guidance in this project. The link: https://www.tensorflow.org/tutorials/images/classification was my main inspiration for my project.
## Contact
If you have any questions or suggestions, please feel free to contact the project maintainer at atamrakar24@wooster.edu
