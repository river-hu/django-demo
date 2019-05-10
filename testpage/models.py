from django.db import models

class Person(models.Model):
    size = (
        ('m','数学'),
        ('c','语文'),
        ('e','英语')
    )
    frist_name = models.CharField("姓名",max_length=30,help_text='输入姓名')
    last_name = models.CharField("签名",max_length=240,null=True,blank=True,help_text='输入签名')
    size_name = models.CharField('科目',max_length=1,choices=size,default='m',help_text='选择科目')
    def __str__(self):
        return self.frist_name

class interest(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    interest_name = models.CharField("兴趣的名字",max_length=10,help_text="请输入兴趣名")
    def __str__(self):
        return self.interest_name

