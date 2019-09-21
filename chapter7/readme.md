- sublime不能运行 函数input() 的文件  
- 需要运行终端。输入cd进入到文件所在目录  输入命令```ls```显示当前目录文件  
- 输入命令```python3 file_name.py```（要在python3下运行，python2会有问题）

```
终端运行如下
mikasa:~ kangshuaibo$ cd ~/Desktop/My-Python-Learn/Chapter7
mikasa:Chapter7 kangshuaibo$ ls
7.1.1greeter.py			readme.md
7.1函数input()原理.py
mikasa:Chapter7 kangshuaibo$ python3 7.1.1greeter.py
Please enter your name: mikasa
Hello, mikasa!
mikasa:Chapter7 kangshuaibo$ 
```


原因：python2.7中要使用函数raw_input()来处理输入信息，python2.7中的input()是来执行python代码的。没有检测到python代码就会报错。

pyhton3的输入函数就是input()了