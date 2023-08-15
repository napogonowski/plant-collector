from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name="detail"),
    path('plants/create', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('plants/<int:plant_id>/assoc_extra/<int:extra_id>/', views.assoc_extra, name='assoc_extra'),
    path('plants/<int:plant_id>/disassoc_extra/<int:extra_id>/', views.disassoc_extra, name='disassoc_extra'),
    path('extras/', views.ExtraList.as_view(), name='extras_index'),
    path('extras/<int:pk>/', views.ExtraDetail.as_view(), name='extras_detail'),
    path('extras/create/', views.ExtraCreate.as_view(), name='extras_create'),
    path('extras/<int:pk>/update/', views.ExtraUpdate.as_view(), name='extras_update'),
    path('extras/<int:pk>/delete/', views.ExtraDelete.as_view(), name='extras_delete'),
]
