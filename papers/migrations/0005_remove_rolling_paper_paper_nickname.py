# Generated by Django 4.2.7 on 2023-11-23 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0004_rolling_paper_paper_nickname'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='rolling_paper',
            name='paper_nickname',
        ),
    ]
