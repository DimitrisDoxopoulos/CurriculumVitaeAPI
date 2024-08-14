from rest_framework import routers
from cv_api import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectsViewSet, basename='projects')
router.register('education', views.EducationViewSet, basename='education')
router.register('working-experience', views.WorkingExperienceViewSet, basename='working-experience')
router.register('skills', views.SkillsViewSet, basename='skills')
router.register('skill-type', views.SkillTypeViewSet, basename='skill-type')
router.register('personal-information', views.PersonalInformationViewSet, basename='personal-information')
router.register('languages', views.LanguagesViewSet, basename='languages')
router.register('emails-from-contacts', views.EmailsFromContactsViewSet, basename='emails-from-contacts')
router.register('blog', views.BlogViewSet, basename='blog')
router.register('category', views.CategoryViewSet, basename='category')
router.register('tag', views.TagViewSet, basename='tag')
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = []

urlpatterns += router.urls
