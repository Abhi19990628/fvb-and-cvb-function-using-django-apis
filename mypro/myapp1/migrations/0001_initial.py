# Generated by Django 5.0.6 on 2024-05-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grandfather', models.CharField(max_length=20)),
                ('grandmother', models.CharField(max_length=20)),
                ('father', models.CharField(max_length=20)),
                ('mother', models.CharField(max_length=20)),
                ('brother', models.CharField(max_length=20)),
                ('sister', models.CharField(max_length=20)),
                ('family_member', models.CharField(max_length=10)),
            ],
        ),
    ]