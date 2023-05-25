from django.urls import path
from .views import ItemList, ItemDetail, ArduinoDataList, ArduinoDataDetail, update_light_PN_ON, update_light_PN_OFF, update_light_PK_ON, update_light_PK_OFF, update_Door_ON, update_Door_OFF

urlpatterns = [
    path('items/', ItemList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
    path('datas/', ArduinoDataList.as_view()),
    path('datas/<int:pk>/', ArduinoDataDetail.as_view()),

    path('ledpn_on/', update_light_PN_ON, name='ledpn_on'),
    path('ledpn_off/', update_light_PN_OFF, name='ledpn_off'),
    path('ledpk_on/', update_light_PK_ON, name='ledpk_on'),
    path('ledpk_off/', update_light_PK_OFF, name='ledpk_off'),
    path('door_on/', update_Door_ON, name='door_on'),
    path('door_off/', update_Door_OFF, name='door_off'),
]
