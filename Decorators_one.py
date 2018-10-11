#coding=utf-8

############learn Decorators##############

#函数可以传递 ，函数可以嵌套函数 ， 函数可以返回函数 ，函数可以作为参数传给另一个函数
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def decorated(*args,**kwargs):
        if not can_run:
            return '函数不能运行'
        return a_func(*args,**kwargs)
    return decorated


@a_new_decorator
def a_functiong_requiring_decoration():
    "被装饰函数"
    print '正在执行函数'
can_run=True
#等价于：a_functiong_requiring_decoration=a_new_decorator(a_functiong_requiring_decoration)
print a_functiong_requiring_decoration()