from .Diet import Diet
from .Mental import Mental
from .Sports import Sports
# from ..DB.Query import query
from .TCM import TCM
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


class BaseInfo:

    def __init__(self, questionnaire):
        # print(questionnaire['1'])

        # # 基础信息查询
        # self.__username = user_information_result[1]
        # self.__telphone_num = user_information_result[2]
        # self.__sex = user_information_result[5]
        # self.__date_of_birth = user_information_result[6]
        self.__height = float(questionnaire['5'][0]['questionAnswer']['comment'])
        self.__weight = float(questionnaire['5'][1]['questionAnswer']['comment'])
        # self.__educational_level = user_information_result[9]
        # self.__occupation = user_information_result[10]

        # # 基础信息计算
        self.__bmi_result = self.count_bmi(self.__height, self.__weight)
        self.__standard_weight = self.__height - 105

        try:
            # # 心理、运动、饮食、中医信息模块
            self.__Mental = Mental(questionnaire['4'])
            # print(self.__Mental.proposal)
            self.__Sports = Sports(questionnaire['1'], questionnaire['2'], questionnaire['4'], questionnaire['5'],
                                   questionnaire['user'], self.__bmi_result, self.__standard_weight)
            self.__Diet = Diet(questionnaire, self.__bmi_result,
                               self.__Sports.standard_calories)
            self.__TCM = TCM(self.__Sports.sleepless, self.__Mental.mental_results)
        except Exception as err:
            logger.error("四大模块创建失败:" + str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            raise Exception("Model Initialization Failed")

    @staticmethod
    def count_bmi(height, weight):
        height = height / 100
        bmi = weight / (height * height)
        # print("@@", weight, height, bmi)
        if bmi < 18.5:
            result = "偏瘦"
        elif 18.5 <= bmi < 24:
            result = "正常"
        elif 24 <= bmi < 28:
            result = "超重"
        else:
            result = "肥胖"
        return {"bmi": bmi, "bmi_state": result, "height": height, "weight": weight}

    @staticmethod
    def count_waistline(waistline, sex):
        waistline_result = "正常腰围"
        if sex == "1" and waistline >= 90:  # 男性
            waistline_result = "中心性肥胖"
        if sex == "0" and waistline >= 85:  # 女性
            waistline_result = "中心性肥胖"
        return waistline_result

    def get_proposal(self):
        return {"Mental": self.__Mental.recommendMental,
                "Sports": self.__Sports.recommendSports,
                "Diet": self.__Diet.recommendDiet,
                "TCM": self.__TCM.recommendTCM}
