# Welcome to my project
## 1.Project Description
   This is a program for crawling Douban top250, which will crawl down the information of each movie and store it in MySQL database, and can generate a front-end page for data analysis
## 2.how to use?
   Please modify the database configuration in the config.yaml file,Open the command line to enter the spider directory.(在本地mysql必须创建test逻辑库)
   ```
    python main.py -s douban -o *.html
```
## 3.rely
   After downloading the project, use the command line to enter the project directory, and enter:
   ```python
    pipenv install
```
To create a virtual environment, enter:
```python
    pipenv shell
```
To open the virtual environment.



