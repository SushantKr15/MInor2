# Generated by Django 2.2.3 on 2019-07-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0008_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='quizName',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]