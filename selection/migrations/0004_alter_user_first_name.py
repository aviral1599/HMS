# Generated by Django 3.2.9 on 2021-12-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_student_no_dues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
