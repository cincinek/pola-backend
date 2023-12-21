# Generated by Django 3.2.16 on 2023-12-18 19:33

import django_resized.forms
import storages.backends.s3
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('company', '0029_alter_company_logotype'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logotype',
            field=django_resized.forms.ResizedImageField(
                blank=True,
                crop=None,
                force_format='PNG',
                keep_meta=True,
                null=True,
                quality=-1,
                scale=None,
                size=[None, 200],
                storage=storages.backends.s3.S3Storage(
                    bucket_name='pola-app-company-logotype',
                    default_acl=None,
                    querystring_auth=True,
                    region_name='eu-central-1',
                ),
                upload_to='brand-logotype/%Y/%m/%d',
                verbose_name='Logotyp',
            ),
        ),
    ]
