 FROM python:3.6.3-jessie
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD ./src/requirements.txt /code/
 RUN pip install -r requirements.txt
 ADD ./src/ /code/
