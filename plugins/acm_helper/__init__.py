from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from .config import Config

from nonebot import on_command
from nonebot.rule import to_me

from .helper.helper import AcmHelper


# register the command
acmHelperCmd = on_command(
    "acm_helper",
    rule=to_me(),
    priority=10,
    block=True
)

# create the helper
acmHelper = AcmHelper()

# handle the command
@acmHelperCmd.handle()
async def get_ac_submissions(bot, event) -> None:
    # get the username
    username = str(event.get_message()).strip().split(' ')[-1]
    if not username:
        await acmHelperCmd.finish("请输入用户名")
    
    # get the solved submissions from codeforces
    solved_problems = acmHelper.get_online_judge_accepted_submissions(username, 'codeforces')

    # return the result
    info_str = "用户 {username} 在 codeforces 上的 AC 提交数为 {ac_num}".format(username=username, ac_num=len(solved_problems))
    await acmHelperCmd.finish(info_str)


__plugin_meta__ = PluginMetadata(
    name="ACM_Helper",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

