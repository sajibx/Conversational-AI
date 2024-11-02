# Conversational-AI

# Exercise 1. Basic Word Tokenization 

# NLTK Tokenization and Frequency Analysis

This project demonstrates how to use the Natural Language Toolkit (NLTK) in Python to perform basic natural language processing tasks. Specifically, it shows how to tokenize a given text into individual words and calculate the frequency of each word. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Steps](#steps)
  - [Code Explanation](#code-explanation)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

1. Make sure you have Python installed (this guide is compatible with Python 3).
2. Install the `nltk` package. If you are using Google Colab, you can skip this step, as the installation code is provided in the notebook.



## Usage

The main purpose of this project is to:
- Tokenize a text paragraph into individual words.
- Count the total number of words (tokens) in the text.
- Calculate the frequency of each word using NLTK's `FreqDist` function.

### Steps

1. **Install NLTK**: Install the NLTK library to use its natural language processing tools.
2. **Import Required Functions**: Import `word_tokenize` for tokenization and `FreqDist` for frequency analysis.
3. **Define Text**: Provide a paragraph of at least four sentences in a variable called `text`.
4. **Download Tokenizer Data**: Download required NLTK data files (e.g., "punkt") for tokenization.
5. **Tokenize the Text**: Use `word_tokenize` to break down the text into individual tokens (words).
6. **Print Tokens**: Display the list of tokens generated.
7. **Count Tokens**: Display the total number of tokens.
8. **Calculate Token Frequency**: Calculate and display the frequency of each token using `FreqDist`.
9. **Display Detailed Frequency**: Optionally, print each word along with its frequency for more detailed information.

### Code Explanation

The following is a complete Python code block to perform the tasks described above:

python
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


#### Explanation of Each Step

- **Step 1**: Install the NLTK library, which contains tools for natural language processing.
- **Step 2**: Import `word_tokenize` to split sentences into individual words and `FreqDist` to calculate word frequencies.
- **Step 3**: Define the text variable `text` with a paragraph of at least four sentences.
- **Step 4**: Download the "punkt" data, which is necessary for the `word_tokenize` function.
- **Step 5**: Tokenize the text using `word_tokenize`, which creates a list of individual words and punctuation marks.
- **Step 6**: Print the list of tokens to view each word in the text as a separate element.
- **Step 7**: Count the total number of tokens in the list and print it.
- **Step 8**: Use `FreqDist` to calculate the frequency of each token (word) in the text and print the distribution.
- **Step 9**: Display each token with its corresponding frequency for a more detailed view of the distribution.

## Example Output

Here's an example output you can expect from the code above:

Tokens: ['Natural', 'language', 'processing', 'is', 'a', 'field', 'of', 'artificial', 'intelligence', '.', 'It', 'focuses', 'on', 'the', 'interaction', 'between', 'computers', 'and', 'human', 'language', '.', 'The', 'goal', 'is', 'to', 'enable', 'computers', 'to', 'understand', ',', 'interpret', ',', 'and', 'generate', 'human', 'language', '.', 'NLP', 'is', 'used', 'in', 'many', 'applications', ',', 'such', 'as', 'chatbots', 'and', 'machine', 'translation', '.']

Number of tokens: 56

Token Frequencies: <FreqDist with 37 samples and 56 outcomes>

Token Frequency in Detail:

Natural: 1

language: 3

processing: 1

is: 3

a: 1



# Exercise 2. Word Cloud (Google Colab) 

The word cloud displays the most frequently occurring words in a text, with the size of each word corresponding to its frequency. In the genarated image, the most prominent words include “will,” “one,” “now,” “said,” and “Rochester.” These words appear larger, suggesting they are used more frequently in the text compared to smaller words.

Here’s an observation of the word cloud:

	•	“Will” and “Now” are the largest, implying frequent use of future-oriented statements or intentions within the text.
	•	“One,” “said,” and “Rochester” also stand out, indicating a focus on dialogue or a particular character (likely Mr. Rochester).
	•	Other notable words, like “thought,” “face,” “house,” “little,” “eye,” and “heart,” suggest themes of introspection, setting, and emotions.
	•	Character names like “Mr. Rochester,” “St. John,” and “Bessie” imply a narrative involving multiple individuals, potentially with relationships or conflicts among them.



 
