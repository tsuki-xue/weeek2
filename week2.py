##标识符
#第一个字符必须是字母表中字母或下划线 _ 。
#标识符的其他的部分由字母、数字和下划线组成。
#标识符对大小写敏感。
#在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

##保留字
'''Python 有一些保留字，不能用作标识符。
#以下是 Python 3.6.5 版本的保留字：
#False      class      finally    is         return
#None       continue   for        lambda     try
#True       def        from       nonlocal   while
#and        del        global     not        with
#as         elif       if         or         yield
#assert     else       import     pass
#break      except     in         raise
#class      exec       is         return
#continue   finally    lambda     try'''
#第一个注释 是单行注释，第二个注释是多行注释。
#第二个注释  多行注释可以用多个 # 号，还有 ''' 和 """：
'''
第三注释
第四注释
'''
"""
第五注释
第六注释
"""
print ("Hello, Python!")

##行与缩进
#python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
#Python的缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print ("True")
else:
    print ("False")
#错误示例
'''if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误'''

#多行语句
#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句，例如：
'''total = item_one + \
        item_two + \
        item_three
print (total)'''
#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \，例如：total = ['item_one', 'item_two', 'item_three','item_four', 'item_five']

#数字类型
'''Python 支持四种数字类型：整数、布尔型、浮点数和复数。
#整数类型：整数类型可以没有小数部分，例如：1、100、-3、0。
#布尔型类型：布尔型只有 True 和 False 两种值，可以用 and、or 和 not 运算符进行逻辑运算。
#浮点数类型：浮点数类型用来表示小数，例如：3.14、-9.01。
#复数类型：复数类型可以用 a + bj 表示，j 表示虚数单位。'''

#字符串String
''' Python 中单引号和双引号都可以用来表示字符串，三引号可以指定多行字符串。
反斜杠 \ 可以转义特殊字符。
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。 如 r"this is a line with \n" 则 \n 会显示，并不是换行
按字面意义级联字符串，如 "this " "is " "string" 会被自动转换为 this is string。
字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
'''

#输出两个print语句会换行，如果想在同一行输出，可以加end=""。
print("Hello, Python!")
print("Hello, Python!")

print("Hello, Python!", end="")
print("Hello, Python!")