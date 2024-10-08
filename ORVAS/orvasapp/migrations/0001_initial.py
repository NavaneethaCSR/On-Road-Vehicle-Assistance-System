# Generated by Django 5.0 on 2023-12-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mobile_no', models.CharField(max_length=30)),
                ('SMS', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('pass1', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Vehicle_Type', models.CharField(max_length=30)),
                ('Vehicle_No', models.CharField(max_length=30)),
                ('Problem', models.CharField(max_length=30)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enter_Name', models.CharField(max_length=30)),
                ('Write_review', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('pass1', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=255)),
                ('mechanic_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=355)),
                ('number', models.CharField(max_length=12)),
                ('service', models.CharField(max_length=255)),
                ('vehicle_types', models.CharField(max_length=22)),
                ('image', models.CharField(max_length=2500)),
            ],
        ),
    ]
