FROM python:3.11-slim-buster
ENV PYTHONUNBUFFERED=1

COPY . /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN chmod -R 755 /app/static/
RUN python manage.py migrate

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]