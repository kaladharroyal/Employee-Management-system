# Generated migration to create SenderEmail model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_service', '0003_seed_default_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='SenderEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Sender Emails',
            },
        ),
    ]
