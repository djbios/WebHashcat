# Generated by Django 3.0.7 on 2020-06-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hashcat', '0003_auto_20200610_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='hash',
            name='hash_hash',
            field=models.CharField(max_length=190, null=True),
        ),
        migrations.AlterField(
            model_name='hash',
            name='hash',
            field=models.TextField(max_length=4096, null=True),
        ),
        migrations.AddIndex(
            model_name='hash',
            index=models.Index(fields=['hashfile', 'hash_hash'], name='hashfileid_hash_index'),
        ),
        migrations.AddIndex(
            model_name='hash',
            index=models.Index(fields=['hash_hash', 'hash_type'], name='hash_index'),
        ),
    ]
