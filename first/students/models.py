from django.db import models
from django.db import models
from django.urls import reverse


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=120)
    school = models.TextField(blank=True, null=True)
    course = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("students:student-detail", kwargs={"id": self.id})