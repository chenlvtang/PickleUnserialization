FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN apt install -y python3 python3-pip nginx netcat curl wget
RUN pip3 install flask gunicorn

RUN groupadd -r ctf && useradd -r -g ctf ctf
RUN mkdir -p /home/ctf/

COPY flag.txt server.py /home/ctf/
COPY static /home/ctf/static/
COPY templates /home/ctf/templates/
COPY ctf-site /etc/nginx/sites-enabled/
RUN rm /etc/nginx/sites-enabled/default

RUN chown -R root:ctf /home/ctf/
RUN chmod -R 750 /home/ctf/

WORKDIR /home/ctf/

CMD nginx && gunicorn server -b 0.0.0.0:8000 -u ctf -g ctf