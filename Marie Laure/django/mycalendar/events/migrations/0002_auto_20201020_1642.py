# Generated by Django 3.1.2 on 2020-10-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(help_text='Sélectionnez une date', verbose_name='Date')),
                ('start_time', models.TimeField(help_text='Sélectionnez un heure de début', verbose_name='Heure de début')),
                ('appointment_type', models.CharField(choices=[('SIM', 'Rendez-vous simple'), ('SPE', 'Rendez-vous spécialiste'), ('MAN', 'Rendez-vous avec manipulation')], default='SIM', help_text='Sélectionnez un type de rendez-vous', max_length=3, verbose_name='Type de rendez-vous')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.DeleteModel(
            name='AppointmentType',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
