# Generated migration to add sender field to EmailHistory

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_service', '0005_emaillog_sender'),
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailhistory',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='email_history', to='email_service.senderemail'),
        ),
    ]
