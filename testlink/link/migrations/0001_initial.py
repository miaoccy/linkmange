# Generated by Django 3.1 on 2020-08-24 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prolink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpname', models.CharField(max_length=100)),
                ('linknum', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkname', models.CharField(max_length=64)),
                ('link', models.URLField()),
                ('linkhj', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('prolink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='link.prolink')),
            ],
            options={
                'unique_together': {('prolink', 'linkname', 'link')},
            },
        ),
    ]