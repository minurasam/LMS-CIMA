from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('courses', views.courses, name='courses'),
    # ---------------------------------------------------------
    path('courses/certificate_level/', views.cert, name='cert'),
    path('courses/operational_level/', views.op, name='oper'),
    path('courses/management_level/', views.mgt, name='mgt'),
    path('courses/strategic_level/', views.strat, name='strat'),
    # ---------------------------------------------------------
    path('accounts/prof/', views.admin, name='admin'),
    path('accounts/prof/courses', views.view_courses, name='v_courses'),
    path('account/prof/create-couses', views.create_course, name='c_course'),
    path('account/prof/up-couses/<str:pk>/', views.update_course, name='up_course'),
    path('account/prof/del-couses/<str:pk>/', views.delete_course, name='del_course'),
    path('accounts/prof/courses/content/', views.course_modules_1, name='view_content'),
    url(r'^accounts/prof/courses/content/(?P<course_id>\d+)/$', views.course_modules_2, name='course_mods'),

    path('account/prof/crsmod-update-couses/<str:pk>/', 
    views.CourseModuleUpdateView.as_view(), 
    name='crsmod_update'),

    url(r'^account/prof/module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$', 
    views.ContentCreateUpdateView.as_view(), 
    name='module_content_create'),

    url(r'^account/prof/module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/$', 
    views.ContentCreateUpdateView.as_view(), 
    name='module_content_update'),

    url(r'^account/prof/module/content/(?P<id>\d+)/delete/$', 
    views.ContentDeleteView.as_view(), 
    name='module_content_delete'),

    url(r'^account/prof/module/(?P<module_id>\d+)/$', 
    views.ModuleContentListView.as_view(), 
    name='module_content_list'),
 
    path('accounts/prof/content', views.content, name='lecnotesvids'),
    path('accounts/prof/editstudent', views.student_edit, name='edit_stud'),
    path('accounts/prof/es/cs', views.load_course, name='courses_dropdown'),
    path('accounts/prof/es/cs1', views.stud_data, name='std_list'),
    path('accounts/prof/lec_notes', views.lecture_notes, name='addNotes'),
    path('accounts/prof/students', views.student_profile, name='v_students'),
    # ----------------------------------------------------------------------------
    path('accounts/stud_prof/', views.student, name='student'),
    path('accounts/stud_prof/student', views.students_profile, name='profilepage'),
    
    url(r'^accounts/stud_prof/dashboard/$',
    views.StudentCourseListView.as_view(),
    name='student_course_list'),

    url(r'^course/(?P<pk>\d+)/$',
    views.StudentCourseDetailView.as_view(),
    name='student_course_detail'),

    url(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$',
    views.StudentCourseDetailView.as_view(),
    name='student_course_detail_module'),

    # path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]