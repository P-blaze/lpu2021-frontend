# Generated by Django 3.2.7 on 2021-09-29 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.CharField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('symbol', models.CharField(max_length=50)),
            ],
        ),
    ]
