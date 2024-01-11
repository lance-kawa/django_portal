FROM python:3.12   

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000  
WORKDIR /app
CMD ["python", "manage.py", "runserver"]
