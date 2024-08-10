from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class Mechanics(models.Model):

    username=models.CharField(max_length=50 , default="")
    pass1=models.CharField(max_length=50 , default="")
    




class Workshops(models.Model):
    shop_name = models.CharField(max_length=255)
    mechanic_name = models.CharField(max_length=255)
    address = models.CharField(max_length=355)
    number = models.CharField(max_length=12)
    service = models.CharField(max_length=255)
    vehicle_types = models.CharField(max_length=22)
    image = models.CharField(max_length=2500)


class Reviews(models.Model):

    Enter_Name = models.CharField(max_length=30)
    Write_review = models.CharField(max_length=30)


class Request(models.Model):
    id = models.AutoField(primary_key=True)

    Name = models.CharField(max_length=30)
    Vehicle_Type = models.CharField(max_length=30)
    Vehicle_No = models.CharField(max_length=30)
    Problem = models.CharField(max_length=30)
    status = models.IntegerField(default=0)



class Call(models.Model):

    Mobile_no = models.CharField(max_length=30)
    SMS = models.CharField(max_length=30)


class Users(models.Model):


    username = models.CharField(max_length=50 , default="")
    pass1=models.CharField(max_length=50 , default="")
    

    def __str__(self):
        return self.username


