from django.urls import path, include
from .views import RetrieveSingleService, ListAllServices, CreateSingleService,DeleteSingleService, UpdateSingleService, \
    ListAllFeedbacks, RetrieveSingleFeedback,CreateSingleFeedback, DeleteSingleFeedback, UpdateSingleFeedback
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Services API",
        default_version='v1',
        description="The API enables the Creating, Modifying, Deleting, and Reading of Services and Feedbacks.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # List view (Read all) feedbacks
    path('feedbacks/', ListAllFeedbacks.as_view()),
    # Create view feedback
    path('feedbacks/create/', CreateSingleFeedback.as_view()),
    # Retrieve view (Read one) feedback
    path('feedbacks/<str:pk>/', RetrieveSingleFeedback.as_view()),
    # Update view feedback
    path('feedbacks/<str:pk>/update/', UpdateSingleFeedback.as_view()),
    # Delete view feedback
    path('feedbacks/<str:pk>/delete/', DeleteSingleFeedback.as_view()),
    # List services view (Read all)
    path('', ListAllServices.as_view()),
    # Create service view
    path('create/', CreateSingleService.as_view()),
    # Retrieve service view (Read one)
    path('<str:id>/', RetrieveSingleService.as_view()),
    # Update service view
    path('<str:pk>/update/', UpdateSingleService.as_view()),
    # Delete service view
    path('<str:pk>/delete/', DeleteSingleService.as_view()),
]