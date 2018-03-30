FROM debian:9
RUN apt-get update -q
RUN apt-get install python-pip -yq
RUN apt-get install python3-pip -yq
RUN pip3 install proxybroker
WORKDIR /opt/proxy
ADD . .
CMD python runner.py
