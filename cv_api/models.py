from django.db import models
from django.utils.text import slugify


class Projects(models.Model):
    project_title = models.CharField(max_length=252)
    project_description = models.CharField(max_length=255)
    project_published = models.BooleanField()
    project_banner = models.ImageField(default='fallback.png', blank=True)
    project_created = models.DateTimeField(auto_now=True)
    project_updated = models.DateTimeField(auto_now=True)


class Education(models.Model):
    education_title = models.CharField(max_length=252)
    education_description = models.CharField(max_length=252)
    education_published = models.BooleanField()
    education_year = models.CharField(max_length=50)
    education_banner = models.ImageField(default='fallback.png', blank=True)
    education_created = models.DateTimeField(auto_now=True)
    education_updated = models.DateTimeField(auto_now=True)


class WorkingExperience(models.Model):
    working_experience_title = models.CharField(max_length=252)
    working_experience_description = models.CharField(max_length=252)
    working_experience_published = models.BooleanField()
    working_experience_start = models.DateField()
    working_experience_end = models.DateField()
    working_experience_created = models.DateTimeField(auto_now=True)
    working_experience_updated = models.DateTimeField(auto_now=True)


class Skills(models.Model):
    skill_title = models.CharField(max_length=252)
    skill_description = models.CharField(max_length=252)
    skill_type = models.CharField(max_length=2)
    skill_banner = models.ImageField(default='fallback.png', blank=True)
    skill_created = models.DateTimeField(auto_now=True)
    skill_updated = models.DateTimeField(auto_now=True)


class SkillType(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_type_created = models.DateTimeField(auto_now=True)
    skill_type_updated = models.DateTimeField(auto_now=True)


class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    military_obligations_fulfilled = models.BooleanField()
    professional_profile = models.CharField(max_length=500)
    personal_banner = models.ImageField(default='fallback.png', blank=True)
    personal_info_created = models.DateTimeField(auto_now=True)
    personal_info_updated = models.DateTimeField(auto_now=True)


class Languages(models.Model):
    language_name = models.CharField(max_length=50)
    language_level = models.CharField(max_length=50)
    language_created = models.DateTimeField(auto_now=True)
    language_updated = models.DateTimeField(auto_now=True)


class EmailsFromContacts(models.Model):
    sender_full_name = models.CharField(max_length=50)
    sender_email = models.CharField(max_length=50)
    sender_phone_number = models.CharField(max_length=50)
    sender_email_subject = models.CharField(max_length=50)
    sender_email_body = models.TextField()
    sender_email_created_at = models.DateTimeField(auto_now=True)
    sender_email_updated_at = models.DateTimeField(auto_now=True)
