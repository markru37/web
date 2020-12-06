from django.db import models
from django import forms

class Human(models.Model):
     email = models.EmailField()
     password = models.CharField(max_length=20, verbose_name="Пароль")
     login = models.CharField(max_length=15 , verbose_name="Ник")



     # def __str__(self):
     #     return 'Почта - [0] , Ник - [1] , Пароль - [2]'.format(self.email , self.login, self.password)
     


