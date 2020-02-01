# *_*coding:utf-8 *_*
# __author__ = 'GonzaloWang'
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'ww19971214',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
