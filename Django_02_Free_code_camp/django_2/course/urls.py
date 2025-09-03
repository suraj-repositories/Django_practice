
from django.urls import path

from .views import CourseView, CourseListView, ActiveListView, CourseCreateView, CourseUpdateView, CourseDeleteView

app_name = 'course'

urlpatterns = [
    path('', CourseListView.as_view(), name='course_index'),
    path('active-only/', ActiveListView.as_view(), name='course_index_active'),
    path('<int:id>/', CourseView.as_view(), name='course_detail'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),
]
