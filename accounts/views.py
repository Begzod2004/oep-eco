from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, VerifySerializer, LoginSerializer
from .utils import send_sms
import random

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        verification_code = '{:04d}'.format(random.randint(0, 9999))
        user.verification_code = verification_code
        user.is_active = False
        user.save()
        message = f"Siz O'EP a'zosi bo'ldingiz. Tasdiqlash kodingiz: {verification_code}"
        send_sms(user.phone_number, message)
        return Response({"message": "Verification code sent"}, status=status.HTTP_201_CREATED)

class VerifyView(generics.GenericAPIView):
    serializer_class = VerifySerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        code = serializer.validated_data['code']
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.verification_code == code:
                user.is_active = True
                user.verification_code = None
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                return Response({"message": "Phone number verified", "token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        password = serializer.validated_data['password']
        user = authenticate(phone_number=phone_number, password=password)
        if user is not None:
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "User is not active"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
