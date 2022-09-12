# from ..DB.Query import query
from .Constant.MentalInfo import MentalScore
from .Constant.MentalInfo import MentalProposal_div
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


def count_score(data):  # 计算每个心理模块的分数：压力、抑郁、焦虑
    score = 0
    # print(data, len(data))
    for i in data:  # question+option_id对应相应的分数
        # print(i, data[i])
        score += MentalScore[i][data[i]]
    # print(score)
    # print("-------------")
    return score


class Mental:

    def __init__(self, questionnaire_mental):
        try:
            self.D = {}  # D:抑郁
            self.A = {}  # A:焦虑
            self.P = {}  # P:压力
            self.character = {}
            self.init_questionnaire_mental(questionnaire_mental)
            self.mental_results = {'D': count_score(self.D), 'A': count_score(self.A), 'P': count_score(self.P)}
            self.mental_results = {'D': 0, 'A': 0, 'P': 30}
            # results = {'D': 15, 'A': 15, 'P': 25}  # 测试用例
            self.recommendMental = self.get_mental_proposal(self.mental_results)
        except Exception as err:
            logger.error("心理模块故障:" + str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            raise Exception("Mental Model Breakdown")

    def init_questionnaire_mental(self, questionnaire_mental):
        # P
        for questions in questionnaire_mental[0:14]:
            option_sort = 0
            for option in questions['optionInformationList']:
                if questions['questionAnswer']['optionId'] == option['id']:
                    option_sort = option['optionSort']
            self.P[questions['questionName']] = option_sort
        # print(self.P)
        # D
        for questions in questionnaire_mental[14:24]:
            option_sort = 0
            for option in questions['optionInformationList']:
                if questions['questionAnswer']['optionId'] == option['id']:
                    option_sort = option['optionSort']
            self.D[questions['questionName']] = option_sort
        # print(self.D)
        # A
        for questions in questionnaire_mental[24:31]:
            option_sort = 0
            for option in questions['optionInformationList']:
                if questions['questionAnswer']['optionId'] == option['id']:
                    option_sort = option['optionSort']
            self.A[questions['questionName']] = option_sort
        # print(self.A)

    @staticmethod
    def get_mental_proposal(results):  # 哪个不合格添加哪个建议
        proposal = []
        mental_result = []
        if results['A'] <= 4 and results['D'] < 10 and results['P'] < 25:  # 均合格时
            proposal.append(MentalProposal_div["A<=4 D<10 P<25"])
            result_end = "您的情绪状态良好"
            return {"得分": results, "建议": proposal, "判断结果": result_end, "健康教育": {}}
        # P
        if 25 <= results['P']:
            proposal.append(MentalProposal_div['25<=P'])
            mental_result.append("压力")
        # D
        if 10 <= results['D']:
            proposal.append(MentalProposal_div['10<=D'])
            mental_result.append("抑郁情绪")
        # A
        if 5 <= results['A'] <= 9:
            proposal.append(MentalProposal_div['5<=A<=9'])
            mental_result.append("轻度的焦虑情绪")
        elif 10 <= results['A'] <= 14:
            proposal.append(MentalProposal_div['10<=A<=14'])
            mental_result.append("中度的焦虑情绪")
        elif 15 <= results['A']:
            proposal.append(MentalProposal_div['15<=A'])
            mental_result.append("重度的焦虑情绪")
        result_end = "您可能存在"
        for one in mental_result:
            if one != mental_result[0]:
                result_end += "和"
            result_end += one
        # 健康教育
        health_education = {}
        if results['A'] >= 5:
            health_education = MentalProposal_div["焦虑健康教育"]
        if results['P'] >= 25:
            health_education = MentalProposal_div["压力健康教育"]
        return {"得分": results, "建议": proposal, "判断结果": result_end, "健康教育": health_education}
        # 排列组合所有情况代码，已废弃
        # if results['A'] <= 4:  # A
        #     if results['D'] < 10:  # D
        #         if results['P'] < 25:  # P
        #             return MentalProposal["A<=4 D<10 P<25"]
        #         else:  # P
        #             return "A<=4 D<10 P>=25"
        #
        #     else:  # D
        #         if results['P'] < 25:  # P
        #             return "A<=4 D>=10 P<25"
        #         else:  # P
        #             return "A<=4 D>=10 P>=25"
        #
        # elif 5 <= results['A'] < 10:  # A
        #     if results['D'] < 10:  # D
        #         if results['P'] < 25:  # P
        #             return "5<=A<10 D<10 P<25"
        #         else:  # P
        #             return "5<=A<10 D<10 P>=25"
        #
        #     else:  # D
        #         if results['P'] < 25:  # P
        #             return "5<=A<10 D>=10 P<25"
        #         else:  # P
        #             return "5<=A<10 D>=10 P>=25"
        #
        # elif 10 <= results['A'] < 15:  # A
        #     if results['D'] < 10:  # D
        #         if results['P'] < 25:  # P
        #             return "10<=A<15 D<10 P<25"
        #         else:  # P
        #             return "10<=A<15 D<10 P>=25"
        #
        #     else:  # D
        #         if results['P'] < 25:  # P
        #             return "10<=A<15 D>=10 P<25"
        #         else:  # P
        #             return "10<=A<15 D>=10 P>=25"
        #
        # else:  # A
        #     if results['D'] < 10:  # D
        #         if results['P'] < 25:  # P
        #             return "15<=A D<10 P<25"
        #         else:  # P
        #             return "15<=A D<10 P>=25"
        #
        #     else:  # D
        #         if results['P'] < 25:  # P
        #             return "15<=A D>=10 P<25"
        #         else:  # P
        #             return "15<=A D>=10 P>=25"
