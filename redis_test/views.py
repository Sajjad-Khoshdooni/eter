from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

# For cache timeout
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class RedisTestView(APIView):

    @method_decorator(vary_on_cookie)
    @method_decorator(cache_page(60 * 60))
    def get(self, request):
        
        if 'name1' in cache:
            name = cache.get('name1')

            print('from cache')
            
            return Response(name, 201)

        else:
            result = {
                "name1": "sajad"
            }
            cache.set('name1', result, CACHE_TTL)

            print('from View API')
            return Response(result, 201)