FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED=1

WORKDIR /scrapy

COPY . /scrapy

RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /scrapy/kolesa/

ENTRYPOINT ["scrapy"]

CMD []