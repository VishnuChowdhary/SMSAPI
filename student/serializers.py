from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['roll_number', 'first_name', 'last_name', 'mobile', 'address', 'department']
         