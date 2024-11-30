# 実行手順

## １．起動
'docker compose up -d'

## ２．データベース接続
'docker compose exec postgres -U guest -d my-db'

## ３．a5m2からの接続
compose.ymlに記載されているport、user、password、dbを設定する。