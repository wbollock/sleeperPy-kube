FROM mongo:latest
WORKDIR /code
COPY app/requirements.txt requirements.txt
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install -r requirements.txt
COPY app/import_data.py .
COPY start.sh .
CMD ["bash", "start.sh"]