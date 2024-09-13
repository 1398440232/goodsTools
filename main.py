from dbapi import dbprocess


class tools():
    def __init__(self) -> None:
        self.db = dbprocess()
        self.connection = self.db.dbconnect()
        self.db.adddata(self.connection,'螺类','田螺肉', 125,'4包*4斤（黄色）', '无',125, '无')
    
    

