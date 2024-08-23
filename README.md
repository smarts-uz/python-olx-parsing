# Olx Parsing

## Quick Start



Also check video [explanation](https://t.me/c/1928723945/46379/49933):





```python
https://github.com/smarts-uz/python-olx-parsing.git
```
 Firstly create venv 
 ```python
py -m venv venv
```
 Activate the virtual envoirment
```python 
venv\scripts\activate 
```
 Third, install the django & django-extensions package:
```python 
 pip install django django-extensions  
 ```
 Then install requirements
```python
pip install -r requirements.txt
```
**Creating a new django_orm  project**
```python
django-admin startproject django_orm
```
Second, create an HR application inside the django_orm project:
```python
cd django_orm
python manage.py startapp hr
```
Cheking and updating DB models
```python 
python manage.py makemigrations
python manage.py migrate
```
Using the parsing system
positional arguments:
  category_id  ID of the category
options:
  -h, --help   show this help message and exit
```python
 python Category_parser_ID.py [category_id] 
```
be sure you have .env file with it credentials













