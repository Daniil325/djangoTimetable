from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import *
from .serializers import *


class FacultyListView(APIView):
    def get(self, request):
        faculties = Faculty.objects.all()
        serializer = FacultyListSerializer(faculties, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def api_faculties(request):
    if request.method == "GET":
        faculties = Faculty.objects.all()
        serializer = FacultyListSerializer(faculties, many=True)
        return Response(serializer.data)


class EmploymentListView(APIView):
    def get(self, request):
        employments = Employment.objects.all()
        serializer = EmploymentListSerializer(employments, many=True)
        return Response(serializer.data)