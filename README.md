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
```shell
pip install -r requirement.txt
```

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
```shell
python manage.py runserver
```

## docker run
```shell
docker build -t drf:latest .

docker run -it -p 8080:8080 drf
```

## 预览
http://localhost:8080/cached/swagger/

## 运行图
![demo1](https://github.com/Mzihao/drf/blob/master/screenshots/img.png)
