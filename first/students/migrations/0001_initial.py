# Generated by Django 3.2 on 2021-06-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('school', models.TextField(blank=True, null=True)),
                ('course', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
