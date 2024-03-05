# Generated by Django 5.0 on 2024-03-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendor", "0006_alter_openinghour_day_alter_openinghour_is_closed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="openinghour",
            name="from_hour",
            field=models.CharField(
                blank=True,
                choices=[
                    ("12:00:AM", "12:00:AM"),
                    ("12:30:AM", "12:30:AM"),
                    ("01:00:AM", "01:00:AM"),
                    ("01:30:AM", "01:30:AM"),
                    ("02:00:AM", "02:00:AM"),
                    ("02:30:AM", "02:30:AM"),
                    ("03:00:AM", "03:00:AM"),
                    ("03:30:AM", "03:30:AM"),
                    ("04:00:AM", "04:00:AM"),
                    ("04:30:AM", "04:30:AM"),
                    ("05:00:AM", "05:00:AM"),
                    ("05:30:AM", "05:30:AM"),
                    ("06:00:AM", "06:00:AM"),
                    ("06:30:AM", "06:30:AM"),
                    ("07:00:AM", "07:00:AM"),
                    ("07:30:AM", "07:30:AM"),
                    ("08:00:AM", "08:00:AM"),
                    ("08:30:AM", "08:30:AM"),
                    ("09:00:AM", "09:00:AM"),
                    ("09:30:AM", "09:30:AM"),
                    ("10:00:AM", "10:00:AM"),
                    ("10:30:AM", "10:30:AM"),
                    ("11:00:AM", "11:00:AM"),
                    ("11:30:AM", "11:30:AM"),
                    ("12:00:PM", "12:00:PM"),
                    ("12:30:PM", "12:30:PM"),
                    ("01:00:PM", "01:00:PM"),
                    ("01:30:PM", "01:30:PM"),
                    ("02:00:PM", "02:00:PM"),
                    ("02:30:PM", "02:30:PM"),
                    ("03:00:PM", "03:00:PM"),
                    ("03:30:PM", "03:30:PM"),
                    ("04:00:PM", "04:00:PM"),
                    ("04:30:PM", "04:30:PM"),
                    ("05:00:PM", "05:00:PM"),
                    ("05:30:PM", "05:30:PM"),
                    ("06:00:PM", "06:00:PM"),
                    ("06:30:PM", "06:30:PM"),
                    ("07:00:PM", "07:00:PM"),
                    ("07:30:PM", "07:30:PM"),
                    ("08:00:PM", "08:00:PM"),
                    ("08:30:PM", "08:30:PM"),
                    ("09:00:PM", "09:00:PM"),
                    ("09:30:PM", "09:30:PM"),
                    ("10:00:PM", "10:00:PM"),
                    ("10:30:PM", "10:30:PM"),
                    ("11:00:PM", "11:00:PM"),
                    ("11:30:PM", "11:30:PM"),
                ],
                default="Closed",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="openinghour",
            name="is_closed",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="openinghour",
            name="to_hour",
            field=models.CharField(
                blank=True,
                choices=[
                    ("12:00:AM", "12:00:AM"),
                    ("12:30:AM", "12:30:AM"),
                    ("01:00:AM", "01:00:AM"),
                    ("01:30:AM", "01:30:AM"),
                    ("02:00:AM", "02:00:AM"),
                    ("02:30:AM", "02:30:AM"),
                    ("03:00:AM", "03:00:AM"),
                    ("03:30:AM", "03:30:AM"),
                    ("04:00:AM", "04:00:AM"),
                    ("04:30:AM", "04:30:AM"),
                    ("05:00:AM", "05:00:AM"),
                    ("05:30:AM", "05:30:AM"),
                    ("06:00:AM", "06:00:AM"),
                    ("06:30:AM", "06:30:AM"),
                    ("07:00:AM", "07:00:AM"),
                    ("07:30:AM", "07:30:AM"),
                    ("08:00:AM", "08:00:AM"),
                    ("08:30:AM", "08:30:AM"),
                    ("09:00:AM", "09:00:AM"),
                    ("09:30:AM", "09:30:AM"),
                    ("10:00:AM", "10:00:AM"),
                    ("10:30:AM", "10:30:AM"),
                    ("11:00:AM", "11:00:AM"),
                    ("11:30:AM", "11:30:AM"),
                    ("12:00:PM", "12:00:PM"),
                    ("12:30:PM", "12:30:PM"),
                    ("01:00:PM", "01:00:PM"),
                    ("01:30:PM", "01:30:PM"),
                    ("02:00:PM", "02:00:PM"),
                    ("02:30:PM", "02:30:PM"),
                    ("03:00:PM", "03:00:PM"),
                    ("03:30:PM", "03:30:PM"),
                    ("04:00:PM", "04:00:PM"),
                    ("04:30:PM", "04:30:PM"),
                    ("05:00:PM", "05:00:PM"),
                    ("05:30:PM", "05:30:PM"),
                    ("06:00:PM", "06:00:PM"),
                    ("06:30:PM", "06:30:PM"),
                    ("07:00:PM", "07:00:PM"),
                    ("07:30:PM", "07:30:PM"),
                    ("08:00:PM", "08:00:PM"),
                    ("08:30:PM", "08:30:PM"),
                    ("09:00:PM", "09:00:PM"),
                    ("09:30:PM", "09:30:PM"),
                    ("10:00:PM", "10:00:PM"),
                    ("10:30:PM", "10:30:PM"),
                    ("11:00:PM", "11:00:PM"),
                    ("11:30:PM", "11:30:PM"),
                ],
                default="Closed",
                max_length=10,
            ),
        ),
    ]
