# Generated by Django 4.2.1 on 2023-05-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_seatmetrixdb_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seatmetrixdb',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
