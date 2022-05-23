from django.urls import path
from redis_test.views import RedisTestView

urlpatterns = [
    path("", RedisTestView.as_view())
]