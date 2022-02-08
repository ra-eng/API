# Generated by Django 4.0.1 on 2022-01-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0002_alter_scoring_employerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('includeAt', models.DateTimeField()),
                ('employeedId', models.CharField(max_length=10)),
                ('employerId', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Scoring',
        ),
    ]