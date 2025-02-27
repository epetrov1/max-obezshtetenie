# Generated by Django 5.1.1 on 2024-10-15 12:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_af', models.CharField(max_length=250, null=True)),
                ('title_ar', models.CharField(max_length=250, null=True)),
                ('title_ar_dz', models.CharField(max_length=250, null=True)),
                ('title_ast', models.CharField(max_length=250, null=True)),
                ('title_az', models.CharField(max_length=250, null=True)),
                ('title_bg', models.CharField(max_length=250, null=True)),
                ('title_be', models.CharField(max_length=250, null=True)),
                ('title_bn', models.CharField(max_length=250, null=True)),
                ('title_br', models.CharField(max_length=250, null=True)),
                ('title_bs', models.CharField(max_length=250, null=True)),
                ('title_ca', models.CharField(max_length=250, null=True)),
                ('title_ckb', models.CharField(max_length=250, null=True)),
                ('title_cs', models.CharField(max_length=250, null=True)),
                ('title_cy', models.CharField(max_length=250, null=True)),
                ('title_da', models.CharField(max_length=250, null=True)),
                ('title_de', models.CharField(max_length=250, null=True)),
                ('title_dsb', models.CharField(max_length=250, null=True)),
                ('title_el', models.CharField(max_length=250, null=True)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('title_en_au', models.CharField(max_length=250, null=True)),
                ('title_en_gb', models.CharField(max_length=250, null=True)),
                ('title_eo', models.CharField(max_length=250, null=True)),
                ('title_es', models.CharField(max_length=250, null=True)),
                ('title_es_ar', models.CharField(max_length=250, null=True)),
                ('title_es_co', models.CharField(max_length=250, null=True)),
                ('title_es_mx', models.CharField(max_length=250, null=True)),
                ('title_es_ni', models.CharField(max_length=250, null=True)),
                ('title_es_ve', models.CharField(max_length=250, null=True)),
                ('title_et', models.CharField(max_length=250, null=True)),
                ('title_eu', models.CharField(max_length=250, null=True)),
                ('title_fa', models.CharField(max_length=250, null=True)),
                ('title_fi', models.CharField(max_length=250, null=True)),
                ('title_fr', models.CharField(max_length=250, null=True)),
                ('title_fy', models.CharField(max_length=250, null=True)),
                ('title_ga', models.CharField(max_length=250, null=True)),
                ('title_gd', models.CharField(max_length=250, null=True)),
                ('title_gl', models.CharField(max_length=250, null=True)),
                ('title_he', models.CharField(max_length=250, null=True)),
                ('title_hi', models.CharField(max_length=250, null=True)),
                ('title_hr', models.CharField(max_length=250, null=True)),
                ('title_hsb', models.CharField(max_length=250, null=True)),
                ('title_hu', models.CharField(max_length=250, null=True)),
                ('title_hy', models.CharField(max_length=250, null=True)),
                ('title_ia', models.CharField(max_length=250, null=True)),
                ('title_ind', models.CharField(max_length=250, null=True)),
                ('title_ig', models.CharField(max_length=250, null=True)),
                ('title_io', models.CharField(max_length=250, null=True)),
                ('title_is', models.CharField(max_length=250, null=True)),
                ('title_it', models.CharField(max_length=250, null=True)),
                ('title_ja', models.CharField(max_length=250, null=True)),
                ('title_ka', models.CharField(max_length=250, null=True)),
                ('title_kab', models.CharField(max_length=250, null=True)),
                ('title_kk', models.CharField(max_length=250, null=True)),
                ('title_km', models.CharField(max_length=250, null=True)),
                ('title_kn', models.CharField(max_length=250, null=True)),
                ('title_ko', models.CharField(max_length=250, null=True)),
                ('title_ky', models.CharField(max_length=250, null=True)),
                ('title_lb', models.CharField(max_length=250, null=True)),
                ('title_lt', models.CharField(max_length=250, null=True)),
                ('title_lv', models.CharField(max_length=250, null=True)),
                ('title_mk', models.CharField(max_length=250, null=True)),
                ('title_ml', models.CharField(max_length=250, null=True)),
                ('title_mn', models.CharField(max_length=250, null=True)),
                ('title_mr', models.CharField(max_length=250, null=True)),
                ('title_ms', models.CharField(max_length=250, null=True)),
                ('title_my', models.CharField(max_length=250, null=True)),
                ('title_nb', models.CharField(max_length=250, null=True)),
                ('title_ne', models.CharField(max_length=250, null=True)),
                ('title_nl', models.CharField(max_length=250, null=True)),
                ('title_nn', models.CharField(max_length=250, null=True)),
                ('title_os', models.CharField(max_length=250, null=True)),
                ('title_pa', models.CharField(max_length=250, null=True)),
                ('title_pl', models.CharField(max_length=250, null=True)),
                ('title_pt', models.CharField(max_length=250, null=True)),
                ('title_pt_br', models.CharField(max_length=250, null=True)),
                ('title_ro', models.CharField(max_length=250, null=True)),
                ('title_ru', models.CharField(max_length=250, null=True)),
                ('title_sk', models.CharField(max_length=250, null=True)),
                ('title_sl', models.CharField(max_length=250, null=True)),
                ('title_sq', models.CharField(max_length=250, null=True)),
                ('title_sr', models.CharField(max_length=250, null=True)),
                ('title_sr_latn', models.CharField(max_length=250, null=True)),
                ('title_sv', models.CharField(max_length=250, null=True)),
                ('title_sw', models.CharField(max_length=250, null=True)),
                ('title_ta', models.CharField(max_length=250, null=True)),
                ('title_te', models.CharField(max_length=250, null=True)),
                ('title_tg', models.CharField(max_length=250, null=True)),
                ('title_th', models.CharField(max_length=250, null=True)),
                ('title_tk', models.CharField(max_length=250, null=True)),
                ('title_tr', models.CharField(max_length=250, null=True)),
                ('title_tt', models.CharField(max_length=250, null=True)),
                ('title_udm', models.CharField(max_length=250, null=True)),
                ('title_ug', models.CharField(max_length=250, null=True)),
                ('title_uk', models.CharField(max_length=250, null=True)),
                ('title_ur', models.CharField(max_length=250, null=True)),
                ('title_uz', models.CharField(max_length=250, null=True)),
                ('title_vi', models.CharField(max_length=250, null=True)),
                ('title_zh_hans', models.CharField(max_length=250, null=True)),
                ('title_zh_hant', models.CharField(max_length=250, null=True)),
                ('tag', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('content', models.TextField()),
                ('content_af', models.TextField(null=True)),
                ('content_ar', models.TextField(null=True)),
                ('content_ar_dz', models.TextField(null=True)),
                ('content_ast', models.TextField(null=True)),
                ('content_az', models.TextField(null=True)),
                ('content_bg', models.TextField(null=True)),
                ('content_be', models.TextField(null=True)),
                ('content_bn', models.TextField(null=True)),
                ('content_br', models.TextField(null=True)),
                ('content_bs', models.TextField(null=True)),
                ('content_ca', models.TextField(null=True)),
                ('content_ckb', models.TextField(null=True)),
                ('content_cs', models.TextField(null=True)),
                ('content_cy', models.TextField(null=True)),
                ('content_da', models.TextField(null=True)),
                ('content_de', models.TextField(null=True)),
                ('content_dsb', models.TextField(null=True)),
                ('content_el', models.TextField(null=True)),
                ('content_en', models.TextField(null=True)),
                ('content_en_au', models.TextField(null=True)),
                ('content_en_gb', models.TextField(null=True)),
                ('content_eo', models.TextField(null=True)),
                ('content_es', models.TextField(null=True)),
                ('content_es_ar', models.TextField(null=True)),
                ('content_es_co', models.TextField(null=True)),
                ('content_es_mx', models.TextField(null=True)),
                ('content_es_ni', models.TextField(null=True)),
                ('content_es_ve', models.TextField(null=True)),
                ('content_et', models.TextField(null=True)),
                ('content_eu', models.TextField(null=True)),
                ('content_fa', models.TextField(null=True)),
                ('content_fi', models.TextField(null=True)),
                ('content_fr', models.TextField(null=True)),
                ('content_fy', models.TextField(null=True)),
                ('content_ga', models.TextField(null=True)),
                ('content_gd', models.TextField(null=True)),
                ('content_gl', models.TextField(null=True)),
                ('content_he', models.TextField(null=True)),
                ('content_hi', models.TextField(null=True)),
                ('content_hr', models.TextField(null=True)),
                ('content_hsb', models.TextField(null=True)),
                ('content_hu', models.TextField(null=True)),
                ('content_hy', models.TextField(null=True)),
                ('content_ia', models.TextField(null=True)),
                ('content_ind', models.TextField(null=True)),
                ('content_ig', models.TextField(null=True)),
                ('content_io', models.TextField(null=True)),
                ('content_is', models.TextField(null=True)),
                ('content_it', models.TextField(null=True)),
                ('content_ja', models.TextField(null=True)),
                ('content_ka', models.TextField(null=True)),
                ('content_kab', models.TextField(null=True)),
                ('content_kk', models.TextField(null=True)),
                ('content_km', models.TextField(null=True)),
                ('content_kn', models.TextField(null=True)),
                ('content_ko', models.TextField(null=True)),
                ('content_ky', models.TextField(null=True)),
                ('content_lb', models.TextField(null=True)),
                ('content_lt', models.TextField(null=True)),
                ('content_lv', models.TextField(null=True)),
                ('content_mk', models.TextField(null=True)),
                ('content_ml', models.TextField(null=True)),
                ('content_mn', models.TextField(null=True)),
                ('content_mr', models.TextField(null=True)),
                ('content_ms', models.TextField(null=True)),
                ('content_my', models.TextField(null=True)),
                ('content_nb', models.TextField(null=True)),
                ('content_ne', models.TextField(null=True)),
                ('content_nl', models.TextField(null=True)),
                ('content_nn', models.TextField(null=True)),
                ('content_os', models.TextField(null=True)),
                ('content_pa', models.TextField(null=True)),
                ('content_pl', models.TextField(null=True)),
                ('content_pt', models.TextField(null=True)),
                ('content_pt_br', models.TextField(null=True)),
                ('content_ro', models.TextField(null=True)),
                ('content_ru', models.TextField(null=True)),
                ('content_sk', models.TextField(null=True)),
                ('content_sl', models.TextField(null=True)),
                ('content_sq', models.TextField(null=True)),
                ('content_sr', models.TextField(null=True)),
                ('content_sr_latn', models.TextField(null=True)),
                ('content_sv', models.TextField(null=True)),
                ('content_sw', models.TextField(null=True)),
                ('content_ta', models.TextField(null=True)),
                ('content_te', models.TextField(null=True)),
                ('content_tg', models.TextField(null=True)),
                ('content_th', models.TextField(null=True)),
                ('content_tk', models.TextField(null=True)),
                ('content_tr', models.TextField(null=True)),
                ('content_tt', models.TextField(null=True)),
                ('content_udm', models.TextField(null=True)),
                ('content_ug', models.TextField(null=True)),
                ('content_uk', models.TextField(null=True)),
                ('content_ur', models.TextField(null=True)),
                ('content_uz', models.TextField(null=True)),
                ('content_vi', models.TextField(null=True)),
                ('content_zh_hans', models.TextField(null=True)),
                ('content_zh_hant', models.TextField(null=True)),
                ('featured', models.BooleanField(default=False)),
                ('date_create', models.DateField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
