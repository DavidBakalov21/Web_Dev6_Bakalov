from django.urls import path
from hw8 import views
urlpatterns = [
path('viewAll', views.display, name='all_users'),
path('addForm', views.AddForm, name='add_user'),
path('addUser/', views.postNew),
path('user/<str:id>/', views.showById, name='profile'),
path("delete/", views.Delete),
path("updateForm/<str:id>", views.UpdateForm, name="update"),
path("updateForm/updateUser/", views.Update_User),
path("PatchForm/<str:id>", views.Patch_Form, name="Patch"),
path("PatchForm/PatchUser/", views.Patch_User),
    path("info", views.Info, name="Infohw8")
    ]