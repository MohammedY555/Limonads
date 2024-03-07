from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advertisement
from .serializers import AdvertisementSerializer


class ServerUpView(APIView):
    def get(self, request):
        data = {'message': 'Server is up and running'}
        return Response(data)


class AdvertisementView(generics.ListAPIView):
    queryset = Advertisement.objects.filter(is_deleted=False)
    serializer_class = AdvertisementSerializer


class AdvertisementDetailView(APIView):
    def get(self, request, id):
        try:
            advertisement = Advertisement.objects.get(id=id, is_deleted=False)
            serializer = AdvertisementSerializer(advertisement)
            return Response(serializer.data)
        except Advertisement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
