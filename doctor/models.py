from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
            return self.name
class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
#one to many-> many part e kintu foreign key use korte hoy
#ekjon doctor er multiple time thakuk,many time
#ekta service er under e multiple review thakbe
#ekta cart e multiple service thakbe
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete = models.CASCADE)
    image=models.ImageField(upload_to = "doctor/images") 
    designation=models.ManyToManyField(Designation)

    #ekta designation er under e multiple doctor thakte pare,ekta doctor er multople designation thakte pare 
    specialization =  models.ManyToManyField(Specialization)
     #ekta specializtion er under e multiple doctor thakte pare,ekta doctor er multiple specialization thakte pare 
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length = 150)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
          

STAR_CHOICES =[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
    
]
class Review(models.Model):
    reviewer = models.ForeignKey(Patient,on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating=models.CharField(choices=STAR_CHOICES,max_length = 10) 
    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name} ; Doctor {self.doctor.user.first_name}"
