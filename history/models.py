from django.db import models
from employee.models import Employee
from email_service.models import SenderEmail


class EmailHistory(models.Model):

    STATUS_CHOICES = [
        ('Sent', 'Sent'),
        ('Failed', 'Failed'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    sender = models.ForeignKey(
        SenderEmail,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='email_history'
    )

    recipient_email = models.EmailField()

    subject = models.CharField(max_length=255)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    retry_count = models.IntegerField(default=0)

    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee} - {self.subject}"