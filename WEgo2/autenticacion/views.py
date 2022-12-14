from django.shortcuts import render

# imports rest_ framework
from django.contrib.auth import authenticate, login, logout
from rest_framework import status , generics
from rest_framework.response import Response
from rest_framework.views import APIView



#import serializer
from .serializer import UserSerializer

# VIEWS API
class LoginView (APIView):
    
    def post (self,request):
        #Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get ('email',None)
        password = request.data.get ('password',None)
        user = authenticate (email=email,password=password)
        
        
        #si es correcto añadimos a la request la informacion de sesion
        if user:
            login(request,user)
            return Response (
                UserSerializer(user).data ,
                status = status.HTTP_200_OK
            )
        
        #Si no es correcto devolvemos un error en la peticion
        return Response (
            status = status.HTTP_404_NOT_FOUND
        )
        
class LogoutView (APIView):
    def post (self,request):
        #Borramos de la request la informacion de sesion
        logout(request)
    
        #devolvemos la respuesta al cliente
        return Response (status = status.HTTP_200_OK)
    
    
class SignupView (generics.CreateAPIView):
    serializer_class = UserSerializer