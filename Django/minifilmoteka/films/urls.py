from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'films', views.FilmViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('films/view/', views.film_list_view, name='film-list-view'),
    path('films/<int:pk>/view/', views.film_detail_view, name='film-detail-view'),
    path('test-serialization/', views.test_serialization, name='test-serialization'),
    path('test-serialization-view/', views.test_serialization_view, name='test-serialization-view'),
]