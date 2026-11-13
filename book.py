class Book:

    def __init__(self, name, author, done=False):
        if not name:
            raise ValueError("书名不能为空")
        if not author:
            raise ValueError("作者不能为空")
        self.name = name
        self.author = author
        self._done = done

    def make_done(self):
        self._done = True
    def reopen(self):
        self._done = False

    @property
    def done(self):
        return self._done

    def __str__(self):
        if self._done:
            return f"书名《{self.name}》作者 {self.author} 已借出"
        else:
            return f"书名《{self.name}》作者 {self.author} 未借出"