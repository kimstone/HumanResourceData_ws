# Generated by Django 3.1.7 on 2021-03-16 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mission', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mission', models.CharField(max_length=500)),
                ('relationship', models.CharField(blank=True, choices=[('child', 'Child'), ('husband', 'Husband'), ('wife', 'Wife')], max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('min_salary', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('max_salary', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
