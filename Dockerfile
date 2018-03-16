FROM          alpine:3.7

ADD           install.sh /install.sh
ADD           entrypoint.sh /entrypoint.sh
ADD           fullcontact.py /fullcontact.py
RUN           /install.sh && rm -f /install.sh

ENTRYPOINT   ["/entrypoint.sh"]
