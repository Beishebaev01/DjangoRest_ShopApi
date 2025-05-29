from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.serializers import UserCreateSerializer, UserAuthSerializer, CodeConfirmSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import VerificationCode


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
# @api_view(['POST'])
# def authorization_api_view(request):
#     serializer = UserAuthSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(**serializer.validated_data)
#     if user:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response(data={'key': token.key})
#     return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = User.objects.create_user(username=username,
                                        password=password,
                                        is_active=False)

        code = VerificationCode.objects.create(user=user)

        return Response(status=status.HTTP_201_CREATED,
                        data={
                            'user_id': user.id,
                            'verification_code': code.code
                        })
# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data['username']
#     password = serializer.validated_data['password']
#
#     user = User.objects.create_user(username=username,
#                                     password=password,
#                                     is_active=False)
#
#     code = VerificationCode.objects.create(user=user)
#
#     return Response(status=status.HTTP_201_CREATED,
#                     data={
#                         'user_id': user.id,
#                         'verification_code': code.code
#                     })

class ConfirmAPIView(APIView):
    def post(self, request):
        serializer = CodeConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(username=serializer.validated_data['username'])
        code_obj = user.verification_code

        user.is_active = True
        user.save()

        code_obj.is_verified = True
        code_obj.save()

        return Response({'message': 'Пользователь активирован'}, status=200)
# @api_view(['POST'])
# def confirm_code_api_view(request):
#     serializer = CodeConfirmSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     user = User.objects.get(username=serializer.validated_data['username'])
#     code_obj = user.verification_code
#
#     user.is_active = True
#     user.save()
#
#     code_obj.is_verified = True
#     code_obj.save()
#
#     return Response({'message': 'Пользователь активирован'}, status=200)