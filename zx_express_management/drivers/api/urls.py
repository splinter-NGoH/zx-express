from django.urls import path
from .views import CreateDriver


urlpatterns = [
    path(
        "createdriverget/",
        CreateDriver.as_view(
            {
                "get": "list",
            }
        ),
        name="create",
    ),
    path(
        "createdriver/",
        CreateDriver.as_view(
            {
                "post": "create",
            }
        ),
        name="createdriver",
    ),
    path(
        "createdriverretrieve/<int:pk>/",
        CreateDriver.as_view(
            {
                "get": "retrieve",
            }
        ),
        name="retrieve",
    ),
]
