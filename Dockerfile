# Usa un'immagine di Python
FROM python:3.9

# Imposta la directory di lavoro all'interno dell'immagine
WORKDIR /app

# Scarica il file virtuale.py direttamente da GitHub
RUN curl -o prova.py https://raw.githubusercontent.com/xdvrob/VIRTUALE/main/prova.py
# Specifica il comando di avvio del programma
CMD ["python", "prova.py"]
