# Generated by Django 4.1.5 on 2023-01-16 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_moviedialogue_castid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedialogue',
            name='castid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.moviedesc'),
        ),
    ]
