# Generated by Django 4.2.7 on 2023-11-23 06:57

from django.db import migrations, models
import django.db.models.constraints


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_alter_rolling_paper_nickname'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='rolling_paper',
            constraint=models.UniqueConstraint(deferrable=django.db.models.constraints.Deferrable['IMMEDIATE'], fields=('nickname',), name='paper_nickname'),
        ),
    ]
