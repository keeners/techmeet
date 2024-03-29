# Generated by Django 2.2.2 on 2019-07-06 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20190706_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='start')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='end')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('tech_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='data.TechGroup')),
            ],
        ),
    ]
