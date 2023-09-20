# Generated by Django 4.2.2 on 2023-09-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_delete_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
