from rest_framework import viewsets
from cv_api import models, serializers


class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = models.Projects.objects.all()
    serializer_class = serializers.ProjectSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer


class WorkingExperienceViewSet(viewsets.ModelViewSet):
    queryset = models.WorkingExperience.objects.all()
    serializer_class = serializers.WorkingExperienceSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = models.Skills.objects.all()
    serializer_class = serializers.SkillsSerializer


class SkillTypeViewSet(viewsets.ModelViewSet):
    queryset = models.SkillType.objects.all()
    serializer_class = serializers.SkillTypeSerializer


class PersonalInformationViewSet(viewsets.ModelViewSet):
    queryset = models.PersonalInformation.objects.all()
    serializer_class = serializers.PersonalInformationSerializer


class LanguagesViewSet(viewsets.ModelViewSet):
    queryset = models.Languages.objects.all()
    serializer_class = serializers.LanguagesSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.BlogPost.objects.all()
    serializer_class = serializers.BlogSerializer


class EmailsFromContactsViewSet(viewsets.ModelViewSet):
    queryset = models.EmailsFromContacts.objects.all()
    serializer_class = serializers.EmailsFromContactsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
