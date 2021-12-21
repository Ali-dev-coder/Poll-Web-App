# Generated by Django 3.2.5 on 2021-12-12 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll_app', '0002_alter_pollmodel_poll_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollmodel',
            name='poll_option_one',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pollmodel',
            name='poll_option_one_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pollmodel',
            name='poll_option_three',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pollmodel',
            name='poll_option_three_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pollmodel',
            name='poll_option_two',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pollmodel',
            name='poll_option_two_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pollmodel',
            name='poll_question',
            field=models.TextField(),
        ),
    ]