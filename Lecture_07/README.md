##Introduction to Natural Language Processing
In this lecture, we will cover some basics of NLP.
Please create the following conda environment:
```conda create -n nlp spacy nltk jupyter```

Windows users should use an Anaconda Prompt with Admin Privileges.
1) activate the environment
2) There seems to be an issue with latest spacy module in the anaconda channel. 
Run this after installing spacy<br>
```pip install msgpack-python==0.5.4```
3) Download the `en` language model.<br>
[Windows users should run Anaconda Prompt as Admin]<br>
```python -m spacy download en```
4) Install pycorenlp<br>
```pip install pycorenlp```

