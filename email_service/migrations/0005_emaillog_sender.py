# Generated migration to add sender field to EmailLog

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_service', '0004_senderemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillog',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_emails', to='email_service.senderemail'),
        ),
    ]
