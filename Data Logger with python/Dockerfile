FROM python:3.9.18-alpine3.18
EXPOSE 6379
RUN pip install redis
WORKDIR /cgt_mail

COPY . /cgt_mail/
CMD ["python3","sending_mail.py"]   