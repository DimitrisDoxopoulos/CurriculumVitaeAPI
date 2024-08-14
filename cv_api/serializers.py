from rest_framework import serializers
from cv_api import models


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'


class WorkingExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkingExperience
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = '__all__'


class SkillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkillType
        fields = '__all__'


class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PersonalInformation
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Languages
        fields = '__all__'


class EmailsFromContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmailsFromContacts
        fields = '__all__'
