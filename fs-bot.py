import requests
from config import config

#login_access_uri = 'https://open.feishu.cn/open-apis/authen/v1/index?redirect_uri={REDIRECT_URI}&app_id={APPID}&state={STATE}'

def get_app_access_token(app_id,app_secret):
    r = requests.post('https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal',
                         json={'app_id':app_id,'app_secret':app_secret})
    if r.status_code == 200:
        result = eval(r.text)
        assert result['code'] == 0 or result['msg'] == 'ok'
        config['app_access_token'] = result['app_access_token']
        config['tenant_access_token'] = result['tenant_access_token']

get_app_access_token(config['app_id'],config['app_secret'])
print(config)