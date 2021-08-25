Скачиваем приложение:

```bash
git clone 
```

Создаем виртуальное окружение:

```bash
python3 -m venv venv
```

Устанавливаем все зависмости:

```bash
pip install -r requirements.txt
```

Создаем ```.env``` файл и записываем в перменную ```SITE_URL``` адрес сайта с результатами пойска машины.

Из каталога ```/kolesa``` апускаем программу:

```bash
 scrapy crawl kolesa_spider -O data.json
```

Результаты парсинга будут в файле data.json в корне проекта.