// ライブラリのインポート
const CryptoJS = require('crypto-js');
const readline = require('readline');

// readlineインターフェースを作成
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Please enter a value: ', (userInput) => {
    // 入力された値をコンソールに出力
    console.log('You entered: ' + userInput);
    
    // ハッシュ化
    const hash = CryptoJS.SHA256(userInput);

    // ハッシュを16進数文字列に変換
    const result = hash.toString(CryptoJS.enc.Hex);

    // SHA-256ハッシュをコンソールに表示
    console.log(result);
    console.log(hash);

    // インターフェースを閉じる
    rl.close();
});
