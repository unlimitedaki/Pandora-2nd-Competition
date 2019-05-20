# 魔盒挑战第二期赛题

## 考察点

- 网络
    - `POST`，`GET`
    - `HTML` 文档解析
- 命令行操作
    - `Git`
    - `SSH Key`
    - `Scp`
- Python 编程
    - `Flask` 基本使用
    - `PIL` 图片处理
    - `JSON`序列化与反序列化
    - `Base64`、`md5`编码使用
    - 字符串处理
    - 文件操作

## 部署方式

1. 点击页面右上方的`Fork`按钮，创建自己的赛题仓库；

2. 克隆自己的赛题仓库；
```shell
git clone <YOUR_REPO_URL>
cd ./Pandora-2nd-Competition
```

3. 安装 Python 运行依赖（Python >=3.6）；
```shell
python -m pip install -r requirements.txt
```

4. 测试依赖是否安装成功；
```shell
python -m pytest -v
```

如果出现类似以下结果，则说明依赖安装成功：
```
======== 1 passed in xxx seconds ========
```

至此，就可以开始愉快地做题啦！

> **PS: 运行 Flask**
```shell
python -m flask run
```

## 注意事项

- 本项目已经提供的依赖：
> 以下为主要依赖，细节请参考`requirements.txt`
```
Flask==1.0.2            # Web Server Framework
Pillow==6.0.0           # Image Process Lib
requests==2.21.0        # HTTP Request Lib
beautifulsoup4==4.7.1   # HTML Parse Lib
lxml==4.3.3             # XML Parse Lib
pyquery==1.4.0          # HTML Parse Lib
Markdown==3.1           # Markdown Parse
pprint==0.1             # Pretty Print
pytest==4.5.0           # Python Unit Test
```

- 如果需要添加依赖，请在提交到 Github 之前在根目录将依赖冻结：
```shell
python -m pip freeze > requirements.txt
```
