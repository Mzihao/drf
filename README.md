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

#豆瓣镜像
pip install -i https://pypi.doubanio.com/simple/ -r requirements.txt
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
# 创建后台管理员
python manage.py createsuperuser 

# 生成数据库迁移文件，后面指定app_name：只针对这个app生成迁移脚本（也可以指定多个）也可以不指定单个APP，生成所有APP的迁移文件。
python manage.py makemigrations app_name

# 将迁移文件内容写入数据库中，并生成数据库表
python manage.py migrate 

# 运行
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
