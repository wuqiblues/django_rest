# Generated by Django 3.2 on 2022-05-15 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('describe', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('describe', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=30)),
                ('ip', models.GenericIPAddressField()),
                ('describe', models.TextField(blank=True, null=True)),
                ('app', models.ManyToManyField(to='myapp_api.App')),
            ],
        ),
        migrations.AddField(
            model_name='app',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp_api.project'),
        ),
    ]
