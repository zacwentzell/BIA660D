#### Instructions to set up the environment to run the Lecture_03/information_extraction.py script:
1) Download the zip file for the pyclausie repo, unzip it (note the file's location) https://github.com/AnthonyMRios/pyclausie
2) Create a new conda environment having python 2, `conda create -n chatbot python=2`
> Be sure to activate the environment before installing any packages (`source activate chatbot` on Mac, `activate chatbot` on Windows [use Anaconda Prompt])

3) Install spacy using conda, `conda install -c conda-forge spacy`
4) CD into the pyclausie directory that you unzipped (should be called `pyclausie-master` unless you changed it, it will contain a file named `setup.py`)
5) install the pyclausie module using `python setup.py install`
6) download the `en` spacy model using `python -m spacy download en`

To run ```information_extraction.py``` in PyCharm, make sure your project interpreter or the interpreter in your run configuration is set to use the chatbot environment:
- https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
- https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html

<br>
<br>
<br>

#### In order to run Lecture_03/flask_apis.py:
1) activate the chatbot environment as you did above
2) `conda install flask flask-restful`