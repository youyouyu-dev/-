import sys
from storage import load, save
from book import Book
from pathlib import Path
import logging



def found(books):
    f = False
    for b in books:
        if b.name == sys.argv[2]:
            f = True
            continue
    return f
        

def add(path):
    books = load(path)
    if found(books):
        print("该书已在库")
        logging.warning("该书已在库")
    else:
        newbook = Book(sys.argv[2], sys.argv[3])
        books.append(newbook)
        save(path, books)
        print("已添加")
        logging.info("已添加：%s", newbook)
        return

def delete(path):
    books = load(path)
    if found(books):
        nbooks = []
        for b in books:
            if b.name != sys.argv[2]:
                nbooks.append(b)
        save(path, nbooks)
        print("已删除")
        logging.info("已删除：%s", sys.argv[2])
        return
    else:
        print("没找到")
        logging.warning("没找到")


def done(path):
    books = load(path)
    if found(books):
        for b in books:
            if b.name == sys.argv[2]:
                book = b
        if book.done == False:
            book.make_done()
            save(path, books)
            print("已确认出库")
            logging.info("出库 %s", book)
        else:
            print("该书未在库")
            logging.warning("该书未在库")
    else:
        print("没找到")
        logging.warning("没找到")

def reopen(path):
    books = load(path)
    if found(books):
        for b in books:
            if b.name == sys.argv[2]:
                book = b
        if book.done == True:
            book.reopen()
            save(path, books)
            print("已确认入库")
            logging.info("入库 %s", book)
        else:
            print("该书已在库")
            logging.warning("该书已在库")
    else:
        print("没找到")
        logging.warning("没找到")

def search(path):
    books = load(path)
    found = False
    for b in books:
        if sys.argv[2] in b.name:
            found = True
            print(b)
            break 
    if not found:
        print("没找到")
        logging.warning("没找到")
        return

def show(path):
    books = load(path)
    for b in books:
        print(b)
        logging.info("show")
    return

# 分发
def check(n):
    c = False
    if len(sys.argv) < n:
        print("缺少参数")
        logging.warning("缺少参数")
        return c
    elif len(sys.argv) > n:
        print("命令不合法")
        logging.warning("参数不合法")
        return c
    else:
        c = True
        return c

JSON_PATH = Path(__file__).resolve().parent / "图书管理.json"
def main(path=JSON_PATH):
    logging.basicConfig(
        filename=Path(__file__).resolve().parent / "main.log",
        encoding="utf-8",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        
    )    
    if len(sys.argv) >= 2:
        if sys.argv[1] == "add":
            if check(4):
                add(path)

        elif sys.argv[1] == "delete":
            if check(3):
                delete(path)

        elif sys.argv[1] == "done":
            if check(3):
                done(path)
            

        elif sys.argv[1] == "reopen":
            if check(3):
                reopen(path)

        elif sys.argv[1] == "search":
            if check(3):
                search(path)

        elif sys.argv[1] == "show":
            if check(2):
                show(path)
        else:
            print("命令错误")
            logging.warning("命令错误")
    else:
        print("未输入命令")
        logging.warning("未输入命令")

if __name__ == "__main__":
    main()