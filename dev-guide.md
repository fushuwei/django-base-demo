# django-base-demo 项目搭建步骤

## 创建项目

```shell
django-admin startproject django_base_demo django-base-demo
```

## 创建虚拟环境

```shell
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境（Windows系统下是 Scripts 目录，Linux系统对应的是 bin 目录）
venv\Scripts\activate

# 退出虚拟环境
deactivate
```

## 升级pip版本

```shell
python -m pip install --upgrade pip
```

## 安装依赖包

```shell
# 生成 requirements.txt 文件
pip freeze > requirements.txt

# 安装依赖包
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

# 部署

```shell
https://docs.djangoproject.com/zh-hans/2.2/howto/deployment/wsgi/
```
