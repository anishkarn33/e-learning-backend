from django.urls import path
from .views import (RegisterView, LoginView, LogoutView, StatusUpdateView, CourseCreateView, CourseListView, CourseDetailView,
                    EnrollmentCreateView, FeedbackCreateView, FileCreateView, TeacherListView, StudentListView, BlockStudentView)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/status-update/', StatusUpdateView.as_view(), name='status_update'),
    path('api/courses/', CourseCreateView.as_view(), name='create_course'),
    path('api/courses/list/', CourseListView.as_view(), name='list_courses'),
    path('api/courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('api/enrollments/', EnrollmentCreateView.as_view(), name='create_enrollment'),
    path('api/feedbacks/', FeedbackCreateView.as_view(), name='create_feedback'),
    path('api/files/', FileCreateView.as_view(), name='create_file'),
    path('api/teachers/', TeacherListView.as_view(), name='list_teachers'),
    path('api/students/', StudentListView.as_view(), name='list_students'),
    path('api/block-student/<int:pk>/', BlockStudentView.as_view(), name='block_student'),
]
