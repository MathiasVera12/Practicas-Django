# Generated by Django 5.2.1 on 2025-05-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0003_rename_notedescription_note_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.CharField(max_length=50),
        ),
    ]
