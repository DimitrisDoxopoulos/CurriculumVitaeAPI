from rest_framework import routers
from blog import views

router = routers.DefaultRouter()

router.register('blog', views.BlogViewSet, basename='blog')
router.register('category', views.CategoryViewSet, basename='category')
router.register('tag', views.TagViewSet, basename='tag')
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = []

urlpatterns += router.urls
