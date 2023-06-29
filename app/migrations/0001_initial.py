# Generated by Django 4.1.5 on 2023-06-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(choices=[('remote', '1'), ('office', '2')], default='office', max_length=10)),
                ('posted_on', models.DateField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
