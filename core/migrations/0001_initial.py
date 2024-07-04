# Generated by Django 5.0.6 on 2024-07-04 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inclusao', models.DateField(auto_now_add=True, verbose_name='Data')),
                ('filial', models.IntegerField(default=1)),
                ('nome', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('email', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('atendimento', models.IntegerField(default=0)),
                ('apresentacao', models.IntegerField(default=0)),
                ('qualidade', models.IntegerField(default=0)),
                ('observacao', models.CharField(blank=True, default='-', max_length=2000, null=True)),
                ('detalhes', models.CharField(blank=True, default='-', max_length=2000, null=True)),
            ],
            options={
                'verbose_name': 'NPS',
                'verbose_name_plural': 'NPS',
                'db_table': 'nps',
                'ordering': ['data_inclusao'],
            },
        ),
    ]
