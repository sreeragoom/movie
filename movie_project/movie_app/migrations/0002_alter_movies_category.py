# Generated by Django 4.2.9 on 2024-02-06 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movies",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="movie_app.category",
            ),
        ),
    ]
