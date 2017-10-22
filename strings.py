# Python 也有多种方式处理字符串，字符串可以被包裹在单引号('...')中或者双引号("...")中，斜线\可以被用来转移引号
# 1.单引号
print('single quotes');
# 2.双引号 
print("double quotes"); 

# 3.引号内嵌套引号
# 注：引号之间只能嵌套与外层不同的引号
print("'single quotes', hello,world");
print('"double quotes", hello,world');
# 如想嵌套相同引号，则需使用 \ 进行转义
print("\"double quotes\", hello,world");

# 4.特殊字符
# \n 是换行符，其后面的字符串将在新的一行展示
print('First line.\nSecond line.');
# 有时也会遇到意外，例如
print('C:\some\name'); #打印结果如下
# C:\some
# ame
# 如果你不想加了前缀 \ 的字符被解释为特殊字符，可以在字符串的第一个字符之前加一个 r ，表示原始字符串
print(r'C:\some\name');

# 5.字符串文本可以多行展示

# 一种方式是使用三层引号("""...""") or ('''...''');
# 注：换行符内，产生空行也将会占用一行，所以我们有必要使用 \ 字符来避免空的行
print("""\
\
	hello, world,
	hello, Python""");

# 6.字符串可以使用 + 进行拼接，也可以使用 * 来表示字符串的重复次数
# 例如：一个字符串出现3次'un'，紧跟一个字符串 'ium'
print(3 * 'un' + 'ium');

# 7.多个字符串排列展示，后面的字符串自动拼接
print('Py''thon');

# 8.字符串的枚举
str1 = 'Python';
print(str1[0],str1[2]);
# 令人意外的是，也可以使用负数进行枚举字符串，其顺序是从右往左，与正数索引相反
# 注：-0 跟 0 的索引的是同一个值，负数枚举的其实下标是 -1 
print(str1[-1]);
print(str1[-3]);

# 9.字符串的截取（切片）
str2 = 'hello, world';
# 对字符串str2从下标0开始，截取2个字符
print(str2[0:2]); # 冒号前面表示截取的起始下标，后面表示截取长度
# 注：当下标为空时，默认为0，当截取长度为空时，截取长度将 = 符串的长度 - 截取下标
print(str2[2:]);
print(str2[:2]);
# 当下标为负数，截取个数为空，截取长度 = |-3|（下标的绝对值）
print(str2[-3:]);

# 10.字符串是不可变的
# str2[1] = 'P'; # TypeError: 'str' object does not support item assignment
# 如果想要改变一个字符串，则必须创建新的字符串
str3 = 'T' + str2[2:];
print(str3);

# 11.内置函数len()，返回字符串长度
print(len(str3));