# Generated by Django 3.0.5 on 2020-05-13 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_studymat_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='studymat',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Module'),
        ),
    ]