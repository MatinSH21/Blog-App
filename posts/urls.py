from django.urls import path, include

from . import views
from . import api_views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', api_views.PostView, basename='posts')

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-home'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/user/<str:author>', views.UserPostListView.as_view(), name='post-user'),
    path('api/', include(router.urls))
]
