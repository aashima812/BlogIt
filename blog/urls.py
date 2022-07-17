from django.urls import path
from . import views
#for list view
from .views import PostListView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view() , name='user-posts'),
    # path('', views.home , name='blog-home'),
    #<model>_form.html->default
    path('post/new/', PostCreateView.as_view() , name='blog-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name='blog-update'),
    #<model>_<viewtype>.html->default
    path('post/<int:pk>/', PostDetailView.as_view() , name='blog-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='blog-delete'),
    path('about/', views.about , name='blog-about'),
]