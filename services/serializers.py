from rest_framework import serializers
from .models import Service, Feedback



class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id','service', 'content', 'star_rating')

class ServiceSerializer(serializers.ModelSerializer):
    service_feedbacks = FeedbackSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'creation_date','service_feedbacks')

    def create(self, validated_data):
        service_feedbacks = validated_data.pop('service_feedbacks')
        service_instance = Service.objects.create(**validated_data)
        for feedback in service_feedbacks:
            Feedback.objects.create(user=service_instance,**feedback)
        return service_instance
