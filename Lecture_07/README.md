##Introduction to Natural Language Processing
In this lecture, we will cover some basics of NLP.
Please create the following conda environment:
```conda create -n nlp spacy nltk jupyter```

Windows users should use an Anaconda Prompt with Admin Privileges.
1) activate the environment
2) There seems to be an issue with spacy in Windows. 
Maybe it's just from updating to the latest conda.<br>
[Windows users run this]<br>
```pip install msgpack-python==0.5.4```
3) Download the `en` language model.<br>
[Windows users should run Anaconda Prompt as Admin]<br>
```python -m spacy download en```

