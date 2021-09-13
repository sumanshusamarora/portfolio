from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class APIHealth(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        return Response(status=status.HTTP_200_OK)