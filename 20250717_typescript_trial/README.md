# TypeScript環境構築

## １．Node.jsのインストール
Node.jsをインストールします。以下のリンクからダウンロードしてインストールしてください。
- [Node.js公式サイト](https://nodejs.org/)

## ２．Node.jsのプロジェクト作成
Node.jsがインストールされたら、以下のコマンドを実行して新しいプロジェクトを作成します。
```bash
mkdir typescript_trial
cd typescript_trial
npm init -y
```

## ３．TypeScriptのインストール
Node.jsがインストールされたら、以下のコマンドを実行してTypeScriptをインストールします。
```bash
npm install -g typescript
```

## ４．TypeScriptの初期化
TypeScriptの初期設定を行います。以下のコマンドを実行します
```bash
tsc --init
```

## ５．TypeScriptのコードを書く
`src`ディレクトリを作成し、その中にTypeScriptのファイルを作成します。
```bash
mkdir src
touch src/index.ts
```
次に、`src/index.ts`に以下のコードを追加します。
```typescript
const greeting: string = "Hello, TypeScript!";
console.log(greeting);
```

## ６．TypeScriptのコンパイル
TypeScriptのコードをJavaScriptにコンパイルします。以下のコマンドを実行します。
```bash
tsc
```

## ７．JavaScriptの実行
コンパイルされたJavaScriptファイルを実行します。以下のコマンドを
実行します。
```bash
node dist/index.js
```

## ８．TypeScriptの開発サーバーのセットアップ
開発中に自動でコンパイルを行うために、`ts-node`と`nodemon`をインストールします。
```bash
npm install --save-dev ts-node nodemon
```
次に、`package.json`に以下のスクリプトを追加します。
```json
"scripts": {
  "start": "nodemon --exec ts-node src/index.ts"
}
```

## ９．開発サーバーの起動
以下のコマンドを実行して開発サーバーを起動します。
```bash
npm start
```
これで、`src/index.ts`の変更が自動的にコンパイルされ、実行されます。

## １０．TypeScriptの型定義ファイルのインストール
外部ライブラリを使用する場合は、型定義ファイルをインストールする必要があります。以下のコマンドで型定義ファイルをインストールします。
```bash
npm install --save-dev @types/node
```
これで、Node.jsの型定義がプロジェクトに追加されます。

## １１．TypeScriptのLintツールのセットアップ
TypeScriptのコード品質を保つために、ESLintをセットアップします。以下のコマンドを実行します。
```bash
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin
```
次に、ESLintの設定ファイルを作成します。
```bash
npx eslint --init
```
設定の際に、以下のオプションを選択します。
- How would you like to use ESLint? → To check syntax, find problems, and enforce code style
- What type of modules does your project use? → JavaScript modules (import/export)
- Which framework does your project use? → None of these
- Does your project use TypeScript? → Yes
- Where does your code run? → Node
- What format do you want your config file to be in? → JSON
次に、`package.json`に以下のスクリプトを追加します。
```json
"scripts": {
  "lint": "eslint . --ext .ts"
}
```
## １２．ESLintの実行
以下のコマンドを実行して、ESLintを実行します。
```bash
npm run lint
```

これで、TypeScriptのコードがESLintによってチェックされます。

