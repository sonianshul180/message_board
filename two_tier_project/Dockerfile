FROM python:3.8-slim

WORKDIR /two_tier

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000

CMD ["gunicorn", "two_tier_project.wsgi:application", "--bind", "0.0.0.0:8000"]
~                                                                                                                                                             
~                                                                                                                                                             
~                                                                                                                                                             
~                                                                                           
