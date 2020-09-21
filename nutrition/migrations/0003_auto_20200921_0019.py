# Generated by Django 3.1.1 on 2020-09-21 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_remove_nutrition_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrition',
            name='plan_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='day',
            field=models.DecimalField(decimal_places=0, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='week',
            field=models.DecimalField(decimal_places=0, max_digits=2, null=True),
        ),
    ]
