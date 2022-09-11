
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserAccountSerializers
from rest_framework import status, viewsets
from django.db.models import ProtectedError
from django.http import JsonResponse
from .models import UserAccount
from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    #User.objects.filter(id__in=[1, 5, 34, 567, 229])
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializers
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'email']
    

    # def perform_destroy(self, instance):
    #     try:
    #         instance.delete()
    #     except ProtectedError:
    #         data = {'code': 'server_error',}
    #         JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)
            #messages.error(request, _('Cannot delete product'))


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })