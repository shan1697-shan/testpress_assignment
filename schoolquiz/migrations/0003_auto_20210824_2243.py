# Generated by Django 3.2.6 on 2021-08-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolquiz', '0002_questions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='options',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='anstype',
        ),
        migrations.AddField(
            model_name='questions',
            name='option1',
            field=models.CharField(default=0, max_length=1500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='option2',
            field=models.CharField(default=0, max_length=1500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='option3',
            field=models.CharField(default=0, max_length=1500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='option4',
            field=models.CharField(default=0, max_length=1500),
            preserve_default=False,
        ),
    ]