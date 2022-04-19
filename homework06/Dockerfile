FROM python:3.9

RUN mkdir /app
WORKDIR /app

#RUN yum update -y && \
#    yum install -y python3

RUN pip3 install --user flask && \
    pip3 install --user redis

COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
