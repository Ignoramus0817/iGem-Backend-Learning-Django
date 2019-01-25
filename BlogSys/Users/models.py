from django.db import models

# Create your models here.

GENDER_CHOICE = (
    (u'M', u'Male'),
    (u'F', u'Female'),
)

class User(models.Model):
    userID = models.IntegerField(unique = True)
    userName = models.CharField(max_length = 20, unique = True)
    passWord = models.CharField(max_length = 30)
    nickName = models.CharField(max_length = 30, unique = True)
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICE)
    email_Address = models.EmailField(max_length = 254, blank = True)
    personalSign = models.CharField(max_length = 100, blank = True)   
    def __unicode__(self):
        return self.nickName