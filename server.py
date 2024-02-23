from flask import jsonify# 从flask框架中导入jsonify函数,用于将数据转换为JSON格式的响应
from flask import request#从flask框架中导入request对象,用于获取客户端发送的请求数据
import json #导入json模块,用于处理JSON数据
from flask import Flask#从flask框架中导入Flask类,用于创建Web应用
from word2vec import f
app=Flask(__name__)

# def get_word(word):#定义一个函数，接受一个单词作为参数，目前函数体仅返回接收到的单词。
#     return word

@app.route("/nlp/words",methods=["GET","POST"])#使用app.route装饰器定义路由,指定URL路径和接受的请求方法
def nlp_service():#定义处理该路由请求的函数
    data=request.get_data()#从请求中获取数据
    result_data=json.loads(data)#{}将获取到的数据从JSON格式解析为Python字典
    word1 = result_data.get("word1","")
    word2 = result_data.get("word2", "")
    value = f(word1,word2)
    return jsonify({"code":200,"result":value})
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=50001)