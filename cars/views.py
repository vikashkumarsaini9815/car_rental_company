from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Car,SeftyFeature,UserProfile
#from django.http import Http404
from cars.serializers import UserProfileSerializer,CarSerializer

# Create your views here.

def index(reuest):
    return render(reuest , 'selectscars.html')
def registration(reuest):
    return render(reuest , 'create_vehicles.html')    

#   create user profile

class CreateUser(APIView):
    def post (self, request, format = None):
        data = request.data
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  create vehicales

class CreateVehicales(APIView):
    def post (self, request, format = None):
        data = request.data
        car_types = data["car_type"]
        registrations = data["registration"]
        features = data ["feature"]
        c = Car(car_type = car_types,registration = registrations )
        c.save()
        for row in features :
            s = SeftyFeature(feature = row,car=c)
            s.save()
       # s = SeftyFeature(feature = features[1],car=c)
       # s.save()
       # s = SeftyFeature(feature = features[2],car=c)
       # s.save()
        
        return Response({"succese":True}, status=status.HTTP_201_CREATED)



#  booking cars

class Booking(APIView):
    def post (self, request, format = None):
        data = request.data
        car_types = data["car_type"]
        features = data ["feature"]
        cars = Car.objects.filter(car_type=car_types,is_Booked = False)
        for carobj in cars :
            avel_feature= []
            for feature in features:
                sefty = SeftyFeature.objects.filter(car =carobj,feature=feature)
                if not sefty:
                    break
                else:
                    avel_feature.append(sefty)
            if len(avel_feature)==len(features):
                return Response({'is_available':True , "registration":carobj.registration}, status=status.HTTP_200_OK)

        return Response({'is_available':False }, status=status.HTTP_200_OK)       
