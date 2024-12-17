from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfile, CustomUser
from .serializers import StudentProfileSerializer


class RegisterView(APIView):
    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        is_student = request.data.get('is_student', False)
        is_educator = request.data.get('is_educator', False)

        if not email or not password:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(username=email, password=password, email=email)
        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class ResetPasswordView(APIView):
    """
    Allows a user to reset their password by providing the old password and a new password.
    """
    def post(self, request):
        email = request.data.get('email')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        # Validate email and old password
        try:
            user = CustomUser.objects.get(email=email)

            # Check if the old password is correct
            if not user.check_password(old_password):
                return Response({"error": "Old password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)

            # Update to the new password
            user.set_password(new_password)
            user.save()

            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "User with this email does not exist."}, status=status.HTTP_404_NOT_FOUND)


class CreateStudentProfileView(generics.CreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        if not user.role == 'student':
            return Response(
                {"error": "Only students can create a student profile."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)