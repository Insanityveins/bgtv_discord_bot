FROM python:3.12.9-slim

WORKDIR /usr/src/app
COPY src/ .

RUN python3.12 -m pip install -r requirements.txt
CMD ["python3.12", "jahbot.py"]