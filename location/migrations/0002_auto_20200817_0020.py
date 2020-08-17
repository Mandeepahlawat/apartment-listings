# Generated by Django 2.2.14 on 2020-08-17 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('state', 'name')},
        ),
    ]