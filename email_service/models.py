from django.db import models
from employee.models import Employee


class SenderEmail(models.Model):
    """
    Store multiple sender email addresses with their credentials
    """
    email_address = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # App password for Gmail
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Sender Emails"

    def __str__(self):
        return f"{self.email_address} ({'Active' if self.is_active else 'Inactive'})"


class EmailLog(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Sending', 'Sending'),
        ('Sent', 'Sent'),
        ('Failed', 'Failed'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='emails'
    )

    sender = models.ForeignKey(
        SenderEmail,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sent_emails'
    )

    recipient_email = models.EmailField()

    subject = models.CharField(max_length=255)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    retry_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class EmailTemplate(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title