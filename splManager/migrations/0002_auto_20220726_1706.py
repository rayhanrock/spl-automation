# Generated by Django 3.2.13 on 2022-07-26 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_is_active'),
        ('splManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spl',
            name='projects',
        ),
        migrations.AddField(
            model_name='project',
            name='spl_code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='splManager.team'),
        ),
        migrations.RemoveField(
            model_name='team',
            name='mentors',
        ),
        migrations.AddField(
            model_name='team',
            name='mentors',
            field=models.ManyToManyField(blank=True, null=True, related_name='team_mentors', to='users.Teacher'),
        ),
        migrations.RemoveField(
            model_name='team',
            name='students',
        ),
        migrations.AddField(
            model_name='team',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='team_students', to='users.Student'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('status', models.CharField(max_length=7)),
                ('priority', models.CharField(max_length=7)),
                ('assign', models.ManyToManyField(blank=True, null=True, related_name='task', to='users.Student')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splManager.project')),
            ],
        ),
    ]
