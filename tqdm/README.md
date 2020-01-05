# tqdm

`tqdm`在阿拉伯语中的意思是“进展”，是一个快速、扩展性强的进度条工具库，用户只需要封装任意的迭代器 `tqdm(iterator)`。

### 用法

最主要的用法有3种，自动控制、手动控制或者用于脚本或命令行。
详细资料见GitHub： https://github.com/tqdm/tqdm

---

##### **【例子】实时显示下载进度**

这里要用到``urllib.request`模块中的`urlretrieve()``方法。

```python
urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)
```

`filename`以此文件名保存在当前文件夹中，如果未提供此参数，则生成临时文件。

`filename`以此文件名保存在当前文件夹中，如果未提供此参数，则生成临时文件。

如果存在``reporthook`，即钩子函数 / 回调函数。钩子函数将在建立网络连接时调用一次，之后每次读取块后调用一次。

该钩子将传递三个参数，到目前为止传输的块的数量，以字节为单位的块大小以及文件的总大小。

```python
from urllib.request import urlretrieve
from tqdm import tqdm

class TqdmUpTo(tqdm):
    # Provides `update_to(n)` which uses `tqdm.update(delta_n)`.

    last_block = 0
    def update_to(self, block_num=1, block_size=1, total_size=None):
        '''
        block_num  : int, optional
            到目前为止传输的块 [default: 1].
        block_size : int, optional
            每个块的大小 (in tqdm units) [default: 1].
        total_size : int, optional
            文件总大小 (in tqdm units). 如果[default: None]保持不变.
        '''
        if total_size is not None:
            self.total = total_size
        self.update((block_num - self.last_block) * block_size)  
        self.last_block = block_num

eg_link = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
file = eg_link.split('/')[-1]
with TqdmUpTo(unit='B', unit_scale=True, unit_divisor=1024, miniters=1,
              desc=file) as t:  # 继承至tqdm父类的初始化参数
    urlretrieve(eg_link, filename=file, reporthook=t.update_to, data=None)
```

##### 【例子】实时显示解压进度

针对`zip`文件的解压缩使用`zipfile.ZipFile()`方法，但是`ZipFile()`方法不支持回调函数，只能考虑逐文件解压，将`tqdm()`包装到迭代器上。

可以用`ZipFile.namelist()`返回整个压缩文件的名字列表，然后逐个解压。

```python
if not isdir('dir_path'):
    with ZipFile('imgs.zip', 'r') as zipf:   
        for name in tqdm(zipf.namelist()[:1000],desc='Extract files', unit='files'):
            zipf.extract(name, path='dir_path')
        zipf.close()
```

逐文件解压会增加解压时间：
同样解压10000张图片，``zipf.extractall()``方法耗时 8.81s；上述方法耗时 9.86s，多花时间 12%。
