from .OJ_helper import OJHelper
from ..infoClass.userinfo import UserInfo

from pyquery import PyQuery as pq
from requests


class NowCoderHelper(OJHelper):
    def __init__(self):
        pass

    def get_data(self, uid: str) -> str:
        # get the general data of the user
        url: str = 'https://ac.nowcoder.com/acm/contest/profile/{uid}/practice-coding'.format(uid=uid)
        # 喜报, 不需要加 header(
        response: requests.Response = requests.get(url)
        response.raise_for_status()
        return response.text()

    def gatgatInfo(self, uid: str) -> dict:
        doc=pq(self.get_data(uid));data={}# 写完才发现data其实是字典...本来是按列表写的
        # data 格式 [username, rating, rating_rank, solvedProblems], 均为字符串
        data['username']=doc('.coder-info-detail .coder-name').text() # 用户名, 查找不到返回空字符串
        if data['username'] == '':
            return {'username':None}
        data['rating']=doc('.nk-container .status-item .state-num').text() # Rating
        data['rating_rank']=[i for i in doc('.nk-container .status-item').items()][1].text()[:-9] # Rating 排名
        data['solvedProblems']=[i for i in doc('.nk-main .my-state-main .my-state-item .state-num').items()][1].text() # 解出的题目数
        return data 

    def getUserInfo(self, uid: str) -> UserInfo:
        # check the uid
        if not uid.isdigit():
            return '暂时只支持 uid 查询。do! 御坂如是说。'
        # get the user info
        info = self.gatgatInfo(uid)
        # check if the user exists
        username = info['username']
        if username is None:
            return UserInfo(username=None, onlineJudge='NowCoder')

        return UserInfo(
            username=info['username'],
            onlineJudge='NowCoder',
            rating=int(info['rating'])
            rating_rank=int(info['rating_rank'])
            solvedProblems=int(info['solvedProblems'])
        )

    def getApproachingContestsInfo(self) -> str:
        return '暂时没有实现 NowCoder 的比赛查询功能。do! 御坂抱歉说。'