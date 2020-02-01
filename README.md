# Welcome to my project
## 1.Project Description
   Django embeds a "spider" script, grabs Douban top250 movie information, saves it to a mysql database, and displays data analysis on the command line or web page.
## 2.How to use?
   You must create a 'settings_local.py' file in the project root directory, which contains some passwords, users and other information of your mysql database, so that django can connect to the mysql database. You can use the following command to start running 'spider' ,Here, -o, the parameter must end with '.html', this parameter is used to generate web pages.
   ```
python manage.py spider -s douban -o *.html
```
    
## 3.Rely
   After downloading the project, use the command line to enter the project directory, and enter:
   ```python
pipenv install
```
To create a virtual environment, enter:
```python
pipenv shell
```
To open the virtual environment.
