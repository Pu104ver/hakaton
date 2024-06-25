# Generated by Django 5.0.6 on 2024-06-13 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_created_by_course_is_free_course_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprogress',
            options={'verbose_name_plural': 'User Progress'},
        ),
        migrations.RemoveField(
            model_name='userprogress',
            name='completed_at',
        ),
        migrations.AddField(
            model_name='userprogress',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]