from .QuestionnaireModel import QuestionnaireModel
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


class Physical:

    def __init__(self, Sports, bmi_result, questionnaire_physiology: QuestionnaireModel):
        try:
            self.PhysicalActivityType = Sports.physical_activity_type
            self.BloodCalcium = Sports.blood_calcium
            self.BloodMagnesium = Sports.blood_magnesium
            self.Homocysteine = Sports.homocysteine
            self.bmi = bmi_result
            self.BloodPressureUp = None  # 收缩血压
            self.BloodPressureDown = None  # 舒张血压
            self.get_blood_pressure(questionnaire_physiology)
            self.BloodGlucose = None  # 血糖
            self.GlycosylatedProtein = None  # 糖化血红蛋白
            self.get_blood_glucose_GSP(questionnaire_physiology)
            self.Cholesterol = None  # 胆固醇
            self.Triglyceride = None  # 甘油三酯
            self.LDL = None  # 低密度脂蛋白胆固醇
            self.get_blood_fat(questionnaire_physiology)

            self.PhysicalLevel = {}
            self.get_physical_proposal()
        except Exception as err:
            logger.error("生理模块故障:" + str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            raise Exception("Sports Model Breakdown")

    def get_blood_pressure(self, questionnaire_physiology: QuestionnaireModel):
        question_blood_pressure = questionnaire_physiology.get_question(id=175)
        if question_blood_pressure.questionAnswer.comment != "":
            self.BloodPressureUp, self.BloodPressureDown = str(question_blood_pressure.questionAnswer.comment).split(
                "/")
            self.BloodPressureUp = float(self.BloodPressureUp)
            self.BloodPressureDown = float(self.BloodPressureDown)
        else:
            self.BloodPressureUp = 110
            self.BloodPressureDown = 79
        # print(self.BloodPressureUp, self.BloodPressureDown)

    def get_blood_glucose_GSP(self, questionnaire_physiology: QuestionnaireModel):
        question_blood_glucose = questionnaire_physiology.get_question(id=177)
        if question_blood_glucose.questionAnswer.comment != "":
            self.BloodGlucose = float(question_blood_glucose.questionAnswer.comment)
        else:
            self.BloodGlucose = 6.0

        question_get_GSP = questionnaire_physiology.get_question(id=178)
        if question_get_GSP.questionAnswer.comment != "":
            self.GlycosylatedProtein = float(question_get_GSP.questionAnswer.comment)
        else:
            self.GlycosylatedProtein = 0.5
        # print(self.BloodGlucose, self.GlycosylatedProtein)

    def get_blood_fat(self, questionnaire_physiology: QuestionnaireModel):
        # self.Cholesterol = None  # 胆固醇
        # self.Triglyceride = None  # 甘油三酯
        # self.LDL # 血清低密度脂蛋白胆固醇
        question_cholesterol = questionnaire_physiology.get_question(id=179)
        if question_cholesterol.questionAnswer.comment != "":
            self.Cholesterol = float(question_cholesterol.questionAnswer.comment)
        else:
            self.Cholesterol = 5.0

        question_triglyceride = questionnaire_physiology.get_question(id=180)
        if question_triglyceride.questionAnswer.comment != "":
            self.Triglyceride = float(question_triglyceride.questionAnswer.comment)
        else:
            self.Triglyceride = 1.5

        question_ldl = questionnaire_physiology.get_question(id=181)
        if question_ldl.questionAnswer.comment != "":
            self.LDL = float(question_ldl.questionAnswer.comment)
        else:
            self.LDL = 3.0

        # print(self.Cholesterol, self.Triglyceride, self.LDL)

    def get_physical_proposal(self):
        # 体力活动情况
        pat = "低体力活动"
        if self.PhysicalActivityType == 0:  # 1:高体力活动  0:中体力活动 -1:低体力活动
            pat = "中体力活动"
        elif self.PhysicalActivityType == 1:
            pat = "高体力活动"

        # 血钙情况
        bc = None
        if self.BloodCalcium == -1:
            bc = "血钙偏低"
        elif self.BloodCalcium == 0:
            bc = "血钙正常"
        elif self.BloodCalcium == 1:
            bc = "血钙偏高"

        # 血镁情况
        bm = None
        if self.BloodMagnesium == -1:
            bm = "血镁偏低"
        elif self.BloodMagnesium == 0:
            bm = "血镁正常"
        elif self.BloodMagnesium == 1:
            bm = "血镁偏高"

        # 同型半胱氨酸情况
        hcy = None
        if self.Homocysteine == 0:
            hcy = "同型半胱氨酸正常"
        elif self.Homocysteine == 1:
            hcy = "同型半胱氨酸轻度升高"
        elif self.Homocysteine == 2:
            hcy = "同型半胱氨酸中度升高"
        elif self.Homocysteine == 3:
            hcy = "同型半胱氨酸重度升高"

        # 血压情况
        if 120 <= self.BloodPressureUp <= 139 or 80 <= self.BloodPressureDown <= 89:
            bp = "正常高值血压"
        elif 140 <= self.BloodPressureUp or 90 <= self.BloodPressureDown:
            bp = "高血压"
        else:
            bp = "正常血压"

        # 血糖情况
        if self.BloodGlucose > 6.1 or self.GlycosylatedProtein > 0.6:
            bg = "血糖升高"
        else:
            bg = "血糖正常"

        # 血脂情况
        bf = None
        if self.Cholesterol >= 5.2 or self.Triglyceride >= 1.7 or self.LDL >= 3.4:
            bf = "血脂异常"
        else:
            bf = "血脂正常"

        self.PhysicalLevel["体力活动情况"] = pat
        self.PhysicalLevel["血钙情况"] = bc
        self.PhysicalLevel["血镁情况"] = bm
        self.PhysicalLevel["同型半胱氨酸情况"] = hcy
        self.PhysicalLevel["BMI水平"] = self.bmi
        self.PhysicalLevel["血压情况"] = bp
        self.PhysicalLevel["血糖情况"] = bg
        self.PhysicalLevel["血脂情况"] = bf

