# Generated by Django 4.1.5 on 2023-01-16 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_alter_moviedialogue_castid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedialogue',
            old_name='castid',
            new_name='castnameid',
        ),
    ]
