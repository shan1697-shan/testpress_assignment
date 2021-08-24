# Generated by Django 3.2.6 on 2021-08-23 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolquiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=3000)),
                ('options', models.CharField(max_length=1500)),
                ('anstype', models.BooleanField(default=False)),
                ('relatedquiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz', to='schoolquiz.quiz')),
            ],
        ),
    ]
