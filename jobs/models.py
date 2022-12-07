from django.db import models
# from django.contrib import admin

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    github_link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.summary

# Create your models here.
# @admin.register(models.Model)
# class Job(admin.ModelAdmin):
#     image = models.ImageField(upload_to='images/')
#     summary = models.CharField(max_length=200)
#     github_link = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.summary


