from django.db import models

# Create your models here.

class Header(models.Model):
  name = models.CharField(max_length=255)
  job_title = models.CharField(max_length=255)
  description = models.TextField()
  mail = models.EmailField()
  experience = models.CharField(max_length=4)
  projects = models.IntegerField()
  happyClients = models.IntegerField()
  profile_photo = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Project(models.Model):
  title = models.CharField(max_length=255)
  field = models.CharField(max_length=255)
  description = models.JSONField()
  image = models.CharField(max_length=255)
  link = models.CharField(max_length=255)

  def __str__(self):
    return self.title

class SocialMedia(models.Model):
  linkedIn = models.CharField(max_length=255)
  gitHub = models.CharField(max_length=255)
  stackOverFlow = models.CharField(max_length=255)
  
  def __str__(self):
    return "Social Media"

class Education(models.Model):
  title = models.CharField(max_length=255)
  organization = models.CharField(max_length=255)
  date = models.CharField(max_length=255)
  icon_link = models.CharField(max_length=255)

  def __str__(self):
    return self.organization

class Skill(models.Model):
  title = models.CharField(max_length=255)
  icon_link = models.CharField(max_length=255)

  def __str__(self):
    return self.title

class Certificate(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    icon_link = models.CharField(max_length=255)

    def __str__(self):
      return self.title

class OtherSkill(models.Model):
  skill = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.skill

class WorkExperience(models.Model):
  companyName = models.CharField(max_length=255)
  date = models.CharField(max_length=255)
  position = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  experience = models.JSONField()

class Resume(models.Model):
  resume_link = models.CharField(max_length=255)


