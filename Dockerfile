FROM python:3.11.0a6-alpine3.15
ARG GIT_COMMIT
ENV GIT_COMMIT=$GIT_COMMIT
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt --no-cache-dir
RUN apk add curl
COPY . /code
CMD python app.py