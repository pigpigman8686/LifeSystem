from .Diet import Diet
from .Mental import Mental
from .Sports import Sports
# from ..DB.Query import query
from .TCM import TCM
from .Physical import Physical
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
        self.QuestionnairePhysiology = QuestionnaireModel(questionnaire=questionnaire["5"])
        self.QuestionnaireUser = {"年龄": questionnaire["user"]["年龄"], "性别": questionnaire["user"]["性别"]}

        # 基础信息查询
        # self.height = float(questionnaire['5'][0]['questionAnswer']['comment'])
        self.height = float(self.QuestionnairePhysiology.get_question(id=172).questionAnswer.comment)
        # self.weight = float(questionnaire['5'][1]['questionAnswer']['comment'])
        self.weight = float(self.QuestionnairePhysiology.get_question(id=173).questionAnswer.comment)

        # 基础信息计算
        self.bmi_result = self.count_bmi(self.height, self.weight)
        self.standard_weight = self.height - 105

        try:
            # 心理、运动、饮食、中医信息模块
            self.Mental = Mental(self.QuestionnaireMental)
            # print("Mental Ok.....")
            self.Sports = Sports(self.QuestionnaireNormal, self.QuestionnaireSport, self.QuestionnaireMental,
                                 self.QuestionnairePhysiology, self.QuestionnaireUser, self.bmi_result,
                                 self.standard_weight)
            # print("Sports Ok.....")
            self.Diet = Diet(self.bmi_result, self.Sports.standard_calories)
            # print("Diet Ok.....")
            self.TCM = TCM(self.Sports.sleepless, self.Mental.mental_results)
            # print("TCM Ok.....")
            self.Physical = Physical(self.Sports, self.bmi_result["bmi_state"], self.QuestionnairePhysiology)
            # print("Physical Ok.....")
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
        return {"Mental": self.Mental.recommendMental,
                "Sports": self.Sports.recommendSports,
                "Diet": self.Diet.recommendDiet,
                "TCM": self.TCM.recommendTCM,
                "Physical": self.Physical.PhysicalLevel}
