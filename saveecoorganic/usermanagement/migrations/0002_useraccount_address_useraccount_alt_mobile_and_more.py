# Generated by Django 4.1 on 2022-09-08 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='alt_mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='anniversary',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='father',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='gen_info_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_married',
            field=models.CharField(choices=[('Married', 'Married'), ('Un-Married', 'Un-Married')], default='Un-Married', max_length=12),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_number_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='kyc_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='nominee_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='pincode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='position',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='referral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Direct', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='relation',
            field=models.CharField(choices=[('mother', 'Mother'), ('father', 'Father'), ('others', 'others')], default='mother', max_length=10),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='sponsor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Placement', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Blocked', 'Blocked')], default='Active', max_length=10),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='mobile',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
