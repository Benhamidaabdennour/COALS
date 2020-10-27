# COALS-Correlated-Occurrence-Analogue-to-Lexical-Semantics
This work is supported by the Ministry of Higher Education and Scientific Research in Algeria (Project C00L07UN100120180002)
Conception & Supervision : L. Ouahrani & D. Bennouar /  Contributor : Abdennour BenHamida.

This code allows you to compute and save a COALS model for a text document. The output file contains:
- A dictionnary with every vector word representation according to the retained words after cleaning
- A list of the words

1- Requirments:
- You may need to enable these two commandes if your punkt isn't installed, once dowloaded and installed nltk will work perfectly fine: #1- import nltk #2- nltk.download('punkt')
- Python 2.7 or later
- At least 10mb of storage
- For better results, at 18gb of ram is needed, for models with 14k words. You can still use google colab for up to 30k words using the free version.
- "Stopwords.txt"

2- Libraries used:
- re.sub: function that alllow as to delete portions of text that are or not in the text
- word_tokenize: we use to tokenize (split) our texts into a list of words
- math: used to compute "sqrt"
- json: files.json management

3- How to use:
- If your input is a".txt" file, you need to read it with the "fromTxt(Path)" function included in the "COALS.py" file.
- Otherwise, directaly launch the "getSemSpace" function with your text
- Keep in mind that a considerable size of RAM is needed, make sure you have enough left for your system.

For further questions or inquiries about this code, you can contact:
- abdennourbenhamida09@gmail.com
