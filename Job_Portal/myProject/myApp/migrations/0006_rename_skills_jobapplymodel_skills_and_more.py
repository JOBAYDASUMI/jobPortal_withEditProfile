# Generated by Django 5.0.1 on 2024-10-29 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_remove_jobmodel_skill_jobmodel_skills_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplymodel',
            old_name='Skills',
            new_name='skills',
        ),
        migrations.RenameField(
            model_name='jobmodel',
            old_name='Skills',
            new_name='skills',
        ),
        migrations.RenameField(
            model_name='seekerprofilemodel',
            old_name='Skills',
            new_name='skills',
        ),
    ]
