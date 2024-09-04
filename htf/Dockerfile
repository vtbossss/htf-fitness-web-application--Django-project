FROM python:3.9

WORKDIR /htf

COPY Requirements.txt Requirements.txt
RUN pip install -r Requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
