from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from . models import Users
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .serializers import Contact_Serializer

from rest_framework.pagination import PageNumberPagination

"""
ResultsPagination class is basically used to provide pagination feature to a Viewset without and extra code
need to define some of the variables like "page_size","query_param"
"""
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5


class Contact(viewsets.ModelViewSet):
  """
  The view class which provides the crud operations, same as above class need to define few predefined variables
  """
  pagination_class = StandardResultsSetPagination
  queryset = Users.objects.all()
  permission_classes = (IsAuthenticated,)
  serializer_class = Contact_Serializer
  lookup_field = 'email'


#another type of delete where you delete it only by email
  @action(detail=True,methods=['delete'])
  def delete(self, request, email=None):
    print('lol')
    instance = get_object_or_404(Users,pk__icontains=email)
    serialised_data = {'email':instance.email}
    serialised_data['message']='successfully deleted above object'
    instance.delete()
    return Response(serialised_data)

#you can even fetch proper object using this url paths
  @action(detail=True,methods=['post'])
  def search(self,request,**kwargs):
      try:
          contact_obj = Users.objects.get(email__icontains=self.kwargs['email'])
          return Response(Contact_Serializer(contact_obj).data)

      except Users.DoesNotExist:
          return Response({'Error': 'Given email isn"t present in DB'})


#method to retrive objects based on either email/name provided in the same path attributes
  #send either name or username of email not both,
  # else send email in body
  def retrieve(self, request, *args, **kwargs):
    print(kwargs)
    try:
      contact_obj = Users.objects.get(email__icontains=self.kwargs['email'])
      return Response(Contact_Serializer(contact_obj).data)

    except Users.DoesNotExist:
        list_of_users = Users.objects.filter(name__iexact=self.kwargs['email'])
        if (len(list_of_users) == 0):
          return Response({'Error': 'Given name/email isn"t present in DB'})
        else:
          return Response([Contact_Serializer(user).data for user in list_of_users])


    except Exception as e:
      return Response({'Error': 'Possible error while fetching object using email. Exception cause: '+e.__class__.__name__})



