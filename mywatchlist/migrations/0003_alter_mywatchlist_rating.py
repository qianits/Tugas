# Generated by Django 4.1 on 2022-09-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_alter_mywatchlist_review_alter_mywatchlist_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.TextField(),
        ),
    ]
