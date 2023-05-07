from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CoursesListView.as_view(), name='course-list'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('update/<int:pk>/', views.CourseUpdateView.as_view(), name='course-update'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course-delete'),
    path('create/', views.CourseCreateView.as_view(), name='course-create'),
]
