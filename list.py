# 列表 or 数组
squares = [1, 3, 7, 9, 11];

# 1.索引
print(squares[2]);
print(squares[-1]);

# 2.切片
# (1)简单的使用
print(squares[1:]);
print(squares[:-1]);
# (2)替换数组元素
squares[1:3] = [45,23,56];
print(squares);
# (3)删除数组元素
squares[1:3] = [];
print(squares);
# (4)清空数组
arr = [1,2,3,4];
arr[:] = []; # or arr = []
print('arr',arr);


# 3.类字符串的添加
print(squares + [10, 23]);

# 4.List.append 追加元素
cubes = [1, 8, 27];
cubes.append(64);
print(cubes);

# 练习
# 斐波那契数列
def fibonacci(num):
	indexNum = 0;
	nextIndexNum = 1;
	arr = [];
	while nextIndexNum <= num:
		arr.append(nextIndexNum);
		indexNum, nextIndexNum = nextIndexNum, indexNum + nextIndexNum;
	return arr;
print(fibonacci(23));

