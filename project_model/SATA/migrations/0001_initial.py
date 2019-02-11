# Generated by Django 2.1.5 on 2019-02-11 09:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_challenge', models.CharField(max_length=255)),
                ('banyak_soal', models.IntegerField()),
                ('bobot_nilai', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Direksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('no_telepon', models.IntegerField()),
                ('jabatan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Live_Code',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_live_code', models.CharField(max_length=255)),
                ('banyak_soal', models.IntegerField()),
                ('bobot_nilai', models.IntegerField()),
                ('tanggal_pelaksanaan', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mata_Pelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelajaran', models.CharField(max_length=255)),
                ('jadwal_dimulai', models.CharField(max_length=255)),
                ('jadwal_berakhir', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('no_telepon', models.IntegerField()),
                ('nomor_absen', models.IntegerField()),
                ('nilai_rata', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('no_telepon', models.IntegerField()),
                ('mata_pelajaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SATA.Mata_Pelajaran')),
            ],
        ),
        migrations.AddField(
            model_name='live_code',
            name='mata_pelajaran',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SATA.Mata_Pelajaran'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='mata_pelajaran',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SATA.Mata_Pelajaran'),
        ),
    ]