from rest_framework.views import APIView
from rest_framework.response import Response


class View(APIView):

    def get(self, request):
        assert request.user.is_authenticated and request.user.username == 'admin'
        return Response({})
