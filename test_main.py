from main import found, add, delete, done, reopen, search, show, check, main
from book import Book
import sys
import pytest


def test_found(monkeypatch):
    b = Book("高数", "张三")
    k = Book("英语", "李四")
    books = [b, k]

    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数"])
    assert found(books) is True
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "概论论"])
    assert found(books) is False

def test_add(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数", "张三"])
    path = tmp_path / "demo.json"
    add(path)
    assert "已添加" in capsys.readouterr().out
    add(path)
    assert "该书已在库" in capsys.readouterr().out

def test_delete(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数", "张三"])
    path = tmp_path / "demo.json"
    add(path)
    monkeypatch.setattr(sys, "argv", ["main.py", "delete", "高数"])
    delete(path)
    assert "已删除" in capsys.readouterr().out
    delete(path)
    assert "没找到" in capsys.readouterr().out

def test_done(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数", "张三"])
    path = tmp_path / "demo.json"
    add(path)
    monkeypatch.setattr(sys, "argv", ["main.py", "done", "高数"])
    done(path)
    assert "已确认出库" in capsys.readouterr().out
    done(path)
    assert "该书未在库" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["main.py", "done", "2"])
    done(path)
    assert "没找到" in capsys.readouterr().out

def test_reopen(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数", "张三"])
    path = tmp_path / "demo.json"
    add(path)
    monkeypatch.setattr(sys, "argv", ["main.py", "reopen", "高数"])
    reopen(path)
    assert "该书已在库" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["main.py", "done", "高数"])
    done(path)
    monkeypatch.setattr(sys, "argv", ["main.py", "reopen", "高数"])
    reopen(path)
    assert "已确认入库" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["main.py", "reopen", "1"])
    reopen(path)
    assert "没找到" in capsys.readouterr().out

def test_search(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数", "张三"])
    path = tmp_path / "demo.json"
    add(path)
    monkeypatch.setattr(sys, "argv", ["main.py", "search", "高数"])
    search(path)
    assert "书名《高数》作者 张三 未借出" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["main.py", "search", "1"])
    search(path)
    assert "没找到" in capsys.readouterr().out
    
def test_check(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数"])
    check(4)
    assert "缺少参数" in capsys.readouterr().out
    check(2)
    assert "命令不合法" in capsys.readouterr().out

def test_show(monkeypatch, tmp_path, capsys):
    path = tmp_path / "demo.json"
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数", "张三"])
    add(path)
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "概论论", "李四"])
    add(path)
    monkeypatch.setattr(sys, "argv", ["main.py", "show"])
    show(path)
    out = capsys.readouterr().out
    assert "书名《高数》作者 张三 未借出" in out
    assert "书名《概论论》作者 李四 未借出" in out

def test_main(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "高数", "张三"])
    main(tmp_path / "demo.json")
    assert "已添加" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["main.py"])
    main(tmp_path / "demo.json")
    assert "未输入命令" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["main.py", "111"])
    main(tmp_path / "demo.json")
    assert "命令错误" in capsys.readouterr().out