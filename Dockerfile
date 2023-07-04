FROM python:3-alpine AS base
ENV PYTHONUNBUFFERED 1
COPY ./ ./app/

FROM base AS front

WORKDIR /app/front/

RUN pip install poetry
RUN poetry install
ENV PYTHONPATH=$PYTHONPATH:/app/iso8583/
ADD ./iso8583 /app/front

FROM base AS back

WORKDIR /app/back/

RUN pip install poetry
RUN poetry install
ENV PYTHONPATH=$PYTHONPATH:/app/iso8583/

FROM base AS authorizer

WORKDIR /app/authorizer/

RUN pip install poetry
RUN poetry install

FROM base AS crud
WORKDIR /app/simple_crud/
RUN pip install poetry
RUN poetry install

FROM mongo AS mongo
