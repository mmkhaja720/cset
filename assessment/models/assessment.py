from django.db import models

# Create your models here.


class Assessment(models.Model):
    assessmentname = models.CharField(max_length=100)
    assessmentdate = models.DateField()
    facilityname = models.CharField(max_length=100)
    cityname = models.CharField(max_length=100)
    statename = models.CharField(max_length=100)
    assessment_options = models.CharField(max_length=100)

    def register(self):
        self.save()

    # @staticmethod
    # def get_user_by_email(email):
    #     return Assessment.objects.get(useremail=email)

    # @staticmethod
    # def get_all_user():
    #     return User.objects.all()

    # def isExist(self):
    #     if User.objects.filter(useremail=self.useremail):
    #         return True
    #     return False
