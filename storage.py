import json
from book import Book
import logging

def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        books = json.loads(text) if text.split() else []
    except FileNotFoundError:
        print("文件不存在")
        logging.error("读失败：文件不存在")
        with open(path, "w") as f:
            print("已新建")
            logging.info("已新建json")
        return []
    except json.JSONDecodeError:
        print("文件损坏")
        logging.error("读失败，文件损坏")
        return []
    else:
        book = []
        for i in books:
            book.append(Book(i["name"], i["author"], i["done"]))
        return book

def save(path, books):
    datas = books
    book = []
    for b in datas:
        data = {}
        data["name"] = b.name
        data["author"] = b.author
        data["done"] = b.done
        book.append(data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False)
    return