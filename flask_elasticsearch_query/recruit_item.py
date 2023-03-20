# 定义一个数据结构recruit_info
class recruit_info:
    # 初始化方法，接受title，url，date三个参数
    def __init__(self, title, url, date):
        # 将参数赋值给实例属性
        self.title = title
        self.url = url
        self.date = date
    
    # 定义一个方法，返回title属性的值
    def get_title(self):
        return self.title
    
    # 定义一个方法，返回url属性的值
    def get_url(self):
        return self.url
    
    # 定义一个方法，返回date属性的值
    def get_date(self):
        return self.date
