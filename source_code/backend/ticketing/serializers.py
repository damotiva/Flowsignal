from dataclasses import fields
from rest_framework import serializers

from .models import PatientTicket
from .models import PatientTicketInference

# PatientTicketSerializer Serializer
class PatientTicketSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientTicket
		fields = '__all__'


# PatientTicketInferenceSerializer Serializer
class PatientTicketInferenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = PatientTicketInference
		fields = '__all__'