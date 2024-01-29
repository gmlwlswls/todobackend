# Generated by Django 5.0.1 on 2024-01-29 05:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("userid", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=100)),
                ("done", models.BooleanField(default=False)),
                ("regdate", models.DateTimeField(auto_now_add=True)),
                ("moddate", models.DateTimeField(null=True)),
            ],
        ),
    ]
