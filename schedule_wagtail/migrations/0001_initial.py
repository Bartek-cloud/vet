# Generated by Django 3.2.18 on 2023-03-20 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyCalendarandHour',
            fields=[
                ('formpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='website.formpage')),
            ],
            options={
                'verbose_name': 'calendar',
            },
            bases=('website.formpage',),
        ),
    ]
