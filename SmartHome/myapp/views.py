from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import ItemSerializer, ArduinoDataSerialezer
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import serial
import time


# Create your views here.
from rest_framework import generics
ser = serial.Serial('COM4', 9600)


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ArduinoDataList(generics.ListCreateAPIView):
    queryset = ArduinoData.objects.all()
    serializer_class = ArduinoDataSerialezer


class ArduinoDataDetail(generics.RetrieveUpdateAPIView):
    queryset = ArduinoData.objects.all()
    serializer_class = ArduinoDataSerialezer


def update_light_PN_ON(request):
    # Lấy trạng thái bật đèn từ cơ sở dữ liệu
    obj = Item.objects.get(pk=1)
    obj.status = True
    obj.save()
    # Gửi yêu cầu điều khiển đèn tới Arduino
    # arduino_port = get_arduino_port()
    data = '1'
    ser.write(data.encode())
    return HttpResponse('Light PN On successfully!')


def update_light_PN_OFF(request):
    # Lấy trạng thái bật đèn từ cơ sở dữ liệu
    obj = Item.objects.get(pk=1)
    obj.status = False
    obj.save()
    # Gửi yêu cầu điều khiển đèn tới Arduino
    # arduino_port = get_arduino_port()
    data = '0'
    ser.write(data.encode())
    return HttpResponse('Light PN OFF successfully!')


def update_light_PK_ON(request):
    # Lấy trạng thái bật đèn từ cơ sở dữ liệu
    obj = Item.objects.get(pk=5)
    obj.status = True
    obj.save()
    # Gửi yêu cầu điều khiển đèn tới Arduino
    # arduino_port = get_arduino_port()
    data = '3'
    ser.write(data.encode())
    return HttpResponse('Light PK On successfully!')


def update_light_PK_OFF(request):
    obj = Item.objects.get(pk=5)
    obj.status = False
    obj.save()
    # Gửi yêu cầu điều khiển đèn tới Arduino
    # arduino_port = get_arduino_port()
    data = '2'
    ser.write(data.encode())
    return HttpResponse('Light PK OFF successfully!')


def update_Door_ON(request):
    # Cập nhật trạng thái Bật đèn từ cơ sở dữ liệu

    obj = Item.objects.get(pk=4)
    obj.status = True
    obj.save()
    # Gửi yêu cầu điều khiển đèn tới Arduino
    # arduino_port = get_arduino_port()
    data = '4'
    ser.write(data.encode())
    return HttpResponse('Door ON successfully!')


def update_Door_OFF(request):
    # Cập nhật trạng thái tắt đèn từ cơ sở dữ liệu
    obj = Item.objects.get(pk=4)
    obj.status = False
    obj.save()
    data = '5'
    ser.write(data.encode())
    return HttpResponse('Door OFF successfully!')

