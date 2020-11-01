## Flaskアプリケーション用スケルトン
Dockerのインストールが必須です。

Windows環境の場合は要makeインストール

### makeコマンド（起動、停止、削除）
```
# make run
# make stop
# make rm
```

### 構成
```
.
├── docker-compose.yml
├── Makefile
├── README.md
├── app
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── run.py
│   ├── uwsgi.ini
│   ├── src
│   │   ├── batch
│   │   │   ├── __init__.py
│   │   │   └── xxx.py
│   │   ├── config
│   │   │   ├── __init__.py
│   │   │   └── default.py
│   │   ├── views
│   │   │   ├── __init__.py
│   │   │   └── xxx.py
│   ├── static
│   │   └── honoka(bootstrap contents)
│   └── tests
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
└── postgres
    ├── Dockerfile
    └── xxx.conf
```
