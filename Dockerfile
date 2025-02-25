FROM python:3.12.7-alpine3.20

RUN apk update && apk cache clean && apk -U upgrade --no-cache

COPY requirements.txt /requirements.txt
RUN pip install --root-user-action=ignore -r /requirements.txt

RUN mkdir /app

WORKDIR /app

COPY k8s_utils.py acme_challenge_dispatcher.py config.py /app/

RUN python -m pip uninstall --root-user-action=ignore -y pip && \
    apk --purge del apk-tools && \
    rm -rf ~/.cache

RUN addgroup -S -g 10001 acme-user
RUN adduser -S -u 10001 -G acme-user -H -s /sbin/nologin acme-user
RUN chown -R acme-user:acme-user /app

USER acme-user

CMD ["gunicorn", "acme_challenge_dispatcher:app", "--config", "config.py"]