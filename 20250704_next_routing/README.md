# 環境構築手順
# １．next.jsプロジェクトの作成
```bash
npx create-next-app@latest
```

以降、対話形式でプロジェクト名やテンプレートの選択を行う。
```bash
√ What is your project named? ... testapp
√ Would you like to use TypeScript? ... No / Yes
√ Would you like to use ESLint? ... No / Yes
√ Would you like to use Tailwind CSS? ... No / Yes
√ Would you like your code inside a `src/` directory? ... No / Yes
√ Would you like to use App Router? (recommended) ... No / Yes
√ Would you like to use Turbopack for `next dev`? ... No / Yes
√ Would you like to customize the import alias (`@/*` by default)? ... No / Yes
Creating a new Next.js app in E:\ユーザー\ドキュメント\VSCode\practice\20250704_next_routing\testapp.
```

# ２．ポートの変更
デフォルトではポート3000で起動するが、ポートを変更したい場合は、`package.json`の`scripts`セクションを編集する。
```json
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
```
例えば、ポート4000に変更する場合は以下のようにする。
```json
  "scripts": {
    "dev": "next dev --turbopack -p 4000",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
```