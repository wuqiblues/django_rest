from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()

# 项目表
class Project(models.Model):
    name = models.CharField(max_length=30)
    describe = models.TextField(blank=True, null=True)

# 应用表
class App(models.Model):
    name = models.CharField(max_length=30)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # 一对多
    describe = models.TextField(blank=True, null=True)

# 服务器表
class Server(models.Model):
    hostname = models.CharField(max_length=30)
    ip = models.GenericIPAddressField()
    app = models.ManyToManyField(App) # 多对多
    describe = models.TextField(blank=True, null=True)
