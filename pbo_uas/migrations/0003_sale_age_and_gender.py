# Generated by Django 5.1 on 2024-05-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbo_uas', '0002_alter_sale_change_alter_sale_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='age',
            field=models.IntegerField(choices=[('1', '<20'), ('2', '20-29'), ('3', '30-39'), ('4', '40-49'), ('5', '50-59'), ('6', '>60')], default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sale',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
            preserve_default=False,
        ),
    ]