# Generated by Django 5.0.1 on 2024-10-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_remove_seekerprofilemodel_skills_customuser_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]