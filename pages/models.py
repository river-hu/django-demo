from django.db import models

class Blog(models.Model):
    name = models.CharField('文章标题',max_length=100)
    tagline = models.TextField('标签')
    def __str__(self):
        return self.name

class Auther(models.Model):
    name = models.CharField('作者姓名',max_length=20)
    email = models.EmailField('作者联系邮箱')
    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline = models.CharField('内容摘要',max_length=255)
    body_text = models.TextField('文章内容')
    pub_date = models.DateField('创建日期')
    mod_date = models.DateField('修改日期')
    auther = models.ManyToManyField(Auther)
    n_comments = models.IntegerField('评论数量')
    n_pingbacks = models.IntegerField('阅读量')

    def __str__(self):
        return self.headline



