from django.db import models
import uuid


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "service"
        ordering = ['-creation_date']

        def __str__(self) -> str:
            return self.name



class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="feedback_on_service")
    content = models.TextField()
    star_rating = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "feedback"
        db_table_comment = "feedback services"

        def __str__(self) -> str:
            return self.content