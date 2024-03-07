from django.urls import path, include
from .views import ServerUpView, AdvertisementView, AdvertisementDetailView

urlpatterns = [
    path('', ServerUpView.as_view()),
    path('adv/', AdvertisementView.as_view()),
    path('adv/<int:id>/', AdvertisementDetailView.as_view()),
    path('api/', include('limonapp.api.urls'))
]
