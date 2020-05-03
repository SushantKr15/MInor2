# Generated by Django 2.2.3 on 2019-07-25 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizz', '0002_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instName', models.CharField(max_length=50)),
                ('stuName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dateofBirth', models.DateField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
