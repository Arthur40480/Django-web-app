# Generated by Django 4.1.7 on 2023-03-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_announcement_description_announcement_sold_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
