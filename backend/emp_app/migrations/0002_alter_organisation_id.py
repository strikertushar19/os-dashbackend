# Generated by Django 4.2.3 on 2023-08-24 20:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emp_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organisation",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
