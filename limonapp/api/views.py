# from rest_framework import viewsets, status, generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from limonapp.models import Advertisement
# from .serializers import AdvertisementSerializer, UserSerializer
# import logging
#
# logger = logging.getLogger(__name__)
#
#
# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }, status=status.HTTP_201_CREATED)
#
#     logger.error(f"Error creating user: {serializer.errors}")
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AdvertisementViewSet(viewsets.ModelViewSet):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         logger.info(f"User {self.request.user} created advertisement: {serializer.validated_data}")
#         serializer.save()
#
#     def perform_update(self, serializer):
#         logger.info(f"User {self.request.user} updated advertisement: {serializer.validated_data}")
#         serializer.save()
#
#     def perform_destroy(self, instance):
#         logger.info(f"User {self.request.user} deleted advertisement: {instance}")
#         instance.delete()
#
#
# class AdvertisementAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_update(self, serializer):
#         logger.info(f"User {self.request.user} updated advertisement: {serializer.validated_data}")
#         serializer.save()
#
#
# class AdvertisementAPIDestroy(generics.RetrieveUpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_destroy(self, instance):
#         logger.info(f"User {self.request.user} deleted advertisement: {instance}")
#         instance.delete()
#
from django.http import JsonResponse
from rest_framework.decorators import action
import datetime
import logging
from rest_framework import viewsets, status, generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from limonapp.models import Advertisement
from .serializers import AdvertisementSerializer, UserSerializer

logger = logging.getLogger(__name__)


def created_at():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


@api_view(['POST'])
def create_user(request):
    try:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user = serializer.save()
        # refresh = RefreshToken.for_user(user)
        # return Response({
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token),
        # }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'User created successfully'
        })
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    #
    def perform_create(self, serializer):
        try:
            serializer.is_valid(raise_exception=True)
            logger.info(f"User {self.request.user} created advertisement: {serializer.validated_data}")
            serializer.save()
        except Exception as e:
            logger.error(f"Error creating advertisement: {e}")

    # def update(self, serializer):
    #     try:
    #         serializer.is_valid(raise_exception=True)
    #         logger.info(f"User {self.request.user} updated advertisement: {serializer.validated_data}")
    #         serializer.save()
    #     except Exception as e:
    #         logger.error(f"Error updating advertisement: {e}")
    #
    # def delete(self, instance):
    #     try:
    #         logger.info(f"User {self.request.user} deleted advertisement: {instance}")
    #         instance.delete()
    #     except Exception as e:
    #         logger.error(f"Error deleting advertisement: {e}")


# class AdvertisementAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_update(self, serializer):
#         try:
#             serializer.is_valid(raise_exception=True)
#             logger.info(f"User {self.request.user} updated advertisement: {serializer.validated_data}")
#             serializer.save()
#         except Exception as e:
#             logger.error(f"Error updating advertisement: {e}")
#
#
# class AdvertisementAPIDestroy(generics.RetrieveUpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_destroy(self, instance):
#         try:
#             logger.info(f"User {self.request.user} deleted advertisement: {instance}")
#             instance.delete()
#         except Exception as e:
#             logger.error(f"Error deleting advertisement: {e}")


# class AdvertisementViewSet(viewsets.ViewSet):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
# def perform_create(self, serializer):
#     try:
#         serializer.is_valid(raise_exception=True)
#         logger.info(f"User {self.request.user} created advertisement: {serializer.validated_data}")
#         serializer.save()
#     except Exception as e:
#         logger.error(f"Error creatingx` advertisement: {e}")

# @action(detail=True, methods=['update'])
# def perform_update(self, serializer, pk=None):
#     try:
#         serializer.is_valid(raise_exception=True)
#         logger.info(f"User {self.request.user} updated advertisement: {serializer.validated_data}")
#         serializer.save()
#     except Exception as e:
#         logger.error(f"Error updating advertisement: {e}")
#
# def perform_destroy(self, instance):
#     try:
#         logger.info(f"User {self.request.user} deleted advertisement: {instance}")
#         instance.delete()
#     except Exception as e:
#         logger.error(f"Error deleting advertisement: {e}")


# 3
#
# import logging
# import json
# from rest_framework import viewsets, status, generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from limonapp.models import Advertisement
# from .serializers import AdvertisementSerializer, UserSerializer
#
# logger = logging.getLogger(__name__)
#
#
# @api_view(['POST'])
# def create_user(request):
#     try:
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         response_data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
#         logger.info(json.dumps({
#             'message': 'User created',
#             'user_id': user.id,
#             'response_data': response_data
#         }))
#         return Response(response_data, status=status.HTTP_201_CREATED)
#     except Exception as e:
#         logger.error(json.dumps({
#             'message': 'Error creating user',
#             'error': str(e)
#         }))
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AdvertisementViewSet(viewsets.ModelViewSet):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         try:
#             serializer.is_valid(raise_exception=True)
#             logger.info(json.dumps({
#                 'message': 'Advertisement created',
#                 'user_id': self.request.user.id,
#                 'data': serializer.validated_data
#             }))
#             serializer.save()
#         except Exception as e:
#             logger.error(json.dumps({
#                 'message': 'Error creating advertisement',
#                 'error': str(e)
#             }))
#
#     def perform_update(self, serializer):
#         try:
#             serializer.is_valid(raise_exception=True)
#             logger.info(json.dumps({
#                 'message': 'Advertisement updated',
#                 'user_id': self.request.user.id,
#                 'data': serializer.validated_data
#             }))
#             serializer.save()
#         except Exception as e:
#             logger.error(json.dumps({
#                 'message': 'Error updating advertisement',
#                 'error': str(e)
#             }))
#
#     def perform_destroy(self, instance):
#         try:
#             logger.info(json.dumps({
#                 'message': 'Advertisement deleted',
#                 'user_id': self.request.user.id,
#                 'advertisement_id': instance.id
#             }))
#             instance.delete()
#         except Exception as e:
#             logger.error(json.dumps({
#                 'message': 'Error deleting advertisement',
#                 'error': str(e)
#             }))
#
#
# class AdvertisementAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_update(self, serializer):
#         try:
#             serializer.is_valid(raise_exception=True)
#             logger.info(json.dumps({
#                 'message': 'Advertisement updated',
#                 'user_id': self.request.user.id,
#                 'data': serializer.validated_data
#             }))
#             serializer.save()
#         except Exception as e:
#             logger.error(json.dumps({
#                 'message': 'Error updating advertisement',
#                 'error': str(e)
#             }))
#
#
# class AdvertisementAPIDestroy(generics.RetrieveUpdateAPIView):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_destroy(self, instance):
#         try:
#             logger.info(json.dumps({
#                 'message': 'Advertisement deleted',
#                 'user_id': self.request.user.id,
#                 'advertisement_id': instance.id
#             }))
#             instance.delete()
#         except Exception as e:
#             logger.error(json.dumps({
#                 'message': 'Error deleting advertisement',
#                 'error': str(e)
#             }))

def get_advertisement(request, pk):
    try:
        advertisement = Advertisement.objects.get(pk=pk)
        data = {
            'id': advertisement.pk,
            'title': advertisement.title,
            'description': advertisement.description,
            "price": advertisement.price,
            "subcategory": advertisement.subcategory,
            "condition": advertisement.condition,
            "attributes": advertisement.attributes,
            "images": advertisement.images
        }
        return JsonResponse(data)
    except Advertisement.DoesNotExist:
        return JsonResponse({'error': 'Advertisement not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


class AdvertisementAPIUpdate(generics.UpdateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({"message": "Advertisement successfully updated"})
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementAPIDestroy(generics.DestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            return Response({"message": "You have successfully deleted the ad"})
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
