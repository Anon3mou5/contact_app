from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from . models import Users
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .serializers import Contact_Serializer

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5

class Contact(viewsets.ModelViewSet):
  pagination_class = StandardResultsSetPagination
  queryset = Users.objects.all()
  permission_classes = (AllowAny,)
  serializer_class = Contact_Serializer
  lookup_field = 'email'

  @action(detail=True,methods=['delete'])
  def delete(self, request, email=None):
    print('lol')
    instance = get_object_or_404(Users,pk=email)
    serialised_data = {'email':instance.email}
    serialised_data['message']='successfully deleted above object'
    instance.delete()
    return Response(serialised_data)

  def retrieve(self, request, *args, **kwargs):
    print(kwargs['email'])
    try:
      contact_obj = Users.objects.get(email__iexact=self.kwargs['email'])
      return Response(Contact_Serializer(contact_obj).data)

    except Users.DoesNotExist:
        list_of_users = Users.objects.filter(name__iexact=self.kwargs['email'])
        if (len(list_of_users) == 0):
          return Response({'Error': 'Given name/email isn"t present in DB'})
        else:
          return Response([Contact_Serializer(user).data for user in list_of_users])


    except Exception as e:
      return Response({'Error': 'Possible error while fetching object using email. Exception cause: '+e.__class__.__name__})



