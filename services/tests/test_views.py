from django.test import TestCase
from services.models import Service, Feedback
from rest_framework import status


class ListAllServicesViewTest(TestCase):
    def test_list_services(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateSingleServiceViewTest(TestCase):
    def test_create_single_service(self):
        response = self.client.post("/services/create/",
                                    {"name": "Test service name",
                                     "description": "Test service description"},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class RetrieveSingleServiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name",description="Test service description")

    def test_retrive_single_service(self):
        response = self.client.get('/services/'+str(self.service.id)+"/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UpdateSingleServiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name",description="Test service description")

    def test_update_single_service(self):
        response = self.client.patch('/services/'+str(self.service.id)+'/update/',
                                    {"name":"Awesome test feedback updated"},
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteSingleServiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name",description="Test service description")

    def test_delete_single_service(self):
        response = self.client.delete('/services/'+str(self.service.id)+'/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
class ListAllFeedbacksViewTest(TestCase):
    def test_list_feedbacks(self):
        response = self.client.get('/services/feedbacks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CreateSingleFeedbackViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name", description="Test service description")
    def test_create_single_feedback(self):
        response = self.client.post("/services/feedbacks/create/",
                                    {"content":"Awesome test feedback",
                                     "star_rating":5,
                                     "service":str(self.service.id)},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class RetrieveSingleFeedbackViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name", description="Test service description")
        cls.feedback = Feedback.objects.create(content="Awesome test feedback", star_rating=5, service=cls.service)

    def test_retrieve_single_feedback(self):
        response = self.client.get('/services/feedbacks/'+str(self.feedback.id)+'/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UpdateSingleFeedbackViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name",description="Test service description")
        cls.feedback = Feedback.objects.create(content="Awesome test feedback", star_rating=5, service=cls.service)

    def test_update_single_feedback(self):
        response = self.client.patch('/services/feedbacks/'+str(self.feedback.id)+'/update/',
                                     {"content":"Awesome test feedback updated"},
                                     content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteSingleFeedbackViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name",description="Test service description")
        cls.feedback = Feedback.objects.create(content="Awesome test feedback", star_rating=5, service=cls.service)

    def test_delete_single_feedback(self):
        response = self.client.delete('/services/feedbacks/'+str(self.feedback.id)+'/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)