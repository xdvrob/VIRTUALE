FROM python:3.9

# Imposta la directory di lavoro all'interno dell'immagine
WORKDIR /app

# Installa git per clonare il repository
RUN apt-get update && apt-get install -y git

# Clona il repository GitHub del tuo programma
RUN git clone <https://github.com/xdvrob/VIRTUALE/blob/main/virtuale.py> .

# Installa le dipendenze del programma Python
RUN pip install -r requirements.txt

# Specifica il comando di avvio del programma
CMD ["python", "virtuale.py"]
