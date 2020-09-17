FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1

COPY docker/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt


# RUN apt-get update && apt-get install -y nano


WORKDIR /root/code
