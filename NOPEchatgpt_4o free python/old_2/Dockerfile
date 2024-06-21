# Используйте образ Debian, так как образы Python не имеют версии 3.14.4
FROM debian:buster-slim

# Установите необходимые пакеты
RUN apt-get update && apt-get install -y \
    firefox-esr \
    xvfb \
    wget \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev

# Скачайте и установите Python 3.10.0
RUN wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz && \
    tar xvf Python-3.10.0.tgz && \
    cd Python-3.10.0 && \
    ./configure && \
    make && \
    make install

# Установите pip
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py

# Установите вашу библиотеку
RUN pip install pyautogui

# Копируйте ваш Python скрипт в контейнер
# COPY your_script.py .


