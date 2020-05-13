# Generated by Django 3.0.5 on 2020-05-13 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(default=' ', max_length=50)),
                ('courseDesc', models.TextField(default=' ')),
                ('courseImage', models.ImageField(default=' ', upload_to='pics2/')),
                ('price', models.IntegerField(default='100')),
                ('bought', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleName', models.CharField(default=' ', max_length=50)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Course')),
            ],
        ),
        migrations.CreateModel(
            name='studyMat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default=' ', max_length=50)),
                ('typ', models.CharField(choices=[('video', 'video'), ('pdf', 'pdf'), ('doc', 'doc')], default='video', max_length=6)),
                ('file1', models.FileField(default=' ', upload_to='files12/')),
                ('module', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Module')),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizName', models.CharField(default=' ', max_length=50)),
                ('module', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Module')),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(default=' ', max_length=100)),
                ('option1', models.CharField(default=' ', max_length=50)),
                ('option2', models.CharField(default=' ', max_length=50)),
                ('option3', models.CharField(default=' ', max_length=50)),
                ('option4', models.CharField(default=' ', max_length=50)),
                ('correctoption', models.CharField(choices=[('option1', 'option1'), ('option2', 'option2'), ('option3', 'option3'), ('option4', 'option4')], default=models.CharField(default=' ', max_length=50), max_length=50)),
                ('quizName', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.quiz')),
            ],
        ),
    ]
