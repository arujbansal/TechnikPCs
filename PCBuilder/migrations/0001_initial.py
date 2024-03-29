# Generated by Django 3.0.1 on 2020-01-07 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=256, verbose_name='Company')),
                ('selection', models.TextField(verbose_name='Selection')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
        ),
        migrations.CreateModel(
            name='FinalProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_price', models.IntegerField(verbose_name='Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCBuilder.Category')),
                ('parts', models.ManyToManyField(to='PCBuilder.Part')),
            ],
        ),
    ]
