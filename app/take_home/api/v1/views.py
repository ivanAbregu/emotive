from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import MarsPhotoSerializer
import requests

from take_home.services.NasaApiConsumer import NasaApiConsumer

class MarsPhotoListAPIView(generics.ListAPIView):
    """
    Retrieve Mars photos for a specific Earth date.

    Parameters:
    - `earth_date` (str): The Earth date in the format 'YYYY-MM-DD'.

    Example:
    ```
    GET /api/mars-photos/2015-12-23/
    ```
    """
    serializer_class = MarsPhotoSerializer

    def list(self, request, *args, **kwargs):
        """
        List Mars photos for a specific Earth date.

        This endpoint retrieves photos from the NASA Mars Rover Photos API.

        Response:
        - 200 OK: Returns a list of Mars photos with details.
        - 400 Bad Request: If the request parameters are invalid.
        """
        nac = NasaApiConsumer()
        data = nac.get_data_by_date(self.kwargs['earth_date'])
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
