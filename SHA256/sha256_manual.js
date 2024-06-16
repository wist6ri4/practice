// ライブラリのインポート
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
    const result = encrypt(userInput);

    // SHA-256ハッシュをコンソールに表示
    console.log(result);

    // インターフェースを閉じる
    rl.close();
});

function encrypt() {

};