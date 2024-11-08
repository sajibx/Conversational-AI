# -*- coding: utf-8 -*-
"""ps03_Ashiqur Rahman.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ix2QWY6WPGBLp96bpTQ8zpjGL08WnDb5
"""

# Step 1: Install NLTK
!pip install nltk

# Step 2: Import the necessary functions
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Step 3: Define the text
text = "Natural language processing is a field of artificial intelligence. It focuses on the interaction between computers and human language. The goal is to enable computers to understand, interpret, and generate human language. NLP is used in many applications, such as chatbots and machine translation."

# Step 4: Download NLTK data for tokenization
import nltk
nltk.download('punkt')

# Step 5: Tokenize the text
tokens = word_tokenize(text)

# Step 6: Print the tokens
print("Tokens:", tokens)

# Step 7: Count the number of tokens
print("Number of tokens:", len(tokens))

# Step 8: Calculate the frequency of each token
freq_dist = FreqDist(tokens)
print("Token Frequencies:", freq_dist)

# Step 9: Display token frequency in detail
for token, frequency in freq_dist.items():
    print(f"{token}: {frequency}")

# Step 1: Install WordCloud
!pip install wordcloud

# Step 2: Import Required Libraries
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Step 3: Google Drive in Colab
from google.colab import drive
drive.mount('/content/drive')

# Step 4: Load the Text File
with open("/content/drive/My Drive/Colab Notebooks/JaneEyre.txt", "r") as file:
    text = file.read()

# Step 5: Create a WordCloud Object
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=set(STOPWORDS),
    max_words=100,
    min_font_size=10,
).generate(text)

# Step 6: Display the Word Cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# Step 7: Load the Mask Image
from PIL import Image
import numpy as np

mask_path = "/content/drive/My Drive/Colab Notebooks/mask_image.png"  # Update with your mask image path
mask = np.array(Image.open(mask_path))

# Step 8: Create a WordCloud Object with the Mask
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    mask=mask,                   # Apply the mask here
    stopwords=STOPWORDS,
    contour_width=1,             # Optional: Add contour to the mask shape
    contour_color='black'        # Optional: Color of the contour
).generate(text)

# Step 9: Display the Shaped Word Cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()