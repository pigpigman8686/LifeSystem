# from ..DB.Query import query
from .Constant.MentalInfo import MentalScore
from .Constant.MentalInfo import MentalProposal_div
from .QuestionnaireModel import QuestionnaireModel
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


class Mental:

    def __init__(self, questionnaire_mental: QuestionnaireModel):
        try:
            self.D = {}  # D:抑郁
            self.A = {}  # A:焦虑
            self.P = {}  # P:压力
            self.character = {}
            self.init_questionnaire_mental(questionnaire_mental)
            self.mental_results = {'D': self.count_score(self.D),
                                   'A': self.count_score(self.A),
                                   'P': self.count_score(self.P)}
            # self.mental_results = {'D': 0, 'A': 0, 'P': 30}  # 测试用例
            self.recommendMental = self.get_mental_proposal()
        except Exception as err:
            logger.error("心理模块故障:" + str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            raise Exception("Mental Model Breakdown")

    def init_questionnaire_mental(self, questionnaire_mental: QuestionnaireModel):
        # P
        for question_id in range(141, 155):
            question = questionnaire_mental.get_question(id=question_id)
            # print(question)
            option_sort = 0
            for option in question.optionInformationList:
                if question.questionAnswer.optionId == option.id:
                    option_sort = option.optionSort
                    break
            self.P[question.questionName] = option_sort
        # print(self.P)

        # D
        for question_id in range(155, 165):
            question = questionnaire_mental.get_question(id=question_id)
            option_sort = 0
            for option in question.optionInformationList:
                if question.questionAnswer.optionId == option.id:
                    option_sort = option.optionSort
                    break
            self.D[question.questionName] = option_sort
        # print(self.D)

        # A
        for question_id in range(165, 172):
            question = questionnaire_mental.get_question(id=question_id)
            option_sort = 0
            for option in question.optionInformationList:
                if question.questionAnswer.optionId == option.id:
                    option_sort = option.optionSort
                    break
            self.A[question.questionName] = option_sort
        # print(self.A)

    @staticmethod
    def count_score(data):  # 计算每个心理模块的分数：压力、抑郁、焦虑
        score = 0
        # print(data, len(data))
        for i in data:  # question+option_id对应相应的分数
            # print(i, data[i])
            score += MentalScore[i][data[i]]
        # print(score)
        return score

    def get_mental_proposal(self):  # 哪个不合格添加哪个建议
        proposal = []
        mental_result = []
        if self.mental_results['A'] <= 4 and self.mental_results['D'] < 10 and self.mental_results['P'] < 25:  # 均合格时
            proposal.append(MentalProposal_div["A<=4 D<10 P<25"])
            result_end = "您的情绪状态良好"
            return {"得分": self.mental_results, "建议": proposal, "判断结果": result_end,
                    "健康教育": {"建议": None, "练习": None}}
        # P
        if 25 <= self.mental_results['P']:
            proposal.append(MentalProposal_div['25<=P'])
            mental_result.append("压力")
        # D
        if 10 <= self.mental_results['D']:
            proposal.append(MentalProposal_div['10<=D'])
            mental_result.append("抑郁情绪")
        # A
        if 5 <= self.mental_results['A'] <= 9:
            proposal.append(MentalProposal_div['5<=A<=9'])
            mental_result.append("轻度的焦虑情绪")
        elif 10 <= self.mental_results['A'] <= 14:
            proposal.append(MentalProposal_div['10<=A<=14'])
            mental_result.append("中度的焦虑情绪")
        elif 15 <= self.mental_results['A']:
            proposal.append(MentalProposal_div['15<=A'])
            mental_result.append("重度的焦虑情绪")
        result_end = "您可能存在"
        for one in mental_result:
            if one != mental_result[0]:
                result_end += "和"
            result_end += one
        # 健康教育
        health_education = {}
        if self.mental_results['A'] >= 5:
            health_education = MentalProposal_div["焦虑健康教育"]
        if self.mental_results['P'] >= 25:
            health_education = MentalProposal_div["压力健康教育"]
        return {"得分": self.mental_results, "建议": proposal, "判断结果": result_end, "健康教育": health_education}
