# Generated by Django 3.1.3 on 2020-11-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('likes', models.IntegerField()),
            ],
        ),
    ]
