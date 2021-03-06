# 私有权限的作用：
# 不想让一些属性或者方法继承给子类而设置的权限

# 故事：
# 小李老了，想把自己的技术全部传授给小小李，但是不想把自己的10个亿资产传给小小李，选择了捐赠。

# 设置私有权限的方法：
# 在属性和方法名前加两个下划线: __

class Master(object):
    def __init__(self):
        self.gongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'用{self.gongfu}制作煎饼果子')

class Apprentice(Master):
    def __init__(self):
        self.gongfu = '[秘制煎饼果子配方]'
        # self.money = 1000000000
        # 定义一个私有属性
        self.__money = 1000000000

    # 定义一个私有方法
    def __print_info(self):
        print('这是私有方法')

    def make_cake(self):
        print(f'用{self.gongfu}制作煎饼果子')

class Tusun(Apprentice):
    pass

# 验证
xiaoxiaoli = Tusun()
# print(xiaoxiaoli.__money) # 报错
# xiaoxiaoli.__print_info() # 报错
