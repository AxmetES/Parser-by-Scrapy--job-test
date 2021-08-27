Скачиваем приложение:

```bash
git clone https://github.com/AxmetES/Parser-by-Scrapy--job-test.git
```

Билдим image докера:

```bash
docker build -t scrapy .
```

Запускаем контейнер:

```bash
docker run --rm -v {your home dir}:/scrapy -it scrapy crawl kolesa_spider -O data.json
```

For example:

```bash
docker run --rm -v /home/pydev/Desktop/job_tests/Parser-by-Scrapy--job-test:/scrapy -it scrapy crawl kolesa_spider -O data.json
```

Результаты парсинга будут в файле data.json в корне проекта.