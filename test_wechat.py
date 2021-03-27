import requests
import json

class TestWechat:
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'wwea0fa0d2fb56ab67'
        secret = 'qNSrlgmH7KYgkh8QoAiBsOewAi4HCllp_npnsWgcUfU'
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}')
        return r.json()['access_token']

    def test_create(self):
        data = {
                "userid": "zhangsan",
                "name": "张三",
                "alias": "jackzhang",
                "mobile": "+86 13800000000",
                "department": [2],
                }
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        r = requests.post(url=url, data=json.dumps(data))
        print(r.json())

    def test_get_info(self):
        userid = 'zhangsan'
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        print(r.json())

    def test_update(self):
        data = {
                "userid": "zhangsan",
                "name": "张三丰",
                "mobile": "+86 13812345678",
                }
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        r = requests.post(url=url, data=json.dumps(data))
        print(r.json())

    def test_delete(self):
        userid = 'zhangsan'
        r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}')
        print(r.json())
