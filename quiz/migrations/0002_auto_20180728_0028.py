# Generated by Django 2.0.1 on 2018-07-27 18:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='correct_answer',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Correct Answers'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='progress',
            name='wrong_answer',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Wrong Answers'),
            preserve_default=False,
        ),
    ]
