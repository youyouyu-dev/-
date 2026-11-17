from storage import load, save
from book import Book
import pytest

def test_load_save(tmp_path):
    path = tmp_path / "demo.json"
    b = Book("高数", "张三")
    k = Book("英语", "李四")
    bk = [b, k]
    save(path, bk)
    assert load(path)[0].name == "高数"
    assert load(path)[1].name == "英语"

def test_load_notfound(tmp_path):
    assert load(tmp_path / "notfound.json") == []

def test_load_notjson(tmp_path):
    path = tmp_path / "demo.txt"
    with open(path, "w", encoding = "utf-8") as f:
        f.write("不是json")
    with pytest.raises(SystemExit):
        load(path)