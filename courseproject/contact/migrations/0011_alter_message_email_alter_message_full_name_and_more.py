# Generated by Django 4.2.2 on 2023-09-20 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_alter_message_email_alter_message_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
