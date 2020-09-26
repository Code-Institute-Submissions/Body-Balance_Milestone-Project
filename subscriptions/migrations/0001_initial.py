# Generated by Django 3.1.1 on 2020-09-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_duration', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]