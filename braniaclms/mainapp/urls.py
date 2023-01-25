from django.urls import path
from mainapp import views


app_name = 'mainapp'


urlpatterns = [
    path('docs/', views.DocsView.as_view()),
    path('contacts/', views.ContactsView.as_view()),
    path('news/', views.NewsView.as_view()),
    path('courses/', views.CoursesView.as_view()),
    path('login/', views.LoginView.as_view()),
]