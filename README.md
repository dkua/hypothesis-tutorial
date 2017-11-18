# Tutorial: Writing tests that write themselves

Code and slides for my Hypothesis tutorial at PyCon Canada 2017.
All dependencies needed are listed in `requirements.txt`.
Was written for Python 2.7.12 but any version of 2.7 should work.

SSID: Visiteurs UQAM
User: pycon001
pass: x6u4Z5W4

### Quickstart
1. Make sure you have `Python 2.7` and `pip` installed
2. Git clone this repo or download the zip file: https://github.com/dkua/hypothesis-tutorial/archive/master.zip
3. Once cloned or unzipped, go into the `hypothesis-tutorial` folder
4. Run `pip install -r requirements.txt`

### Running the exercises
Inside of the `hypothesis-tutorial` folder:
```
pytest <exercise folder>
```
If you want to run with extra Hypothesis stats:
```
pytest --hypothesis-show-statistics <exercise folder>
```

### Extra materials
Hypothesis documentation: http://hypothesis.readthedocs.io/

Hypothesis GitHub repo: https://github.com/HypothesisWorks/hypothesis-python/

The talk version of this tutorial from PyCon Canada 2016 is online at: https://www.youtube.com/watch?v=SQcCmCyuVyo

A copy of the QuickCheck paper can be found in this repo.
