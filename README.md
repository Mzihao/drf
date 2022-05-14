# DRF_study

## 描述
一个结合django rest_framework和drf_yasg的Swagger风格的接口模板。

## version
python 3.9

## 组件
1. Django
2. djangorestframework
3. djangorestframework_simplejwt
4. drf_yasg

## 安装库
pip install -r requirement.txt

## 数据库连接
```python
music/setting.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

## 本地运行
python manage.py runserver

## docker run
docker build -t drf:latest .
docker run -it -rm -p 8080:8080 drf
