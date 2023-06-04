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

esp8266_ip = 'http://192.168.2.36'

def update_light_PN_ON(request):
    url = f'{esp8266_ip}/ledpn/on'
    response = requests.post(url)
    if response.status_code == 200:
        return HttpResponse('Bật đèn phòng ngủ thành công')
    else:
        return HttpResponse('Bật đèn phòng ngủ không thành công')


def update_light_PN_OFF(request):
    url = f'{esp8266_ip}/ledpn/off'
    response = requests.post(url)
    if response.status_code == 200:
        return HttpResponse('Tắt đèn phòng ngủ thành công')
    else:
        return HttpResponse('Tắt đèn phòng ngủ không thành công')


def update_light_PK_ON(request):
    url = f'{esp8266_ip}/ledpk/on'
    response = requests.post(url)
    if response.status_code == 200:
        return HttpResponse('Bật đèn phòng khách thành công')
    else:
        return HttpResponse('Bật đèn phòng khách không thành công')


def update_light_PK_OFF(request):
    url = f'{esp8266_ip}/ledpk/off'
    response = requests.post(url)
    if response.status_code == 200:
        return HttpResponse('Tắt đèn phòng ngủ thành công')
    else:
        return HttpResponse('Tắt đèn phòng ngủ không thành công')


def update_Door_ON(request):
    url = f'{esp8266_ip}/door/on'
    response = requests.post(url)
    if response.status_code == 200:
        return HttpResponse('Mở cửa thành công')
    else:
        return HttpResponse('Mở cửa không thành công')


def update_Door_OFF(request):
    url = f'{esp8266_ip}/door/off'
    response = requests.post(url)
    if response.status_code == 200:
        return HttpResponse('Đóng cửa thành công')
    else:
        return HttpResponse('Đóng cửa không thành công')
