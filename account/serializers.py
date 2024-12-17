from rest_framework import serializers
from .models import StudentProfile, CustomUser


class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = ['purchased_channels', 'sex', 'age', 'city']
        extra_kwargs = {
            'purchased_channels': {'required': False},
        }
