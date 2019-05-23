from flask import Flask,render_template,request
import base64
from io import BytesIO
import json
import hashlib
from flask import jsonify
import PIL
from PIL import Image
import urllib
import re
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        """
        只有 Hello World 的首页
        :return:
        """
        return "Hello, world!"

    # TODO: 捕获 404 错误，返回 404.html
    @app.errorhandler(404)
    def page_not_found(error):
        """
        以此项目中的404.html作为此Web Server工作时的404错误页
        """
        return render_template("404.html"),404


    # TODO: 完成接受 HTTP_URL 的 picture_reshape
    # TODO: 完成接受相对路径的 picture_reshape
    @app.route('/pic', methods=['GET'])
    def picture_reshape():
        """
        **请使用 PIL 进行本函数的编写**
        获取请求的 query_string 中携带的 b64_url 值
        从 b64_url 下载一张图片的 base64 编码，reshape 转为 100*100，并开启抗锯齿（ANTIALIAS）
        对 reshape 后的图片分别使用 base64 与 md5 进行编码，以 JSON 格式返回，参数与返回格式如下
        
        :param: b64_url: 
            本题的 b64_url 以 arguments 的形式给出，可能会出现两种输入
            1. 一个 HTTP URL，指向一张 PNG 图片的 base64 编码结果
            2. 一个 TXT 文本文件的文件名，该 TXT 文本文件包含一张 PNG 图片的 base64 编码结果
                此 TXT 需要通过 SSH 从服务器中获取，并下载到`pandora`文件夹下，具体请参考挑战说明
        
        :return: JSON
        {
            "md5": <图片reshape后的md5编码: str>,
            "base64_picture": <图片reshape后的base64编码: str>
        }
        """

        argu = request.args.get('b64_url')
        if argu.find('.txt')!= -1:
            f = open("pandora\\"+argu,'r',encoding = 'utf-8')
            data = f.read()
        else:
            response = urllib.request.urlopen(argu)
            datab = response.read()    
            data = datab.decode('utf-8')

        
        result = base64.b64decode(data)
        im = Image.open(BytesIO(result))
        im = im.resize((100, 100), Image.ANTIALIAS)
        output_buffer = BytesIO()
        im.save(output_buffer, format='png')
        bs = output_buffer.getvalue()

        b64e = base64.encodebytes(bs)
        md5 = hashlib.md5(bs).hexdigest()
        result = {}
        result['md5'] = md5
        result['base64_picture'] = b64e.decode('utf-8').replace('\n', '')
        return jsonify(result)


    # TODO: 爬取 996.icu Repo，获取企业名单
    @app.route('/996')
    def company_996():
        """
        从 github.com/996icu/996.ICU 项目中获取所有的已确认是996的公司名单，并

        :return: 以 JSON List 的格式返回，格式如下
        [{
            "city": <city_name 城市名称>,
            "company": <company_name 公司名称>,
            "exposure_time": <exposure_time 曝光时间>,
            "description": <description 描述>
        }, ...]
        """
        response = urllib.request.urlopen('https://github.com/996icu/996.ICU/blob/master/blacklist/README.md')   
        data = response.read().decode('utf-8')
        re_table = '<tr>\n<td.+>(.+)</td>\n<td.+>(.+)</td>\n<td.+>(.+)</td>\n<td.+>(.+)</td>\n.+\n</tr>'
        re_cmp = re.compile(re_table)
        result = re_cmp.findall(data)
        res = []
        for r in result:
            res.append({
                'city':r[0],
                'company':r[1].split('</a>')[0],
                'exposure_time':r[2],
                'description':r[3]
            })
        app.config['JSON_AS_ASCII'] = False
        return jsonify(res)
    return app
