# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import AdvertisementViewSet, AdvertisementAPIUpdate
#
# router = DefaultRouter()
# router.register(r'adv', AdvertisementViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('adv/<int:pk>/', AdvertisementAPIUpdate.as_view())
# ]

from django.urls import path
from .views import AdvertisementViewSet, AdvertisementAPIUpdate, AdvertisementAPIDestroy, get_advertisement

urlpatterns = [
    path('adv/', AdvertisementViewSet.as_view({'get': 'list', 'post': 'create'}), name='advertisement-list'),
    path('adv/<int:pk>/', get_advertisement, name='advertisement-detail'),
    path('adv/<int:pk>/', AdvertisementAPIUpdate.as_view(), name='advertisement-update'),
    path('adv/<int:pk>/delete/', AdvertisementAPIDestroy.as_view(), name='advertisement-delete'),
]
