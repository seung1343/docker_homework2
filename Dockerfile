FROM alpine:latest
RUN apk add python3
COPY record.py ./
CMD ["python3","record.py"]
