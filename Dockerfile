FROM python:3.12.7-alpine3.20
COPY . /app
WORKDIR /app
RUN apk update && apk add --no-cache net-tools
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
