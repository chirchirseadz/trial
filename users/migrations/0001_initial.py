# Generated by Django 3.2.9 on 2022-08-26 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfSpecialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.PositiveIntegerField(null=True, unique=True, verbose_name='National Id')),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('brief_info', models.TextField(blank=True, null=True, verbose_name='Brief Description')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='Location Address')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Mobile Phone Number')),
                ('current_location', models.CharField(choices=[('Nairobi City', 'Nairobi City'), ('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Garissa', 'Garissa'), ('wajir', 'wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ("Murang'a", "Murang'a"), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', 'West Pokot'), ('Samburu', 'Samburu'), ('Trans Nzoia', 'Trans Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Migori'), ('Nyamira', 'Nyamira')], max_length=20)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('company_email', models.EmailField(max_length=254, null=True)),
                ('image', models.ImageField(default='empty.jpg', null=True, upload_to='images/', verbose_name='Profile picture')),
                ('profile_updated', models.BooleanField(default=False)),
                ('area_of_specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.areaofspecialization')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
