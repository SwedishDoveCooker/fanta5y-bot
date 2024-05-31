from .helpers.OJ_helper import OJHelper
from .helpers.codeforces_helper import CodeforcesHelper
from .helpers.luogu_helper import LuoguHelper
from .helpers.nk_helper import NowCoderHelper

from .infoClass.userinfo import UserInfo
from .infoClass.contestInfo import ContestInfo

from typing import Optional


class AcmHelper:
    def __init__(self, url: Optional[str]='127.0.0.1', port: Optional[int]=7890):
        # set codeforces helper
        self.codeforcesHelper = CodeforcesHelper(url, port)
        # set luogu helper
        self.luoguHelper = LuoguHelper(url, port)
        # set nk helper
        self.nowCoderHelper = NowCoderHelper(url, port)
        # set the helper dictionary
        # using the online judge to get the helper
        self.helperDict: dict[str: OJHelper] = {
            'codeforces': self.codeforcesHelper,
            'luogu' : self.luoguHelper,
            'nowcoder': self.nowCoderHelper,
        }

    def getUserInfo(self, username: str, onlineJudge: str) -> UserInfo:
        OJhelper: OJHelper = self.helperDict[onlineJudge]
        return OJhelper.getUserInfo(username)
    
    def getApproachingContestsInfo(self, onlineJudge: str) -> list[ContestInfo]:
        OJhelper: OJHelper = self.helperDict[onlineJudge]
        return OJhelper.getApproachingContestsInfo()
