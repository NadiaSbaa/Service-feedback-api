# Service Feedback API - Django Application

This Django-based API allows users to provide feedback on various services. 
It features two primary models: Service and Feedback.

## Key Features:

* **Service Model**:
  * **ID**: Unique identifier for each service.
  * **Name**: A descriptive title for the service.
  * **Description**: A brief overview of the service.
  * **Creation Date**: Automatically generated timestamp for when the service was added.
* **Feedback Model**:
  * Linked to a specific Service.
  * Includes both text feedback and a star rating (1-5 scale).

## API Functionalities:
This API simplifies the process of gathering and managing user feedback on different services, providing an average rating and comprehensive service details at a glance.

* **Services**:
  * Create, update, delete, and retrieve services.
  * When retrieving a service, all associated feedback is returned, along with the average star rating.

* **Feedback**:
  * Submit feedback for a specific service, modify or delete feedback, and view all feedback.


## Swagger documentation
Once you install swagger via the requirements, you can review the models / operations details via the Swagger interface.
- The documentations are found under the swagger-ui http://127.0.0.1:8000/services/swagger/ or the ReDoc view http://127.0.0.1:8000/services/redoc/

## Test 
For testing the API, you can simply run

```ruby
python manage.py test .
```

