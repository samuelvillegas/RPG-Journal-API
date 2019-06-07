# Generated by Django 2.2.1 on 2019-06-05 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habittracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='number_of_days',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('note', models.CharField(max_length=250)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='habittracker.Habit')),
            ],
        ),
    ]
