from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()
    def _str_(self):
        return self.dep_name
class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    