import sys
from storage import load, save
from book import Book
from pathlib import Path
import logging

logging.basicConfig(
    filename=Path(__file__).resolve().parent / "main.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    
)

def add(path):
    books = load(path)
    found = False
    for b in books:
        if b.name == sys.argv[2]:
            found = True
            print("该书已在库")
            break
    if not found:
        newbook = Book(sys.argv[2], sys.argv[3])
        books.append(newbook)
        save(path, books)
        print("已添加")
        logging.info("已添加：%s", newbook)
        return

def delete(path):
    books = load(path)
    found = False
    for b in books:
        if b.name == sys.argv[2]:
            found = True
            break
    if found:
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
        return
    
def find_book(books, name):
    for b in books:
        if b.name == name:
            return b
    return None

def done(path):
    books = load(path)
    b = find_book(books, sys.argv[2])
    if b is None:
        print("没找到")
        logging.warning("没找到")
        return
    elif b.done == False:
        b.make_done()
        save(path, books)
        print("已确认出库")
        logging.info("出库 %s", b)
        return
    else:
        print("该书已被借走")
        return

def reopen(path):
    books = load(path)
    b = find_book(books, sys.argv[2])
    if b is None:
        print("没找到")
        logging.warning("没找到")
        return
    elif b.done == True:
        b.reopen()
        save(path, books)
        print("已确认入库")
        logging.info("入库 %s", b)
        return
    else:
        print("该书已在库")
        return

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

def main():
    json_ = Path(__file__).resolve().parent / "图书管理.json"
    if len(sys.argv) >= 2:
        if sys.argv[1] == "add":
            if len(sys.argv) == 4:
                add(json_)
            elif len(sys.argv) < 4:
                print("缺少参数")
                logging.warning("缺少参数")
            else:
                print("参数不合法")
                logging.warning("参数不合法")

        elif sys.argv[1] == "delete":
            if len(sys.argv) == 3:
                delete(json_)
            elif len(sys.argv) < 3:
                print("缺少参数")
                logging.warning("缺少参数")
            else:
                print("参数不合法")
                logging.warning("参数不合法")

        elif sys.argv[1] == "done":
            if len(sys.argv) == 3:
                done(json_)
            elif len(sys.argv) < 3:
                print("缺少参数")
                logging.warning("缺少参数")
            else:
                print("参数不合法") 
                logging.warning("参数不合法")        

        elif sys.argv[1] == "reopen":
            if len(sys.argv) == 3:
                reopen(json_)
            elif len(sys.argv) < 3:
                print("缺少参数")
                logging.warning("缺少参数")
            else:
                print("参数不合法") 
                logging.warning("参数不合法")

        elif sys.argv[1] == "search":
            if len(sys.argv) == 3:
                search(json_)
            elif len(sys.argv) < 3:
                print("缺少参数")
                logging.warning("缺少参数")
            else:
                print("参数不合法") 
                logging.warning("参数不合法")

        elif sys.argv[1] == "show":
            if len(sys.argv) == 2:
                show(json_)
            else:
                print("命令不合法")
                logging.warning("命令不合法")
        else:
            print("命令错误")
            logging.warning("命令错误")
    else:
        print("未输入命令")
        logging.warning("未输入命令")

if __name__ == "__main__":
    main()