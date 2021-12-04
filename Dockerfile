FROM python:latest
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt
# mongo tools are required for mongoimport
# annoyingly, doesn't seem like pymongo can import collection data
RUN wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-debian10-x86_64-100.5.1.deb
RUN apt install ./mongodb-database-tools-debian10-x86_64-100.5.1.deb
COPY app/import_data.py .
#COPY app/app.py .
# the app portion is not ready
COPY start.sh .
CMD ["bash", "start.sh"]