from rest_framework.response import Response
from rest_framework import status, generics
from django.db.models import Avg
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .models import  Service, Feedback
from .serializers import ServiceSerializer, FeedbackSerializer
from django.forms.models import model_to_dict



class ListAllServices(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class CreateSingleService(CreateAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class RetrieveSingleService(RetrieveAPIView):
    serializer_class = ServiceSerializer
    lookup_field='id'
    def get_queryset(self):
        service_id = self.kwargs['id']
        return Service.objects.filter(id=service_id)
"""

class RetrieveSingleService(generics.GenericAPIView):
    # To do: Use serializer_context attributes for cleaner code?
    serializer_class = ServiceSerializer
    def get(self, request, *args, **kwargs):
        #print(self.kwargs['id'])
        service_id = self.kwargs['id']
        service = Service.objects.get(id=service_id)
        #print(service)
        serializer = ServiceSerializer(instance=service)
        #print(serializer)
        #feedbacks = serializer.get_fields()['service_feedbacks']
        feedbacks = serializer.get_service_feedbacks(serializer)
        print(feedbacks)
        #print(feedbacks.all())
        #average_star_rating = feedbacks.aggregate(Avg('star_rating'))['star_rating__avg']
        #print(serializer.get_fields()['service_feedbacks'])
        #for feedback in feedbacks:
        #    print(feedback)
        #print(average_star_rating)
        #print(serializer.get('service_feedbacks'))
        #service_id = self.kwargs['id']
        #service = Service.objects.get(id=service_id)
        #feedbacks = Feedback.objects.filter(service=service_id)
        #average_star_rating = feedbacks.aggregate(Avg('star_rating'))['star_rating__avg']

        #convert feedbacks to list to send in Response
        #list_feedbacks = []
        #for item in feedbacks:
        #    list_feedbacks.append(model_to_dict(item))

        return Response({"data": {"service": serializer.data,
                                  "feedbacks":feedbacks}},
                        status=status.HTTP_201_CREATED)

"""
"""

class RetrieveSingleService(generics.GenericAPIView):
    # To do: Use serializer_context attributes for cleaner code?
    serializer_class = ServiceSerializer
    def get(self, request, *args, **kwargs):
        service_id = self.kwargs['id']
        service = Service.objects.get(id=service_id)
        feedbacks = Feedback.objects.filter(service=service_id)
        average_star_rating = feedbacks.aggregate(Avg('star_rating'))['star_rating__avg']

        #convert feedbacks to list to send in Response
        list_feedbacks = []
        for item in feedbacks:
            list_feedbacks.append(model_to_dict(item))

        return Response({"data": {"service": model_to_dict(service),
                                  "feedbacks": list_feedbacks,
                                  "average_star_rating": average_star_rating}},
                        status=status.HTTP_201_CREATED)
"""
class DeleteSingleService(DestroyAPIView):
    # Best practice would be to have some auth here, like
    # only the author can delete a Service, we will skip it for now
    #  permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class UpdateSingleService(UpdateAPIView):
    # Best practice would be to have some auth here, like
    # only the author can update a Service, we will skip it for now
    #  permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ListAllFeedbacks(ListAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

class CreateSingleFeedback(CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class RetrieveSingleFeedback(RetrieveAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class DeleteSingleFeedback(DestroyAPIView):
    # Best practice would be to have some auth here, like
    # only the author can delete a Feedback but we will skip it for now
    #  permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class UpdateSingleFeedback(UpdateAPIView):
    # Best practice would be to have some auth here, like
    # only the author can update a Feedback but we will skip it for now
    #  permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

