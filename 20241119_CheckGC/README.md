# 概要
GCの挙動確認

# 実行コマンド
## javaの実行
```
javac HeapTest1.java
java -Xms100 -Xms100 HeapTest1
```

## 現在のアプリケーションのプロセスを確認
```
jps
```

## jstatで統計取得
第1引数はjpsで確認したID
```
jstat -gcutil -h5 40408 1000 > jstat_HeapTest2.tsv
```
