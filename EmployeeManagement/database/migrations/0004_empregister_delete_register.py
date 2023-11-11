# Generated by Django 4.2 on 2023-11-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_register_delete_employeeregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='empregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('jobtitle', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]