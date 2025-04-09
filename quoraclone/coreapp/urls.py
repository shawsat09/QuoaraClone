from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from coreapp import views  # adjust to your app name

urlpatterns = [
    path('', views.home, name='home'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('ask/', views.post_question, name='post_question'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='coreapp/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    # path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),


]
