from django.db import models

# Create your models here.


class Demography(models.Model):
    sector = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    asset_gross_value = models.CharField(max_length=100)
    expected_effort = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=100)
    business_unit = models.CharField(max_length=100)
    organization_type=models.CharField(max_length=100)
    facilitator=models.CharField(max_length=100)
    critical_service_point=models.CharField(max_length=100)
    include_other_enterprise_business_units=models.CharField(max_length=100)
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
