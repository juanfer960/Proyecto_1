# Generated by Django 2.2.4 on 2019-08-31 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admdesign', '0003_auto_20190831_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdesigns',
            name='prjdsg_status',
            field=models.CharField(choices=[('P', 'En proceso'), ('D', 'Disponible')], max_length=20, verbose_name='Estado'),
        ),
    ]
