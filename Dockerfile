FROM node:16-alpine AS front

#WORKDIR /app

COPY ./ ./app/
WORKDIR /app/front/

RUN npm i
RUN npm run build


FROM python:3-alpine AS back

#WORKDIR /app


COPY ./ /app/
WORKDIR /app/back/

#RUN pip install --upgrade pip

RUN pip install -r requirements.txt
