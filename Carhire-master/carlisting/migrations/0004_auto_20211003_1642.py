# Generated by Django 3.2.7 on 2021-10-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carlisting', '0003_carowner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carowner',
            old_name='image_one',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='information',
        ),
        migrations.RemoveField(
            model_name='carowner',
            name='last_name',
        ),
        migrations.AddField(
            model_name='carowner',
            name='owner_email',
            field=models.CharField(help_text=' Please enter your email', max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='carowner',
            name='owner_name',
            field=models.CharField(help_text='Please enter your full name', max_length=100, null=True, verbose_name='Full name'),
        ),
    ]
