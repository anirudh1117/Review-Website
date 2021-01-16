from django.db import models

# Create your models here.
CHOICES1=(('INR','₹'),('USD','$'),('EUR','€'),('YEN','¥'),)
CHOICES2=(('test1','test1'),('test2','test2'),('test3','test3'),('test4','test4'),)

class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    instructor_name = models.CharField(max_length=100)
    price_unit = models.CharField(max_length=20,choices=CHOICES1,default="INR")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20,choices=CHOICES2,default="test1")
    course_mode =  models.CharField(max_length=100)
    course_url = models.URLField(max_length=200)
    published_date = models.DateTimeField(default=None, blank=True)
    prerequistes = models.TextField(max_length=500)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = 'Courses'
        verbose_name = 'Course'
    
    


