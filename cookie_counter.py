from flask import Flask
# Cookieのため --- (*1)
from flask import make_response, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def index():
    # Cookieの値を取得 --- (*2)
    cnt_s = request.cookies.get('cnt')
    if cnt_s is None:
      cnt = 0
    else:
      cnt = int(cnt_s)

    # 訪問回数カウンタに1加算 --- (*3)
    cnt += 1
    response = make_response("""
    <h1>訪問回数：{}回</h1>
    """.format(cnt)
    )

    # Cookieに値を保存 --- (*4)
    max_age = 60*60*24*90 #単位は秒。90日。
    expires = int(datetime.now().timestamp())+max_age
    response.set_cookie('cnt',value=str(cnt),max_age=max_age,expires=expires)
    
    # 以下、戻り値を記入する。
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

