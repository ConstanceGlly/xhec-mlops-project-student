FROM python:3.10.13-slim
WORKDIR /app_home
COPY ./requirements_app.txt /app_home/requirements_app.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app_home/requirements_app.txt
COPY ./src/web_service /app_home/web_service
WORKDIR /app_home/web_service

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
