from django.db import models
from django.contrib.auth.models import User 
from course.models import Courses

# Create your models here.
class AddCourse(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=200)
    instructor_name = models.CharField(max_length=100)
    price_unit = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=20)
    course_mode =  models.CharField(max_length=100)
    course_url = models.URLField(max_length=200)
    published_date = models.DateTimeField(default=None, blank=True)
    duration = models.DateTimeField(default=None, blank=True)
    prerequistes = models.TextField(default=None,max_length=500)
    description = models.TextField(default=None,max_length=500)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_published:
            course = Courses(course_name=self.course_name,instructor_name=self.instructor_name,price_unit=self.price_unit,price=self.price,category=self.category,course_mode=self.course_mode,course_url=self.course_url,published_date=self.published_date,prerequistes=self.prerequistes,description=self.description)
            course.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Add Course'
        verbose_name = 'Add Course'

    
