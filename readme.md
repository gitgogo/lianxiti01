# python基础题
1. 迭代器和生成器的区别
2. 列表和元组的区别
3. python中一切皆对象
4. python中的内存管理
5. python中多线程如何实现
6. GIL锁
7. 深拷贝和浅拷贝
8. lambda函数是什么
9. 删除List中的重复元素
10. 正则模块re中match和search的区别
11. python中如何实现单例模式
12. 取两个List的差集、交集
13. python中实现socket编程
14. python中文件的操作
15. 一行代码实现1-100之和
16. new和init函数的区别；name、file、class内置方法
17. python中with的用法
18. python中map、reduce、filter方法的使用
```python
from functools import reduce
# 1-100求和
reduce(lambda x,y: x+y, range(1,101))
# 1-100中的奇数
filter(lambda x: x%2, range(1,101))
[x for x in range(1,101) if x%2]
# 1-100每个数2次方输出
map(lambda x: x**2, range(1,101))
# 展开二维数组 e=[[1,2],[3,4],[5,6]]
[i for j in e for i in j]
```
1. 