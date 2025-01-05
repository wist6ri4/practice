import pytest

def add(a, b):
    return a + b

# 正常系のテスト
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# largeのマークが付いているテスト
@pytest.mark.large
def test_add_large():
    assert add (10, 20) == 30

# smallのマークが付いているテスト
@pytest.mark.small
def test_add_small():
    assert add(1, 2) == 3

# 異常系のテスト
def test_add_error():
    with pytest.raises(TypeError):
        add(1, "three")

# クラス化したテスト
class TestAdd:
    def test_add_class(self):
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_add_error_class(self):
        with pytest.raises(TypeError):
            add(1, "three")

# パラメータ化したテスト
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected

# fixtureで事前実行
@pytest.fixture
def add_fixture():
    print("setup")
    return {"a": 2, "b": 3, "expected": 5}

def test_add_fixture(add_fixture):
    assert add(add_fixture["a"], add_fixture["b"]) == add_fixture["expected"]