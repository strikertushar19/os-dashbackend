from django.db import models

class Organisation(models.Model):
    id=models.AutoField(primary_key=True)
    organisation = models.CharField(max_length=50)
    email = models.EmailField()
    given_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    family_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=150)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    user_note=models.CharField(max_length=200)

    phone_no =models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name
