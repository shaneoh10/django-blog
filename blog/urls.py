from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, EditPostView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
]
