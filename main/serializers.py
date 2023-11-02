from rest_framework import serializers
from .models import *


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ("name", "slug")


class EmploymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = ("__all__")