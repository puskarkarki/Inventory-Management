# Generated by Django 3.2.5 on 2021-07-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_auto_20210726_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='issue_to',
            field=models.CharField(blank=True, max_length=51, null=True, verbose_name='Issue to'),
        ),
    ]
