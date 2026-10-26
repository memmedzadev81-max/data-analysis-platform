# DATA Analysis 5.2

Böyük şirkətlər üçün data analitika, data science və data mühəndisliyi platforması. Excel, SQL client, Python notebook və Power BI tipli işləri bir yerdə birləşdirir; bir çox bölmədə AI dəstəyi var.

## İşə salmaq

```bash
pip install -r requirements.txt
python run.py
```

Brauzerdə açılır (`http://127.0.0.1` + port). Server üçün: `python run.py --no-browser`.

## Əsas bölmələr

- **Məlumatlar** — CSV, Excel, JSON, Parquet, PDF/Word cədvəlləri; JOIN
- **Gözləyən fayllar** — iri/xam fayllar üçün növbə, ZIP təhlükəsiz açılış
- **Açıq kataloqlar** — Kaggle, Hugging Face, OpenML, World Bank, Eurostat və s.
- **Avto-hazırlıq** — kirli məlumatın təmizlənməsi və keyfiyyət balı
- **Cədvəl / təmizləmə** — Power Query tipli addımlar, AI ilə təmizləmə
- **Pivot** — çox aqreqat, % və sıralama rejimləri
- **Python notebook** — SQL (`%%sql`), AI kod, kitabxana paneli
- **Diaqramlar, statistik testlər, ML, A/B, causal**

## Qovluq

```
run.py                 giriş nöqtəsi
dataanalysis/          əsas Python paketi
tests/                 avtomat testlər
android/ mobile/       mobil/Android hissələr
plugins/               nümunə plugin
```

Tam mənbə kodu bu repoda yerləşdirilir. İkon/binary fayllar və böyük i18n JSON-ları üçün ZIP-dən əlavə yükləmə tələb oluna bilər.

## Lisenziya / müəllif

Vusal Mammadzade · [memmedzadev81-max](https://github.com/memmedzadev81-max)
