# Generated by Django 5.1.2 on 2024-11-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cover', '0002_rename_corusename_coverpage_coruse_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverpage',
            name='session',
            field=models.CharField(default='DefaultSession', max_length=50),
        ),
        migrations.AlterField(
            model_name='coverpage',
            name='uniName',
            field=models.CharField(max_length=200),
        ),
    ]