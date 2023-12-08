# Generated by Django 4.2.7 on 2023-12-02 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("document_type", models.CharField(max_length=100)),
                (
                    "file",
                    models.FileField(
                        upload_to="Users/jaideepreddyaluru/Documents/dest/"
                    ),
                ),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
