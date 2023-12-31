# Generated by Django 4.0.3 on 2023-05-16 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learnApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materials', models.FileField(null=True, upload_to='')),
                ('description', models.TextField(null=True)),
                ('time_added', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
