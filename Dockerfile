FROM python:3-alpine AS front

#WORKDIR /app

COPY ./ ./app/
WORKDIR /app/front/

#RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

RUN #pip install -r requirements.txt


FROM python:3-alpine AS back

#WORKDIR /app


COPY ./ /app/
WORKDIR /app/back/

#RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
RUN #pip install -r requirements.txt

FROM python:3-alpine AS crud

#WORKDIR /app


COPY ./ /app/
WORKDIR /app/simple_crud/

#RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install
RUN #pip install -r requirements.txt

FROM mongo AS mongo
