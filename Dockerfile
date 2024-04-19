# Usa un'immagine di Python
FROM python:3.9

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN apt-get install -y python-numpy && \
    apt-get install -y python-scipy

# Imposta la directory di lavoro all'interno dell'immagine
WORKDIR /app

# Scarica il file virtuale.py direttamente da GitHub
RUN curl -o prova.py https://raw.githubusercontent.com/xdvrob/VIRTUALE/main/prova.py
# Specifica il comando di avvio del programma
CMD ["python", "prova.py"]
