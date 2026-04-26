FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80
COPY . .

CMD ["fastapi", "run", "main.py", "--port", "80"]