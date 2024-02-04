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
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    ]