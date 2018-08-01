# Generated by Django 2.0.7 on 2018-08-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('experience', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=70)),
                ('phone_no', models.BigIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('education', models.CharField(max_length=250)),
                ('current_location', models.CharField(max_length=100)),
            ],
        ),
    ]