# Generated by Django 3.0.5 on 2020-05-13 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_studymat_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='studymat',
            name='typ',
            field=models.CharField(choices=[('video', 'video'), ('pdf', 'pdf'), ('doc', 'doc')], default='video', max_length=6),
        ),
    ]