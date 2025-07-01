
# 🛠 Node.js API開発環境構築手順書（Docker + nodemon + routing-controllers）

## ✅ 前提

- Docker / Docker Compose が使える環境（WSL2, macOS, Linux, etc）
- Node.js プロジェクト未作成の状態から始める

---

## 1. プロジェクト作成

```bash
mkdir my-api
cd my-api
npm init -y
```

---

## 2. 必要なパッケージをインストール

```bash
npm install express routing-controllers reflect-metadata class-transformer class-validator
npm install --save-dev typescript ts-node nodemon @types/node
```

---

## 3. 設定ファイルを作成

### ✅ tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES6",
    "module": "CommonJS",
    "lib": ["ES6"],
    "rootDir": "src",
    "outDir": "dist",
    "strict": true,
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

### ✅ nodemon.json

```json
{
  "watch": ["src"],
  "ext": "ts",
  "exec": "ts-node src/app.ts"
}
```

---

## 4. プロジェクト構成

```bash
mkdir -p src/controllers
touch src/app.ts src/controllers/HelloController.ts
```

> 上記ファイルに API 処理を記述する（内容は省略可）

---

## 5. package.json にスクリプトを追加

```json
"scripts": {
  "dev": "nodemon"
}
```

---

## 6. Docker関連ファイル作成

### ✅ Dockerfile

```Dockerfile
FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]
```

### ✅ docker-compose.yml

```yaml
version: '3.9'
services:
  app:
    build: .
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    command: npm run dev
```

---

## 7. Docker 起動

```bash
docker-compose up --build
```

---

## 8. 動作確認（打鍵）

### ✅ Hello API

```bash
curl http://localhost:3000/api/hello
# → {"message":"Hello, routing-controllers!"}
```

### ✅ Echo API

```bash
curl -X POST http://localhost:3000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"name":"Shiro"}'
# → {"received":{"name":"Shiro"}}
```

---

## ✅ 完了！

この状態で `.ts` ファイルを編集すれば、`nodemon` により即時再起動され、変更が反映されます。
