from django.urls import path
from additional import views
urlpatterns = [
    #hw6
    path("entity",views.sendAll, name='all_messages'),
    path("entity/<str:id>/",views.sendOne, name='id_message'),
    path("Postentity/",views.postNew, name='post'),
    path("DeleteEntity/<str:id>",views.Delete, name='delete'),
    path("image", views.sendImg),

    #hw7
    path('set_cookie/<str:title>/<str:value>', views.set_cookie),
    path('get_cookie/<str:title>/', views.get_cookie),
    path('set_header/<str:header_name>/<str:header_value>', views.set_Header),
    path('get_header/<str:header_name>/', views.get_Header),

    ]