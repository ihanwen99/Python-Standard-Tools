import os

# 操作系统的名字
print(os.name)
print(os.environ)

# 获取某个环境变量的值
print(os.getenv('PATH'))

# 当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下新建目录
# 首先把新目录的完整路径表示出来
newpath = os.path.join(os.path.abspath('.'), 'newdir')
print(newpath)
# 然后创建一个目录
if not os.path.exists(newpath):
    os.mkdir(newpath)
# 删掉一个目录
os.rmdir(newpath)

# 注意，将两个路径合成一个时，不要直接拼接字符串，而是要通过 os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

# 因为在windows下，os.path.join()返回这样的路径：
# part1\part2

# 而在linux unix mac os 下返回这样的字符串：
# part1/part2

# 同样，拆分路径时也不要直接拆分字符串，而是通过 os.path.split() 函数，这样可以把一个路径拆分为两部分：
# 最后一部分总是最后级别的目录名或是文件名
print(os.path.split('filePath\\filename.txt'))
# ('filePath', 'filename.txt')

# 获取文件扩展名
print(os.path.splitext('filePath\\filename.exe'))
# ('filePath\\filename', '.exe')

# 这些合并、拆分文件路径的函数并不要求文件真实存在，仅仅是对字符串的操作而已
# 下面的代码假设当前路径下 os.path.abspath('.'), 存在'test_os.txt'文件

# 文件重命名
# os.rename('test_os.txt', 'os.py')

# 移动文件
# os.rename('os.py', os.path.join(os.path.abspath('.'), 'learnOS\\os_test.txt'))

# 当前工作路径
print(os.getcwd())

# 相对路径
print(os.curdir)

# 改变当前路径
os.chdir('./learnOS')
print(os.getcwd())
print(os.curdir)
os.chdir('..')
print(os.getcwd())

# 删除文件
# os.remove('os_test.txt')

# 列出当前目录下所有子目录、所有文件、所有py文件
print(os.listdir('.'))
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

