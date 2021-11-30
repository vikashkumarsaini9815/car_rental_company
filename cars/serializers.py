from rest_framework import serializers
from .models import UserProfile,Car,SeftyFeature


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_name','contact','Email']    


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['car_type','registrastion']      


class SeftyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeftyFeature
        fields = ['feature',]            