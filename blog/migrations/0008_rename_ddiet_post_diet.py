# Generated by Django 4.2.16 on 2024-10-31 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_diet_post_ddiet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ddiet',
            new_name='diet',
        ),
    ]