import json
from urllib.parse import unquote_plus

from flask import make_response, request, Blueprint
from log_config import mf_logger

root = Blueprint('root', __name__, url_prefix='/root/')


@root.route('/index.json', methods=('GET',))
def index():
    params = json.loads(unquote_plus(request.args.get('params')))
    mf_logger.info("参数params:" + str(params))
    logStr = ''
    for i in range(100):
        logStr = logStr+str(i) + '-'
    mf_logger.info(logStr)
    response = make_response(json.dumps(params), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@root.route('/add.json')
def addUser():
    from user_model import QrCodeScene
    mf_logger.info("add data start!")
    user = QrCodeScene()
    user.scene = 1
    user.url = '1'
    user.jobID = 1
    user.operatorID = 1
    user.publisher = 1
    user.shopID = 1
    user.tag = 1
    user.userID = 1
    user.save()
    mf_logger.info("add data success!")
    return 'add success!'
