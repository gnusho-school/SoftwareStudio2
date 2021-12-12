# Generated by Django 4.0 on 2021-12-11 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_work_delete_schedule_longterm_shortterm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repeated',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schedule.work')),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('term', models.IntegerField()),
            ],
            bases=('schedule.work',),
        ),
    ]