# Generated by Django 5.0.6 on 2024-05-28 00:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240521_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='kicked_until',
            field=models.DateField(blank=True, null=True, verbose_name='kicked until'),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Report Content')),
                ('reviewed', models.BooleanField(blank=True, default=False, verbose_name='Is reviewed')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='made_reports', to=settings.AUTH_USER_MODEL, verbose_name='Report by')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL, verbose_name='Report of')),
            ],
        ),
    ]
