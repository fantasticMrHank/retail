from rest_framework.decorators import api_view
from user_app.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user_app import models


@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.authtoken.delete()
        return Response({'message':"user logged out"})


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()

            token = Token.objects.get_or_create(user = account).key

            data['username'] = account.username
            data['email'] = account.email
            data['token'] = token

        else:
            data = serializer.errors

        return Response(data)
        