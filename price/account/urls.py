from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,


)
from .views import RegisterView, ResetPasswordView, CreateStudentProfileView, StudentProfileCreateUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('student-profile/', CreateStudentProfileView.as_view(), name='create-student-profile'),
    path('student-info/', StudentProfileCreateUpdateView.as_view(), name='create-student-profile'),
]
