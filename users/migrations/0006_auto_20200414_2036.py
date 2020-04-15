# Generated by Django 3.0.5 on 2020-04-14 20:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200414_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='internships',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=100), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=100), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projects',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=2), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, null=True, size=None),
        ),
    ]