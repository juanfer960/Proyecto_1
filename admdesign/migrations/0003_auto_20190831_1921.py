# Generated by Django 2.2.4 on 2019-08-31 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admdesign', '0002_auto_20190827_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdesigns',
            name='prjdsg_status',
            field=models.CharField(choices=[('D', 'Disponible'), ('P', 'En proceso')], max_length=20, verbose_name='Estado'),
        ),
    ]
