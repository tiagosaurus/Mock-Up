# Mock-Up
Mock Up of DB
## How To install
Make sure you have following software installed in your system.
* Python
* pip3

Create project folder and clone the repository inside of it.
```
mkdir [project-name]
cd [project-name]
git clone https://github.com/GeonYoon/django-rest.git
```
------------------------------------------
### This section is only for mac user
```
pip3 install virtualenv 
```

Create virtual environment on the same dir where this project root folder is located at. 
Activate the environment

```
virtualenv [name]
source [name]/bin/activate 
```
------------------------------------------

Install all the dependencies for the project.

```
cd [project folder]
pip install -r requirements.txt
python manage.py migrate
```
Run server with following line
```
python manage.py runserver
```