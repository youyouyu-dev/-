这是一个用命令行管理的图书小工具，数据存在“图书管理.json”

需要Python3.6以上， 不需要安装任何依赖

命令列表

add：添加书   add 书名 作者
delete：删除书   delete 书名
done：借书   done 书名
reopen：还书   reopen 书名
search：查找书   search 书名
show：展示所有书   show


示例

python main.py add 高数 张三
已添加
python main.py add 高数 张三
该书已在库
python main.py add 高 数 张 三
命令不合法
python main.py add "高 数" "张 三"
已添加
python main.py delete "高 数"
已删除
python main.py delete "高 数"
没找到
python main.py done 高数
已确认出库
python main.py done 高数
该书未在库
python main.py done "高 数"
没找到
python main.py reopen 高数
已确认入库
python main.py reopen 高数
该书已在库
python main.py reopen "高 数"
没找到
python main.py search 高数
书名《高数》作者 张三 未借出
python main.py search "高 数"
没找到
python main.py add 英语 李四
已添加
python main.py show
书名《高数》作者 张三 未借出
书名《英语》作者 李四 未借出