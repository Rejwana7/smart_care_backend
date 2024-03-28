from rest_framework import serializers
from . import models
# javascript er object notation means json e convert hoye zabe
class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'

# model object ke json ke convert korar process serialization
#e serializtion kajta ze kore take bola hoy serializer