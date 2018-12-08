FROM tiangolo/uwsgi-nginx-flask:python3.7


RUN pip install docker boto3 flask-restplus Flask-SQLAlchemy pandas markdown \
    flask-cors paramiko scp

# RUN curl -L http://xrl.us/installperlnix | bash
RUN apt-get install perl
RUN mkdir /root/.ssh
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
RUN cd / && \
    git clone https://github.com/gglusman/data-fingerprints.git

RUN apt-get update && apt-get install dnsutils -y

RUN cpan JSON
COPY ./app /app
