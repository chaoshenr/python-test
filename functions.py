# 函数 function 的学习
# 1.关键字 def
def sayHello():
	print('Hello, Python\'s function');

sayHello();
print(sayHello());# 当不给函数指定返回值时，函数默认返回 None

# 2.函数参数默认值
def defaultArgValues(prompt, retries = 4, reminder = 'please try again'):
	while True:
		inputValue = input(prompt);
		if inputValue in ('y', 'ye', 'yes'):
			return True;
		if inputValue in ('n', 'no'):
			return False;
		retries = retries - 1;
		if retries < 0:
			raise ValueError('invalid user response');
		print(reminder);
# 其中包含了一个语法 in ，即对一个序列中是进行否包含判断
print(defaultArgValues('Do you really want to quit?'));

# 默认值是根据函数在作用域中被定义的位置所决定的，如下
i_val = 5

def defValue(val = i_val):
	print(val)

i_val = 7

defValue(); # result 5

# 注：参数默认值只被初始化一次，如果默认值参数是，可变的对象，如list、dictionary和大多数类的实例，如果发生连续多次调用，默认值参数将会产生差异。
def def_diff(a, L = []):
	L.append(a);
	return L;
print(def_diff(1));
print(def_diff(2));
print(def_diff(3));
# 打印结果如下：
# [1]
# [1, 2]
# [1, 2, 3]
# 这是因为，默认值对象会跟函数存在绑定关系，三个连续调用函数，操作的其实是同一个对象，即默认值对象会被相同的函数共享。
# 那么怎么共享呢？如下：
def noDe_diff(a, L=None):
	if L == None:
		L = [];
	L.append(a);
	return L;
print(noDe_diff(1));
print(noDe_diff(2));
print(noDe_diff(3));

