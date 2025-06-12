[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# 介绍

- algo-api-demo

- 使用fastapi快速开发算法接口模板

    - 以实现关键词提取接口为例 


# 项目名称修改

- 执行下列命令

```
./rename_project.sh <old_name> <new_name>
```

主要实现在下面文件中修改名称：
- `run_app.sh`中修改`Algo_Backend`
- `stop_app.sh`中修改`Algo_Backend`
- `gunncorn.py`中修改`Algo_Banckend`
- `app/main.py`中修改`Algo_Banckend`



# 环境配置

```
conda create -n algo-api python=3.8

conda activate algo-api

pip install -r requirements.txt

```


# 程序运行

- 激活环境

```
conda activate algo-api
```

- 调试程序（debug 8207端口、单线程）

```
bash debug_app.sh
```

- 后台启动程序 (run 8206端口、多线程)

```
bash run_app.sh
```

- 关闭后台程序 (stop)

```
bash stop_app.sh
```

# Git使用

- Merge Request 分支合并请求 [参考](https://juejin.cn/post/7028965736022278175)



# Pytest 测试举例


- test_algo.py所有用例

```
pytest -v -s test_algo.py
```

- 测试test_algo.py里面的`test_keywords_textrank`方法

```
pytest -v -s test_algo.py::test_keywords_textrank
```

# 前端测试

- `http://ip:8207/docs`
- `http://ip:8207/redoc`



# 书写流程

- 定义输入类(eg:`KeywordsInputBase`)
- 定义输出类(eg:`KeywordsOutputBase`)
- 书写接口(eg:`def fetch_keywords`)
- 交互页面测试(eg:`http://ip:8207/docs`)
- 书写接口测试案例(eg:`test_algo.py->test_keywords_textrank`)


# 参考
- 官方教程 [官方](https://fastapi.tiangolo.com/tutorial/), 可以解决99%的问题

- Black Formatter 代码格式化工具 [官方](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) [说明](https://muzing.top/posts/a29e4743/#the-black-code-style)
- pytest的初步使用 [参考](https://www.cnblogs.com/hiyong/tag/pytest/)