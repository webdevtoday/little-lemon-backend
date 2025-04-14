from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from . import serializers, models


# Create your views here.
def sayHello(request):
    return HttpResponse("Hello World")


def index(request):
    return render(request, "index.html", {})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
    # queryset = models.Menu.objects.all()
    # serializer_class = serializers.MenuSerializer
    permission_classes = [IsAuthenticated]
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = models.Menu.objects.all()
    # serializer_class = serializers.MenuSerializer
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})
