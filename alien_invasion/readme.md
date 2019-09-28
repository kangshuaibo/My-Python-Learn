#错误产生环境：macOS MOjave. 
 ```
 官网
 https://conda.io/docs/user-guide/install/macos.html
 ```
- 1.安装Miniconda虚拟环境运行pygame，下面详解第二个方案.
 
- 2.安装Miniconda - 在您的终端窗口中，运行下载的sh
```bash Miniconda3-latest-MacOSX-x86_64.sh```


- 3.关闭终端重新打开，输入以下内容，验证conda是否已在系统上安装并运行：conda --version. 

- 4.创建一个名为“snakes”的新环境，其中包含Python 3.7
```conda create --name snakes python=3.7```

-5. 查看是否创建成功. 
```conda info --envs```. 

- 激活新环境: source activate +环境名
  ```source activate snakes```. 
  
#提示找不到pygame，因为虚拟环境是新的，所以没有这个模块

- pip安装pygame.    
```pip install pygame```


- 在这个虚拟环境中运行python

```
(snakes) mikasa:~ kangshuaibo$ cd ~/Desktop/My-Python-Learn/

(snakes) mikasa:My-Python-Learn kangshuaibo$ cd alien_invasion

(snakes) mikasa:alien_invasion kangshuaibo$ python3 alien_invasion.py
```


#基本操作
```
# 要查看所有环境的列表
conda info --envs
 
# 创建一个名为“snakes”的新环境，其中包含Python 3.5
conda create --name snakes python=3.5
 
# 激活某个环境
source activate snakes
conda activate snakes
 
# 停用snakes环境并返回基础环境
source deactivate
conda deactivate snakes
 
# 删除某个环境conda env remove -n 环境名称
conda env remove -n snakes

```

#mac安装了conda后，前面会有一个(base)，很烦人，终于找到最佳解决方案了：
```
$ conda config --set auto_activate_base false
```

原因：

安装conda后，每次启动终端，都会自动启动conda的base环境，conda的环境可以用 conda env list 查看

只要设置conda不要自动启动base环境就可以了。
