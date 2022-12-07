FROM python:3.10-url-Uploader-Bot-V2.0-Render

WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]
