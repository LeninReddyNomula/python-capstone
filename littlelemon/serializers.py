from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu,BookingTable

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']
        
        
class PasswordSerializer(serializers.Serializer):
    
    password = serializers.CharField(max_length = 15)
    
    

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','title','price','inventory']
        
class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingTable
        fields = ['url','id','name','booking_date','no_of_guests']
        extra_kwargs ={
            'url':{'view_name' : 'booking-detail'}
            
        }