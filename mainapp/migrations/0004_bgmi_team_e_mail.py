# Generated by Django 4.2.10 on 2024-10-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_rename_team_bgmi_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgmi_team',
            name='e_mail',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
