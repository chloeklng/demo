from django.db import models
import os

class JD(models.Model):
    file = models.FileField(upload_to='JD/')
    
class CV(models.Model):
    file = models.FileField(upload_to='CV/')
