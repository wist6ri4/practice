# 辞書定義
data = {
    'key1': 'value1',
    'key2': 'value2',
    'key_test1': True,
    'key_test2': False,
    'key_test3': True,
}

# 条件に基づき数字を抽出
result = [
    int(key.replace('key_test',''))
    for key, value in data.items()
    if key.startswith('key_test') and value is True
]

print(result) # [1, 3]