# Generated by Django 3.0.1 on 2020-01-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCBuilder', '0006_auto_20200107_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalproduct',
            name='category',
            field=models.CharField(default='Gaming', max_length=256, verbose_name='Category'),
        ),
    ]
