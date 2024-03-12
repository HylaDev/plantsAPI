
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import mixins,generics,status

# Overview controller
@api_view(('GET',))
def Overview(request):
    """Returns all endpoints"""
    routes = [
        
    ]
   
    return Response(routes, status= status.HTTP_200_OK)