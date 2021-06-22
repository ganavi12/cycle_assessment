import json
from datetime import datetime

from rest_framework import serializers
from rest_framework.request import Request
from datetime import datetime


class BaseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        """

        Args:
            instance:
            validated_data:

        Returns:

        """

    def create(self, validated_data):
        """

        Args:
            validated_data:

        Returns:

        """
        return validated_data


class PriceList(BaseSerializer):
    """
    Serializer for deleting uploaded files.
    """

    frame_type = serializers.CharField(required=True)
    handle_type = serializers.CharField(required=True)
    seat_type = serializers.CharField(required=True)
    wheel_type = serializers.CharField(required=False)

    def get_data(self, request: Request):
        """

        Args:
            request:

        Returns:

        """
        data = {
            "frame_type": request.data['frame_type'],
            "handle_type": request.data['handle_type'],
            "seat_type": request.data['seat_type'],
            "wheel_type": request.data['wheel_type'],
        }
        self.initial_data = data
