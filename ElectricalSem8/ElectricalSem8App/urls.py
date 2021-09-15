from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('Courses/<str:discipline>/',views.course_list, name="course_list"),
    path('Course_Prompt/<str:name>/',views.course_prompt, name="course_prompt"),
    path('Course_Videos/<str:name>/',views.course_videos,name="course_videos"),
    path('Course_Documents/<str:name>/',views.course_documents,name="course_documents"),
    path('Course_About/<str:name>/',views.course_about,name="course_about"),
    path('Add_Student/', views.StudentCreate.as_view(),name='add_student'),
    path('Student_Details/<int:Id>/',views.student_details, name='student_details'),
    path('Add_Group/', views.add_group, name='add_group'),
    path('Separate/',views.separate, name='separate'),
    path('viewerlogin/<int:logged_out>/', views.viewer_login, name='viewer_login'),
    path('viewerlogin/', views.viewer_login, name='viewer_login'),
    path('viewerlogout/', views.viewer_logout, name='viewer_logout'),
    path('project_registration/', views.project_registration, name='project_registration'),
    path('vote/',views.vote,name='vote'),
    path('grades/',views.grades,name='grades'),
]
