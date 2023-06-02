#FROM mongo:4.2.24
FROM python:3

# install Python 3
#RUN apt-get update && apt-get install -y python3 python3-pip bash
RUN pip3 install pymongo
RUN pip3 install flask

WORKDIR /scripts
#COPY ./app.py /scripts
EXPOSE 5000

CMD ["python3", "/scripts/current.py"]
