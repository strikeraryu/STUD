# Generated by Django 3.1 on 2020-12-14 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('class_no', models.OneToOneField(db_column='class_no', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='schedule.class')),
            ],
            options={
                'db_table': 'teaches',
                'managed': False,
            },
        ),
    ]
