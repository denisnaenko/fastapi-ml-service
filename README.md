# fastapi-ml-service
FastAPI Lab

### Запуск Docker
```
docker build -t iris-api .
docker run -p 8000:80 iris-api
```

### Примеры запросов

Запрос:
```
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [5.1, 3.5, 1.4, 0.2]}'
```
Ответ:
```
{"prediction": 0}
```

Запрос:
```
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"data": [7.0, 3.2, 4.7, 1.4]}'
```
Ответ:
```
{"prediction": 1}
```
