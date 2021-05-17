from django.db import models

# Create your models here.


class User(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    useremail = models.CharField(max_length=100)
    userimage = models.ImageField(upload_to='users/')
    userPassword = models.CharField(max_length=200)
    usertype = models.CharField(max_length=50)

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        return User.objects.get(useremail=email)

    @staticmethod
    def get_all_user():
        return User.objects.all()

    def isExist(self):
        if User.objects.filter(useremail=self.useremail):
            return True
        return False
