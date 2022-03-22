FROM alpine:3.15

RUN apk add --update apk-cron \
    httpie \
    py3-pip && rm -rf /var/cache/apk/*
ADD docker/crontab.txt /crontab.txt
ADD bin/spotprice.sh /bin/spotprice.sh
RUN /usr/bin/crontab /crontab.txt
ADD docker/entry.sh /entry.sh
RUN chmod 755 /entry.sh

# Main app
ADD requirements.txt /
ADD spotprice /spotprice
RUN pip3 install -r requirements.txt



CMD ["/entry.sh"]
