from .Diet import Diet
from .Mental import Mental
from .Sports import Sports
# from ..DB.Query import query
from .TCM import TCM
import logging
from .QuestionnaireModel import QuestionnaireModel

# 获取一个logger对象
logger = logging.getLogger("django")


class BaseInfo:

    def __init__(self, questionnaire):
        self.QuestionnaireNormal = QuestionnaireModel(questionnaire=questionnaire["1"])
        self.QuestionnaireSport = QuestionnaireModel(questionnaire=questionnaire["2"])
        self.QuestionnaireDiet = QuestionnaireModel(questionnaire=questionnaire["3"])
        self.QuestionnaireMental = QuestionnaireModel(questionnaire=questionnaire["4"])
        self.QuestionnaireUser = QuestionnaireModel(questionnaire=questionnaire["5"])
        self.QuestionnaireUserAge = questionnaire["user"]["年龄"]
        self.QuestionnaireUserGender = questionnaire["user"]["性别"]

        # 基础信息查询
        # self.height = float(questionnaire['5'][0]['questionAnswer']['comment'])
        self.height = float(self.QuestionnaireUser.get_question(id=172).questionAnswer.comment)
        # self.weight = float(questionnaire['5'][1]['questionAnswer']['comment'])
        self.weight = float(self.QuestionnaireUser.get_question(id=173).questionAnswer.comment)

        # 基础信息计算
        self.bmi_result = self.count_bmi(self.height, self.weight)
        self.standard_weight = self.height - 105

        try:
            # 心理、运动、饮食、中医信息模块
            self.__Mental = Mental(self.QuestionnaireMental)
            # print("Mental Ok.....")
            self.__Sports = Sports(questionnaire['1'], questionnaire['2'], questionnaire['4'], questionnaire['5'],
                                   questionnaire['user'], self.bmi_result, self.standard_weight)
            # print("Sports Ok.....")
            self.__Diet = Diet(questionnaire, self.bmi_result, self.__Sports.standard_calories)
            # print("Diet Ok.....")
            self.__TCM = TCM(self.__Sports.sleepless, self.__Mental.mental_results)
            # print("TCM Ok.....")
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
