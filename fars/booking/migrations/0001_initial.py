# Generated by Django 2.0.3 on 2018-03-15 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('description', models.TextField()),
                ('bookable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Bookable')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='timeslot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booking.Timeslot'),
        ),
    ]