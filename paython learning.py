def fact(n):   #这是个递归函数
    if n==1:
        return 1
    return n * fact(n - 1)
	

L[0:3] #提前L里的前三个元素
L[:3]  #0可以省略
L[-2:] #从倒数第二个开始取


#列表生成式
[x * x for x in range(1, 11)]
#[1,3,9....100]

#还可以在列表生成式里加入筛选条件
[x * x for x in range(1, 11) if x % 2 == 0]

#两个循环嵌套在一起，形成全排列
[m + n for m in 'ABC' for n in 'XYZ']

f=abs
def add(x, y, f):  #f是一个函数，可以当作参数传人，高阶函数
    return f(x) + f(y)
	
#map和reduce	
map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])  #分别计算每一个分f（）
reduce(add, [1, 3, 5, 7, 9])  #先计算1+3，再计算（1+3）+5。。分开计算


 def fn(x, y):
     return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9])   #把13579变成一个数

def is_odd(n):      
    return n % 2 == 1

filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])   #用fillter过滤掉偶数

sorted([36, 5, 12, 9, 21]) #sorted可以对直接对list排序

map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])#lambda是匿名函数，表明了函数运行规则

int('12345', base=8)  #进行8进制转换


#面向对象的编程，类

class Student(object):  #类名，（从哪个类继承下来的）
bart = Student()  #创建一个类bart，是student类的
bart.name = 'Bart Simpson' #给类赋值

class Student(object):       #通过__init__(self,x,y),强制的给类绑定属性 #第一个参数永远是实例变量self

    def __init__(self, name, score):
        self.name = name
        self.score = score
	def print_score(self):   #直接在类的内部通过内部构造打印姓名-成绩的函数
        print '%s: %s' % (self.name, self.score)
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)  #直接传参数进去，直接就能识别
bart.print_score()  #直接实现打印姓名和成绩



class Student(object):

    def __init__(self, name, score):
        self.__name = name     #将name改成私有变量（前面加__）
        self.__score = score   #将score改成私有变量（前面加__）

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):       #私有化后，想要访问，需要加新方法
        return self.__name

    def get_score(self):
        return self.__score
		
    def set_score(self, score):  #弄一个输入检测装置，防止输入没有意义的数字
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

