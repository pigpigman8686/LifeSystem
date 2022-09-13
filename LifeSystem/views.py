import json
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from .ProposalModel.BaseInfo import BaseInfo
from django.views.decorators.csrf import csrf_exempt
# 导入logging库
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


@csrf_exempt  # 解决跨域问题
def get_user_base_info(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # 获取问卷数据
        try:
            user = BaseInfo(data['questionnaire'])
            return HttpResponse(json.dumps(user.get_proposal(), ensure_ascii=False))
        except Exception as err:
            logger.error(str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            return HttpResponse("ERROR:创建对象失败，请检查问卷格式!\nINFO:" + str(err))
    else:
        return HttpResponse("ERROR:非法请求方式")
