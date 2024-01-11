FROM python:3.12   

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000  

ENTRYPOINT ["./migrate.sh"]
WORKDIR /app
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]
