# Usa un'immagine di Python
FROM python:3.9

# Imposta la directory di lavoro all'interno dell'immagine
WORKDIR /app

# Scarica il file virtuale.py direttamente da GitHub
RUN curl -o virtuale.py https://raw.githubusercontent.com/xdvrob/VIRTUALE/main/virtuale.py

# Installa le dipendenze del programma Python
RUN pip install requirements.txt

# Specifica il comando di avvio del programma
CMD ["python", "virtuale.py"]
