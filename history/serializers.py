from rest_framework import serializers
from .models import EmailHistory
from email_service.models import SenderEmail


class SenderEmailNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SenderEmail
        fields = ('id', 'email_address')


class EmailHistorySerializer(serializers.ModelSerializer):
    sender = SenderEmailNestedSerializer(read_only=True)

    class Meta:
        model = EmailHistory
        fields = "__all__"

        read_only_fields = (
            "status",
            "retry_count",
            "sent_at",
            "sender"
        )