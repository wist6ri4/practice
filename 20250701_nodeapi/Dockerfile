# Node.js Version: 22のイメージを使用
FROM node:22

# アプリケーションの作業ディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# 依存関係をインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

CMD ["npm", "run", "dev"]