# Oficina API Project

Basic commands to start python projects

Enviroment and Requirement

```console
 python -m venv venv
 .\venv\Scripts\activate
 pip install -r requirements.txt
```

 Documentation [https://www.mkdocs.org/getting-started/]

```console
 mkdocs serve
```

 Run APIs [https://fastapi.tiangolo.com/] + [https://www.uvicorn.org/]

```console
uvicorn src.app.api:app --reload
```

 Start Containers

```console
 docker-compose -f .\docker-compose.yaml up
 ```
