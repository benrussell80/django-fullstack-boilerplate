# Generated by Django 3.0.6 on 2020-05-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200511_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(editable=False, max_length=200),
        ),
    ]
