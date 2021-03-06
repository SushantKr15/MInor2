# Generated by Django 3.0.5 on 2020-05-06 18:35

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
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('img', models.ImageField(default=' ', upload_to='pics')),
                ('desc', models.TextField(default=' ')),
                ('price', models.IntegerField(default='100')),
                ('bought', models.BooleanField(default=True)),
                ('destno', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('Name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dateofBirth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instName', models.CharField(max_length=50)),
                ('quizName', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
                ('correctAnswer', models.CharField(max_length=50)),
                ('totalPoints', models.CharField(max_length=50)),
                ('quizDate', models.DateField(max_length=50)),
                ('quizTime', models.CharField(max_length=50)),
                ('stuEmail', models.CharField(max_length=50)),
                ('totalQues', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ReadyQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instName', models.CharField(max_length=50)),
                ('quizName', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
                ('attempts', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stuName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dateofBirth', models.DateField()),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudyFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherEmail', models.CharField(max_length=50)),
                ('folderName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('teacher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizName', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=50)),
                ('ans1', models.CharField(max_length=50)),
                ('ans2', models.CharField(max_length=50)),
                ('ans3', models.CharField(max_length=50)),
                ('ans4', models.CharField(max_length=50)),
                ('correct', models.CharField(max_length=50)),
                ('points', models.IntegerField(default=1)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quizz.Module')),
            ],
        ),
    ]
