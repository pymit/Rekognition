# Generated by Django 2.2.1 on 2019-06-26 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapi', '0010_auto_20190626_0511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputvideo',
            old_name='is_processed',
            new_name='isProcessed',
        ),
    ]
