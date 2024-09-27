from django.test import TestCase
from ..models import Service, Feedback


class TestService(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name", description="Test service description")

    def test_model_content(self):
        self.assertEqual(self.service.name, "Test service name")


class TestFeedback(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = Service.objects.create(name="Test service name", description="Test service description")
        cls.feedback = Feedback.objects.create(content="Awesome test feedback", star_rating=5, service=cls.service)

    def test_model_content(self):
        self.assertEqual(self.feedback.content, "Awesome test feedback")
        self.assertEqual(self.feedback.service.name, "Test service name")
