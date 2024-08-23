import os

from django.conf import settings
from google.cloud import storage
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response

import logging

from core.models import User

logger = logging.getLogger(__name__)


class RegisterUserAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_obj = request.FILES['profile_picture']

        # Create a Google Cloud Storage client
        client = storage.Client(credentials=settings.GS_CREDENTIALS, project=settings.GS_PROJECT_ID)
        bucket = client.get_bucket(settings.GS_BUCKET_NAME)

        # Upload the file to GCS
        file_path = os.path.join('profile_pics', file_obj.name)
        blob = bucket.blob(file_path)
        blob.upload_from_file(file_obj, content_type=file_obj.content_type, num_retries=5)

        file_url = blob.public_url

        user = User.objects.create_user(username=request.data['username'], email=request.data['email'], profile_picture=file_url)
        user.save()

        user.set_password(request.data['password'])
        user.save()

        return Response({"message": "File uploaded successfully"}, status=status.HTTP_201_CREATED)