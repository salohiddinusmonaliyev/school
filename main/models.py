from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class BestPupil(models.Model):
    ism = models.CharField(max_length=40)
    familya = models.CharField(max_length=40)
    otasining_ismi = models.CharField(max_length=40)
    about = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    tugilgan_yil = models.DateField()
    sinf = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.ism

class Teacher(models.Model):
    TOIFA = (
        ["Oliy toifa", "Oliy toifa"],
        ["1-toifa", "1-toifa"],
        ["2-toifa", "2-toifa"],
    )
    ism = models.CharField(max_length=40)
    familya = models.CharField(max_length=40)
    otasining_ismi = models.CharField(max_length=40)
    toifa = models.CharField(max_length=50, choices=TOIFA)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    fan = models.CharField(max_length=70)

    def __str__(self):
        return self.ism

class Blog(models.Model):
    title = models.CharField(max_length=30)
    text = RichTextField()
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title

class Home(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)
    nom = models.CharField(max_length=41, null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.blog.title

class Grade(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Pupil(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    age = models.IntegerField()
    b_day = models.DateField()

    def __str__(self):
        return self.first_name
