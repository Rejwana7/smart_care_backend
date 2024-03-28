from rest_framework import serializers
from . import models

class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False)
    #ekta appointment e ekta time thakbe
    patient = serializers.StringRelatedField(many=False)
    #ekoy time e ekjon paitent 
    doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Appointment
        fields = '__all__'


#model ta json e convert kore dibe        