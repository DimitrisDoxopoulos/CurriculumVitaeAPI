from rest_framework import serializers
from . import models


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


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogPost
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
