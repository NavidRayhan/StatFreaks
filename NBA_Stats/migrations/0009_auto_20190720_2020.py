# Generated by Django 2.1.7 on 2019-07-21 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NBA_Stats', '0008_auto_20190720_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advanced_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PER', models.FloatField(default=None)),
                ('True_shooting', models.FloatField(default=None)),
                ('ThreeP_attempt_rate', models.FloatField(default=None)),
                ('Rebound_perc', models.FloatField(default=None)),
                ('Offensive_rebound_perc', models.FloatField(default=None)),
                ('Defensive_rebound_perc', models.FloatField(default=None)),
                ('Assist_perc', models.FloatField(default=None)),
                ('Steal_perc', models.FloatField(default=None)),
                ('Block_perc', models.FloatField(default=None)),
                ('Turnover_perc', models.FloatField(default=None)),
                ('Usage', models.FloatField(default=None)),
                ('Offensive_winshares_per48', models.FloatField(default=None)),
                ('Defensive_winshares_per48', models.FloatField(default=None)),
                ('Offensive_BPM', models.FloatField(default=None)),
                ('Defensive_BMP', models.FloatField(default=None)),
                ('Value_over_replacement_player', models.FloatField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Basic_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Points', models.FloatField(default=None)),
                ('Assists', models.FloatField(default=None)),
                ('Rebounds', models.FloatField(default=None)),
                ('Age', models.IntegerField(default=None)),
                ('Games', models.IntegerField(default=None)),
                ('Minutes', models.FloatField(default=None)),
                ('Field_Goals_attempted', models.FloatField(default=None)),
                ('Field_Goal_percentage', models.FloatField(default=None)),
                ('ThreeP_attempted', models.FloatField(default=None)),
                ('ThreeP_percentage', models.FloatField(default=None)),
                ('Offensive_rebounds', models.FloatField(default=None)),
                ('Eff_FGP', models.FloatField(default=None)),
                ('Free_throws', models.FloatField(default=None)),
                ('Free_throw_percentage', models.FloatField(default=None)),
                ('Steals', models.FloatField(default=None)),
                ('Blocks', models.FloatField(default=None)),
                ('Turnovers', models.FloatField(default=None)),
                ('Fouls', models.FloatField(default=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='single_player_year',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='single_player_year',
            name='Year',
        ),
        migrations.AddField(
            model_name='single_season',
            name='Name',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AlterField(
            model_name='single_season',
            name='Year',
            field=models.IntegerField(default=None),
        ),
        migrations.DeleteModel(
            name='Single_Player',
        ),
        migrations.DeleteModel(
            name='Single_Player_Year',
        ),
        migrations.AddField(
            model_name='basic_stats',
            name='Name_Year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NBA_Stats.Single_Season'),
        ),
        migrations.AddField(
            model_name='advanced_stats',
            name='Name_Year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NBA_Stats.Single_Season'),
        ),
    ]