# Generated by Django 4.0 on 2022-03-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languagename', models.CharField(max_length=20)),
                ('procent', models.IntegerField()),
            ],
        ),
    ]