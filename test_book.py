from book import Book
import pytest

def test_1_book():
    b = Book("高数", "张三")
    assert b.name == "高数"
    assert b.author == "张三"
    assert b.done == False

def test_2_book():
    b = Book("高数", "张三")
    b.make_done()
    assert b.done == True

def test_3_book():
    b = Book("高数", "张三")
    assert str(b) == "书名《高数》作者 张三 未借出"
    b.make_done()
    assert str(b) == "书名《高数》作者 张三 已借出"
    b.reopen()
    assert str(b) == "书名《高数》作者 张三 未借出"

def test_empty_content():
    with pytest.raises(ValueError):
        Book("", "张三")
    with pytest.raises(ValueError):
        Book("高数", "")