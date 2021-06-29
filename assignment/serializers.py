from rest_framework import  serializers
from .models import Users

#Simple serialiser to serialise model data
class Contact_Serializer(serializers.ModelSerializer):

    class Meta:
         model = Users
         fields = '__all__'
