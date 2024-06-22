# Generated by Django 5.0.6 on 2024-06-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_userprogress_completed_at_and_more'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='departments', to='courses.course'),
        ),
    ]