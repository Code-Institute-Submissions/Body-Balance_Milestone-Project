# Generated by Django 3.1.1 on 2020-10-14 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='has_plan',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
