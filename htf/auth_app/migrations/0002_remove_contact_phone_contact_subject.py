# Generated by Django 4.2.9 on 2024-05-07 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="phone",
        ),
        migrations.AddField(
            model_name="contact",
            name="subject",
            field=models.TextField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
