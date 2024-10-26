# Sudoku Solver

http://sudokusolverai.pythonanywhere.com - sometimes loads on a 2nd time, server side issue

## Setup
There is no database needed so makemigrations and migrate are not needed but you may see some warning messages without doing that, which is fine as well.
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Go to provided link (http://127.0.0.1:8000/ by default)

## Description

This is a web-application built using Django, primarily with vanilla JavaScript, although refactored with React along the way.
Purpose of this tool was to create a self-generating sudoku puzzle to solve. Alternatively, if anyone needs help
solving sudoku from other source, like a magazine or other website, they can input these values into the custom section
of this web-app and get the solution automatically from the backend that uses the backtracking algorithm.

Currently, React is being added directly using HTML script tags. In the future possible division between back and front with React
fully installed, although for such a small project it might not be needed.


