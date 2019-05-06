FROM python:3.6
ENV PYTHONBUFFERED 1
RUN mkdir /FezComicRESTPy-Service
WORKDIR /FezComicRESTPy-Service
ADD . /FezComicRESTPy-Service/
EXPOSE 8000
RUN pip install -r requirements.txt