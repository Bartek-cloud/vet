# Generated by Django 4.1.7 on 2023-05-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("veter", "0011_alter_calendarpageclient_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="dane"),
        ),
        migrations.AlterField(
            model_name="result",
            name="text",
            field=models.CharField(max_length=255, verbose_name="opis"),
        ),
        migrations.AlterField(
            model_name="treatment",
            name="date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="dane"),
        ),
        migrations.AlterField(
            model_name="treatment",
            name="text",
            field=models.CharField(max_length=255, verbose_name="opis"),
        ),
    ]