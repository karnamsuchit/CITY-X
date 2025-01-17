# Generated by Django 5.0.6 on 2024-06-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg_Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_num', models.CharField(editable=False, max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('description', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=15)),
                ('experience_years', models.PositiveIntegerField()),
                ('certificate', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
