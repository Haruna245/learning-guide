# Generated by Django 4.0.3 on 2023-05-20 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnApp', '0003_materials_subject_alter_materials_time_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materials',
            old_name='subject',
            new_name='title',
        ),
    ]
