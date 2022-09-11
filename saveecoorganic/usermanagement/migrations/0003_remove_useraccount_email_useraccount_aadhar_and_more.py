# Generated by Django 4.1 on 2022-09-11 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usermanagement', '0002_useraccount_address_useraccount_alt_mobile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='email',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='aadhar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='aadhar_image',
            field=models.ImageField(blank=True, null=True, upload_to='kyc_images/'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='account_holder_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='account_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='bank_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='branch',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='pan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='pan_image',
            field=models.ImageField(blank=True, null=True, upload_to='kyc_images/'),
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_amount', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StoreDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.CharField(blank=True, max_length=255, null=True)),
                ('gen_info_complete', models.BooleanField(default=False)),
                ('kyc_done', models.BooleanField(default=False)),
                ('proprietor_name', models.CharField(default='Save Eco Organic', max_length=100)),
                ('mobile', models.CharField(max_length=255)),
                ('alt_mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('gst', models.CharField(max_length=255, null=True)),
                ('gst_doc', models.FileField(null=True, upload_to='store/')),
                ('lat_long', models.CharField(max_length=255, null=True)),
                ('is_number_verified', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('EC', 'ECO CENTER'), ('ST', 'STOCKIST'), ('DS', 'DISTRIBUTOR')], default='EC', max_length=20)),
                ('store_under', models.ForeignKey(blank=True, limit_choices_to={'store': True}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='stores', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MixMatchingCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_count', models.IntegerField(default=0)),
                ('right_count', models.IntegerField(default=0)),
                ('left_pair', models.IntegerField(default=0)),
                ('right_pair', models.IntegerField(default=0)),
                ('total_pair', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]