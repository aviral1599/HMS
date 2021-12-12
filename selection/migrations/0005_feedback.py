# Generated by Django 3.2.9 on 2021-12-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('happy', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]