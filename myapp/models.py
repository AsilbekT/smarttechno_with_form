from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class MxikOption(models.Model):
    option = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.option


class MxikObject(models.Model):
    mxik_options = models.ForeignKey(
        MxikOption, on_delete=models.CASCADE)
    mxik_input = models.FileField(
        upload_to='static/mxik/', blank=True, null=True)
    mxik_output = models.FileField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.mxik_input)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    text = RichTextField()
    image = models.ImageField(
        upload_to="static/blogs_img/", default="static/blogs_img/default.jpg")
    date_created = models.DateField(auto_now=True)
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CompanyDocument(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to="static/documents/")

    def __str__(self) -> str:
        return self.file_name
