from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = {
        'users': '/api/users',
        'posts/':'/api/posts'
    }
    return Response()