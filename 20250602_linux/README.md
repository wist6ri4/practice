# ０．環境構築
## ①Docker Imageのpull
``` bash
docker pull ubuntu
```
## ②コンテナの起動
``` bash
docker run -d -it --name sample-ubuntu ubuntu
```
-d：コンテナをバックグラウンドで実行し、コンテナ ID を表示
-it：コンテナの STDIN にアタッチ・疑似ターミナル (pseudo-TTY) を割り当て
## ③コンテナのbashに接続
``` bash
docker exec -it sample-ubuntu bash
```

# １．パッケージ管理
``` bash
# aptが管理するパッケージのリストを更新
apt update

# パッケージのインストール
apt install パッケージ名

# パッケージのバージョンアップ
## すべてのパッケージ
apt upgrade
## 特定のパッケージ
apt install --only-upgrade パッケージ名

# パッケージの削除
apt remove パッケージ名
```

# ２．ディレクトリの操作
``` bash
# カレントディレクトリ
pwd

# ディレクトリの確認
ls ディレクトリパス
ll ディレクトリパス
## オプション
-l：詳細表示

```