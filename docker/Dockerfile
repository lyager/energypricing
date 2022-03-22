FROM alpine:3.15

RUN apk add --update apk-cron \
    httpie && rm -rf /var/cache/apk/*
ADD docker/crontab.txt /crontab.txt
ADD bin/spotprice.sh /bin/spotprice.sh
RUN /usr/bin/crontab /crontab.txt
COPY docker/entry.sh /entry.sh
RUN chmod 755 /entry.sh


CMD ["/entry.sh"]
