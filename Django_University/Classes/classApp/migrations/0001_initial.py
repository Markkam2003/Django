# Generated by Django 4.0.4 on 2022-04-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('course_number', models.IntegerField()),
                ('instructor_name', models.CharField(max_length=50)),
                ('duration', models.FloatField(max_length=4)),
            ],
        ),
    ]
