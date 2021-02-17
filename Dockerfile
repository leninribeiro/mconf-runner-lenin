FROM python:3

COPY . .

RUN pip install requests

EXPOSE 8000

ENTRYPOINT ["python", "runner.py"]