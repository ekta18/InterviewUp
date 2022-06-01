from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ResumeFiles(models.Model):  
    file = models.FileField() 
  
    class Meta:  
        db_table = "resumefiles"

class File(models.Model):
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return str(self.filepath)

class Tech_News(models.Model):  
    title = models.CharField(max_length=150)
    description = models.TextField() 
    link = models.CharField(max_length=150)
  
    class Meta:  
        db_table = "news_tech"


class Tech_Startup(models.Model):  
    title = models.CharField(max_length=150)
    description = models.TextField() 
    link = models.CharField(max_length=150)
  
    class Meta:  
        db_table = "news_startup"

class Domain(models.Model):
	did = models.IntegerField(db_column='did', primary_key=True)
	dname = models.CharField(db_column='dname', max_length=50)


class Question(models.Model):
	qid = models.IntegerField(db_column='qid', primary_key=True)
	question = models.TextField(db_column='question')
	answer = models.TextField(db_column='answer')
	subdomain = models.CharField(db_column='subdomain', max_length=100)
	did = models.ForeignKey(Domain, on_delete=models.CASCADE, db_column='did')

	class Meta:  
		db_table = "questions"


class RolesCompanies(models.Model):
	rcid = models.IntegerField(db_column='rcid', primary_key=True)
	roles = models.CharField(db_column='roles', max_length=150)
	companies = models.TextField(db_column='companies')
	did = models.ForeignKey(Domain, on_delete=models.CASCADE, db_column='did')

	class Meta:  
		db_table = "roles_companies"










class TechNews(models.Model):  
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200) 
    link = models.CharField(max_length=150)
  
    class Meta:  
        db_table = "newstech"

class StartupNews(models.Model):  
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200) 
    link = models.CharField(max_length=150)
  
    class Meta:  
        db_table = "newsstartup"