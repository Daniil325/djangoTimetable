from django.urls import path
from .views import *

urlpatterns = [
    path('faculty/', FacultyListView.as_view()),
    path('faculty_def/', api_faculties),
    path('employment/', EmploymentListView.as_view()),
]
