# Generated by Django 3.2.6 on 2021-08-24 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolquiz', '0004_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='schoolquiz.user'),
            preserve_default=False,
        ),
    ]
