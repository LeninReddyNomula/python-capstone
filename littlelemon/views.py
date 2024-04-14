from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status,generics
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin,CreateModelMixin 
from rest_framework.response import Response
from .serializers import UserSerializer, PasswordSerializer,MenuSerializer,BookingSerializer

#models
from .models import Menu,BookingTable

class UserView(viewsets.ModelViewSet):
    
    
    
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'set_password':
            return PasswordSerializer
        else:
            return UserSerializer
        
    @action(detail=True, methods=['post','get'])
    def set_password(self,request,pk=None):
        user  =User.objects.get(pk=pk)
        print(request.method)
        if request.method == 'POST':
            new_password = request.POST.get('password')
            serializer_class = self.get_serializer_class()
            serializer =serializer_class(data = {'password':new_password},context={'request':request})
            
            if serializer.is_valid():
                user.set_password(serializer.validated_data['password'])
                user.save()
                print("am here")
                return Response({'status': 'Password set successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({"something wrong":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
        
            return Response("")#serialier.data, status=status.HTTP_200_OK)

        
    def list(self,request):
        serializer_class = self.get_serializer_class()
        queryset = self.get_queryset()
        
        serializer = serializer_class(queryset,many=True,context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    def create(self, request):
        queryset = self.get_queryset()  # Accessing get_queryset method
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND) 
    
    
class MenuItemView(generics.ListCreateAPIView,CreateModelMixin,viewsets.GenericViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def list(self, request):
        
        serializer = self.serializer_class(self.get_queryset(),many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    


class SingleMenuItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def retrieve(self, request, pk=None):
        menuitem = Menu.objects.get(pk=pk)
        print(menuitem)
        serializer = self.serializer_class(menuitem)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    def destroy(self, request, pk=None):
        menuitem = Menu.objects.get(pk=pk)
        
        if menuitem:
            menuitem.delete()
            return Response({'message:Deleted successfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message:Item not available'},status=status.HTTP_400_BAD_REQUEST)
        


class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer
    
    
    def list(self,request):
        
        data = self.get_queryset()
        serializer = self.serializer_class(data,context={'request':request},many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        bookings = self.get_queryset()
        booking = get_object_or_404(bookings,pk=pk)
        booking.delete()  # Delete the booking instance
        return Response({"message:deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        
    
    def retrieve(self,request,pk=None):
        queryset = self.get_queryset()
        booking = get_object_or_404(queryset,pk=pk)
        
        serializer = self.serializer_class(booking,context = {'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
        