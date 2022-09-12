class OptionInformation:

    def __init__(self, option_information):
        self.questionId = option_information["questionId"]
        self.optionValue = option_information["optionValue"]
        if "questionnaireId" in option_information:
            self.questionnaireId = option_information["questionnaireId"]
        else:
            self.questionnaireId = None
        self.optionSort = option_information["optionSort"]
        self.fillEnabled = option_information["fillEnabled"]
        self.id = option_information["id"]

    def __str__(self):
        return "[<OptionInformation Object: optionValue: {}>]".format(self.optionValue)


class QuestionAnswer:

    def __init__(self, question_answer):
        if question_answer == {}:
            self.questionId = None
            self.questionnaireId = None
            self.userId = None
            self.optionId = None
            self.comment = None
            self.id = None
            self.submitId = None
            self.createDate = None
        else:
            self.questionId = question_answer["questionId"]
            self.questionnaireId = question_answer["questionnaireId"]
            self.userId = question_answer["userId"]
            self.optionId = question_answer["optionId"]
            self.comment = question_answer["comment"]
            self.id = question_answer["id"]
            self.submitId = question_answer["submitId"]
            self.createDate = question_answer["createDate"]

    def __str__(self):
        return "[<QuestionAnswer Object: QuestionId: {}\tComment: {}>]".format(self.questionId, self.comment)


class Question:

    def __init__(self, question):
        self.id = int(question["id"])
        if "requiredEnabled" in question:
            self.requiredEnabled = question["requiredEnabled"]
        else:
            self.requiredEnabled = None
        self.questionName = question["questionName"]
        self.questionnaireId = question["questionnaireId"]
        self.optionInformationList = []
        for optionInformation in question["optionInformationList"]:
            self.optionInformationList.append(OptionInformation(option_information=optionInformation))
            # print(optionInformation)
        # OptionInformationList(question["optionInformationList"])
        self.questionAnswer = QuestionAnswer(question["questionAnswer"])
        # print(len(self.option_information_list))

    def __str__(self):
        option_information_list_string = []
        for optionInformation in self.optionInformationList:
            option_information_list_string.append(optionInformation.__str__())
        return "[Question Object]:\n\tQuestionId: {}\n\tQuestionnaireId: {}\n\tQuestionName: {}" \
               "\n\tOptionInformationList: {}\n\tQuestionAnswer: {}\n".format(self.id, self.questionnaireId,
                                                                              self.questionName,
                                                                              option_information_list_string,
                                                                              self.questionAnswer)


class QuestionnaireModel:

    def __init__(self, questionnaire):
        self.QuestionList = []
        for i in questionnaire:
            self.QuestionList.append(Question(i))

    def get_question(self, id):  # 根据id获取问卷中的问题
        for i in self.QuestionList:
            if i.id == id:
                return i

# A = {
#     "questionnaire": {
#         "1": [
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "1",
#                         "optionValue": "有",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "1"
#                     },
#                     {
#                         "questionId": "1",
#                         "optionValue": "无",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "2"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "是否有过敏史或饮食禁忌",
#                 "questionAnswer": {
#                     "questionId": "1",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "2",
#                     "comment": "",
#                     "id": "32f62b36-c0ee-40d8-9c75-4ae45f81a81d",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "1"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "2",
#                         "optionValue": "花生",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "759"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "鸡蛋",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "760"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "大豆类",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "761"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "鱼类",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "762"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "虾类",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "763"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "蟹类",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "764"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "贝类",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "765"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "液态乳（如纯牛奶、鲜牛奶）",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "766"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "青霉素",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "767"
#                     },
#                     {
#                         "questionId": "2",
#                         "optionValue": "其他",
#                         "optionSort": 10,
#                         "fillEnabled": 1,
#                         "id": "768"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "有哪些过敏史或饮食禁忌",
#                 "questionAnswer": {},
#                 "id": "2"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "7",
#                         "optionValue": "有",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "10"
#                     },
#                     {
#                         "questionId": "7",
#                         "optionValue": "无",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "11"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "是否有疾病既往史",
#                 "questionAnswer": {
#                     "questionId": "7",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "11",
#                     "comment": "",
#                     "id": "9ee70b96-5f8d-455c-b7fb-cc0838603e12",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "7"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "8",
#                         "optionValue": "通风",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "769"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "甲亢",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "770"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "甲减",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "771"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "肾功能受损",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "772"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "心肺功能不全",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "773"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "脑血管疾病",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "774"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "关节损伤（膝、髋、肩、肘等）",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "775"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "腰间盘突出",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "776"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "脊柱损伤",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "777"
#                     },
#                     {
#                         "questionId": "8",
#                         "optionValue": "其他",
#                         "optionSort": 10,
#                         "fillEnabled": 1,
#                         "id": "778"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "有哪些疾病既往史",
#                 "questionAnswer": {},
#                 "id": "8"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "9",
#                         "optionValue": "有",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "13"
#                     },
#                     {
#                         "questionId": "9",
#                         "optionValue": "无",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "14"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "是否有手术既往史",
#                 "questionAnswer": {
#                     "questionId": "9",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "14",
#                     "comment": "",
#                     "id": "2a667b0a-2381-439f-a2ce-dba0dc0a7c3d",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "9"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "10",
#                         "optionValue": "甲状腺切除术",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "779"
#                     },
#                     {
#                         "questionId": "10",
#                         "optionValue": "心血管相关手术",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "780"
#                     },
#                     {
#                         "questionId": "10",
#                         "optionValue": "脑血管相关手术",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "781"
#                     },
#                     {
#                         "questionId": "10",
#                         "optionValue": "关节（膝、髋、肩、肘等）、脊柱相关手术史",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "782"
#                     },
#                     {
#                         "questionId": "10",
#                         "optionValue": "其他",
#                         "optionSort": 5,
#                         "fillEnabled": 1,
#                         "id": "783"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "有哪些手术既往史",
#                 "questionAnswer": {},
#                 "id": "10"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "11",
#                         "optionValue": "有",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "16"
#                     },
#                     {
#                         "questionId": "11",
#                         "optionValue": "无",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "17"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "是否有运动禁忌",
#                 "questionAnswer": {
#                     "questionId": "11",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "17",
#                     "comment": "",
#                     "id": "0724e2d4-e89d-478c-b18e-2eef647a48dd",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "11"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "12",
#                         "optionValue": "跑步",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "784"
#                     },
#                     {
#                         "questionId": "12",
#                         "optionValue": "自行车",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "785"
#                     },
#                     {
#                         "questionId": "12",
#                         "optionValue": "跳绳",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "786"
#                     },
#                     {
#                         "questionId": "12",
#                         "optionValue": "登山",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "787"
#                     },
#                     {
#                         "questionId": "12",
#                         "optionValue": "其他",
#                         "optionSort": 5,
#                         "fillEnabled": 1,
#                         "id": "788"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "有哪些运动禁忌",
#                 "questionAnswer": {},
#                 "id": "12"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "13",
#                         "optionValue": "有",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "29"
#                     },
#                     {
#                         "questionId": "13",
#                         "optionValue": "无",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "30"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "是否有以下症状（如头痛、头晕、心悸、胸闷、胸痛、眼花、耳鸣）",
#                 "questionAnswer": {
#                     "questionId": "13",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "30",
#                     "comment": "",
#                     "id": "40f0dcd9-cbb1-4d15-9d44-bafb57265954",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "13"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "15",
#                         "optionValue": "荤素均衡",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "39"
#                     },
#                     {
#                         "questionId": "15",
#                         "optionValue": "荤食为主",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "40"
#                     },
#                     {
#                         "questionId": "15",
#                         "optionValue": "素食为主",
#                         "questionnaireId": "1",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "41"
#                     },
#                     {
#                         "questionId": "15",
#                         "optionValue": "嗜盐",
#                         "questionnaireId": "1",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "42"
#                     },
#                     {
#                         "questionId": "15",
#                         "optionValue": "嗜油",
#                         "questionnaireId": "1",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "43"
#                     },
#                     {
#                         "questionId": "15",
#                         "optionValue": "嗜糖",
#                         "questionnaireId": "1",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "44"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "饮食习惯（可单选可多选）",
#                 "questionAnswer": {
#                     "questionId": "15",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "",
#                     "comment": "",
#                     "id": "d90353dc-856d-4bdc-99f1-6a31926d8275",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "15"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "16",
#                         "optionValue": "参加",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "45"
#                     },
#                     {
#                         "questionId": "16",
#                         "optionValue": "从不或几乎不参加",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "46"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【体育锻炼】在过去1年里，您是否参加过体育锻炼",
#                 "questionAnswer": {
#                     "questionId": "16",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "46",
#                     "comment": "",
#                     "id": "2e5e8420-d31a-427a-95c0-8d3512f3d0a0",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "16"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "17",
#                         "optionValue": "每月1~3次",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "47"
#                     },
#                     {
#                         "questionId": "17",
#                         "optionValue": "每周1~2次",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "48"
#                     },
#                     {
#                         "questionId": "17",
#                         "optionValue": "每周3~5次",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "49"
#                     },
#                     {
#                         "questionId": "17",
#                         "optionValue": "每天或几乎每天",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "50"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【体育锻炼】在过去1年里，您一般多久参加1次体育锻炼",
#                 "questionAnswer": {},
#                 "id": "17"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "18",
#                         "optionValue": "散步",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "51"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "跑步",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "52"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "游泳",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "53"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "篮、足、排球",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "54"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "乒乓球、羽毛球、台球等小球",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "55"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "广场舞、健身操",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "56"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "武术、太极拳",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "57"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "自行车",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "58"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "登山",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "59"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "力量训练（自重训练、器械训练）",
#                         "optionSort": 10,
#                         "fillEnabled": 0,
#                         "id": "60"
#                     },
#                     {
#                         "questionId": "18",
#                         "optionValue": "其他",
#                         "optionSort": 11,
#                         "fillEnabled": 1,
#                         "id": "61"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【体育锻炼】您常用的锻炼方式（可单选可多选）",
#                 "questionAnswer": {},
#                 "id": "18"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "19",
#                         "optionValue": "吸烟",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "62"
#                     },
#                     {
#                         "questionId": "19",
#                         "optionValue": "从不吸烟",
#                         "questionnaireId": "1",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "63"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【吸烟情况】是否吸过烟",
#                 "questionAnswer": {
#                     "questionId": "19",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "63",
#                     "comment": "",
#                     "id": "424d7692-a868-4693-84ea-480a434e8690",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "19"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "20",
#                         "optionValue": "{}支（平均）",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "64"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【吸烟情况】日吸烟量",
#                 "questionAnswer": {},
#                 "id": "20"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "21",
#                         "optionValue": "{}岁",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "65"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【吸烟情况】开始吸烟年龄",
#                 "questionAnswer": {},
#                 "id": "21"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "22",
#                         "optionValue": "已戒烟",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "66"
#                     },
#                     {
#                         "questionId": "22",
#                         "optionValue": "未戒烟或从不吸烟",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "67"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【吸烟情况】是否戒烟",
#                 "questionAnswer": {
#                     "questionId": "22",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "67",
#                     "comment": "",
#                     "id": "d38a745f-7d3b-4a3e-9924-116dc87a1ce7",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "22"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "23",
#                         "optionValue": "{}年",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "68"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【吸烟情况】戒烟已持续多少年",
#                 "questionAnswer": {},
#                 "id": "23"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "24",
#                         "optionValue": "饮酒",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "69"
#                     },
#                     {
#                         "questionId": "24",
#                         "optionValue": "从不饮酒",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "70"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【饮酒情况】是否饮酒",
#                 "questionAnswer": {
#                     "questionId": "24",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "70",
#                     "comment": "",
#                     "id": "530b4e7e-34cc-4583-9dd7-6ef2831af98d",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "24"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "25",
#                         "optionValue": "{}岁",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "71"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【饮酒情况】开始饮酒年龄",
#                 "questionAnswer": {},
#                 "id": "25"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "26",
#                         "optionValue": "已戒酒",
#                         "questionnaireId": "1",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "72"
#                     },
#                     {
#                         "questionId": "26",
#                         "optionValue": "未戒酒或从不饮酒",
#                         "questionnaireId": "1",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "73"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【饮酒情况】是否戒酒",
#                 "questionAnswer": {
#                     "questionId": "26",
#                     "questionnaireId": "1",
#                     "userId": "11",
#                     "optionId": "73",
#                     "comment": "",
#                     "id": "d3080419-21a9-4cd9-a9a6-de5c473208f7",
#                     "submitId": "d588a3f4-6dcb-4ce9-9a3b-969efb05f8f2",
#                     "createDate": 1659959554000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "26"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "27",
#                         "optionValue": "{}岁",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "74"
#                     }
#                 ],
#                 "questionnaireId": "1",
#                 "questionName": "【饮酒情况】戒酒年龄",
#                 "questionAnswer": {},
#                 "id": "27"
#             }
#         ],
#         "2": [
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "28",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "75"
#                     },
#                     {
#                         "associatedJumpId": "-1",
#                         "questionId": "28",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "76"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "您目前是否外出工作? ",
#                 "questionAnswer": {
#                     "questionId": "28",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "76",
#                     "comment": "",
#                     "id": "0108bb3d-0745-43cb-b8a4-3ba7b771bfdb",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "28"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "29",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "77"
#                     },
#                     {
#                         "questionId": "29",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "78"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您在工作中是否参加了重体力活动(如搬运重物、挖掘、爬楼梯等)且持续时间超过10分钟?(注意不包括工作以外的活动)",
#                 "questionAnswer": {
#                     "questionId": "29",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "78",
#                     "comment": "",
#                     "id": "680e024d-151c-427f-8f10-ffff81fff529",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "29"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "30",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "79"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在工作中，每周花几天进行重体力活动",
#                 "questionAnswer": {},
#                 "id": "30"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "31",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "80"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在工作中，每天花多长时间进行重体力活动",
#                 "questionAnswer": {},
#                 "id": "31"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "32",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "81"
#                     },
#                     {
#                         "questionId": "32",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "82"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您在工作中是否参加了中度体力活动(如提拎小型物品等)且持续时间超过10分钟?(注意不包括工作以外的活动) ",
#                 "questionAnswer": {
#                     "questionId": "32",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "82",
#                     "comment": "",
#                     "id": "317203f6-305e-4bf2-bf26-9e2227dbb14a",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "32"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "33",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "83"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在工作中，每周花几天进行中度体力活动?",
#                 "questionAnswer": {},
#                 "id": "33"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "34",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "84"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在工作中，每天花多长时间进行中度体力活动?",
#                 "questionAnswer": {},
#                 "id": "34"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "35",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "85"
#                     },
#                     {
#                         "questionId": "35",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "86"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否工作中步行时间持续超过10分钟? (注意不包括上下班路上的步行时间) ",
#                 "questionAnswer": {
#                     "questionId": "35",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "85",
#                     "comment": "",
#                     "id": "b2e3478e-72a1-43ac-9648-26c5d3b47aed",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "35"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "36",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "87"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在工作中，每周花几天步行?",
#                 "questionAnswer": {
#                     "questionId": "36",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "87",
#                     "comment": "5",
#                     "id": "1ea19bd8-87ec-474f-9ef9-e8eefd2de8e5",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "id": "36"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "37",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "88"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在工作中，每天花多长时间步行?",
#                 "questionAnswer": {
#                     "questionId": "37",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "88",
#                     "comment": "30",
#                     "id": "d41bbdfd-59d8-424a-8b42-3c0f72cb2f54",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "id": "37"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "38",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "89"
#                     },
#                     {
#                         "questionId": "38",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "90"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否乘车外出? ",
#                 "questionAnswer": {
#                     "questionId": "38",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "90",
#                     "comment": "",
#                     "id": "18a90bc9-eeff-4e9a-a7f2-55ab579cda44",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "38"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "39",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "91"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天乘车?  ",
#                 "questionAnswer": {},
#                 "id": "39"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "40",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "92"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天乘车花多长时间?  ",
#                 "questionAnswer": {},
#                 "id": "40"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "41",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "93"
#                     },
#                     {
#                         "questionId": "41",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "94"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否骑自行车外出，且持续时间超过10 分钟?",
#                 "questionAnswer": {
#                     "questionId": "41",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "94",
#                     "comment": "",
#                     "id": "5736746e-766e-4b51-8777-499664226590",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "41"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "42",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "95"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天骑自行车?",
#                 "questionAnswer": {},
#                 "id": "42"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "43",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "96"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天骑自行车花多长时间?",
#                 "questionAnswer": {},
#                 "id": "43"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "44",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "97"
#                     },
#                     {
#                         "questionId": "44",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "98"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否步行外出，且持续时间超过10分钟?",
#                 "questionAnswer": {
#                     "questionId": "44",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "98",
#                     "comment": "",
#                     "id": "1e8f3932-6588-4d5e-be5e-b4750d0e3afc",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "44"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "45",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "99"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天步行",
#                 "questionAnswer": {},
#                 "id": "45"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "46",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "100"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天步行花多长时间",
#                 "questionAnswer": {},
#                 "id": "46"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "47",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "101"
#                     },
#                     {
#                         "questionId": "47",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "102"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否参与了重体力家务劳动(如搬运重物、砍柴、扫雪、拖地板等)且持续时间超过10分钟。",
#                 "questionAnswer": {
#                     "questionId": "47",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "102",
#                     "comment": "",
#                     "id": "b5361b85-5e86-4617-9ec6-5c9492358b2c",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "47"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "48",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "103"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天进行重体力家务劳动?",
#                 "questionAnswer": {},
#                 "id": "48"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "49",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "104"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天花多长时间进行重体力家务劳动?",
#                 "questionAnswer": {},
#                 "id": "49"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "50",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "105"
#                     },
#                     {
#                         "questionId": "50",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "106"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否参与了中度体力家务劳动(如提拎小型物品、扫地、擦窗户、整理房间、做饭、洗衣服等)且持续时间超过10分钟",
#                 "questionAnswer": {
#                     "questionId": "50",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "106",
#                     "comment": "",
#                     "id": "edefc5d3-08cc-48b0-8511-ab23b3fb792e",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "50"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "51",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "107"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天进行中度体力家务劳动?",
#                 "questionAnswer": {},
#                 "id": "51"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "52",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "108"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天花多长时间进行中度体力家务劳动?",
#                 "questionAnswer": {},
#                 "id": "52"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "53",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "109"
#                     },
#                     {
#                         "questionId": "53",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "110"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否外出散步，且持续时间超过10分钟? (不包括您己描述过的步行时间)",
#                 "questionAnswer": {
#                     "questionId": "53",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "110",
#                     "comment": "",
#                     "id": "f20ce221-7240-4e39-b397-9599927381aa",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "53"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "54",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "111"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天在散步中? ",
#                 "questionAnswer": {},
#                 "id": "54"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "55",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "112"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天花在散步中的时间是多少? ",
#                 "questionAnswer": {},
#                 "id": "55"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "56",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "113"
#                     },
#                     {
#                         "questionId": "56",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "114"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否参加了重体力活动的体育锻炼(如有氧健身、跑步、快速骑车、游泳及足球、篮球类活动等)且持续时间超过10分钟?",
#                 "questionAnswer": {
#                     "questionId": "56",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "114",
#                     "comment": "",
#                     "id": "53d65198-9b85-4b04-a0ff-2cd7493cad2b",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "56"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "57",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "115"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天进行重体力活动体育锻炼? ",
#                 "questionAnswer": {},
#                 "id": "57"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "58",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "116"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天花多长时间进行重体力活动体育锻炼? ",
#                 "questionAnswer": {},
#                 "id": "58"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "59",
#                         "optionValue": "是",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "117"
#                     },
#                     {
#                         "questionId": "59",
#                         "optionValue": "否",
#                         "questionnaireId": "2",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "118"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您是否参加了中度体力活动的体育锻炼(如快速行走、跳交谊舞、打保龄球、 乒乓球，羽毛球等)且持续时间超过10分钟?",
#                 "questionAnswer": {
#                     "questionId": "59",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "118",
#                     "comment": "",
#                     "id": "ac344469-15ac-48f7-9174-ee80f05bcd00",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "59"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "60",
#                         "optionValue": "每周{}天",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "119"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每周花几天进行中度体力活动体育锻炼?",
#                 "questionAnswer": {},
#                 "id": "60"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "61",
#                         "optionValue": "每天{}分钟",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "120"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "每天花多长时间进行中度体力活动体育锻炼?",
#                 "questionAnswer": {},
#                 "id": "61"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "62",
#                         "optionValue": "每天{}分钟",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "121"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您工作日每天花在坐姿状态中的时间是多少?",
#                 "questionAnswer": {
#                     "questionId": "62",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "121",
#                     "comment": "480",
#                     "id": "ffaeb692-c749-4e96-8d8b-97d1a361446f",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "62"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "63",
#                         "optionValue": "每天{}分钟",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "122"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您周末或休息日每天花在坐姿状态中的时间是多少?",
#                 "questionAnswer": {
#                     "questionId": "63",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "122",
#                     "comment": "120",
#                     "id": "18d7c90f-02da-4675-981f-44b6fba4eaf2",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "63"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "64",
#                         "optionValue": "每天{}分钟",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "123"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您在工作日每天花在睡眠(包括午睡)中的时间是多少?",
#                 "questionAnswer": {
#                     "questionId": "64",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "123",
#                     "comment": "480",
#                     "id": "f8d503d8-d477-4253-ad9f-1b7d92c25253",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "64"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "65",
#                         "optionValue": "每天{}分钟",
#                         "questionnaireId": "2",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "124"
#                     }
#                 ],
#                 "questionnaireId": "2",
#                 "questionName": "在过去7天内，您在周末或休息日每天花在睡眠中的时间是多少? ",
#                 "questionAnswer": {
#                     "questionId": "65",
#                     "questionnaireId": "2",
#                     "userId": "11",
#                     "optionId": "124",
#                     "comment": "480",
#                     "id": "8a5ba51c-3be7-4490-a3ab-e46b101c320f",
#                     "submitId": "266ca678-a423-47ac-8fd5-6825079e9d3d",
#                     "createDate": 1662965569000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "65"
#             }
#         ],
#         "3": [
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "187",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "457"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "458"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "459"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "460"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "461"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "462"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "463"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "464"
#                     },
#                     {
#                         "questionId": "187",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "465"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用米饭",
#                 "questionAnswer": {
#                     "questionId": "187",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "464",
#                     "comment": "",
#                     "id": "9b8041a1-327b-4005-be75-bb51a371f261",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "187"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "188",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "466"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "467"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "468"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "469"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "470"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "471"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "472"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "473"
#                     },
#                     {
#                         "questionId": "188",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "474"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用粥、稀饭或泡饭",
#                 "questionAnswer": {
#                     "questionId": "188",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "466",
#                     "comment": "",
#                     "id": "90bd2deb-eead-4947-81cd-d8d7f2469dc2",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "188"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "189",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "475"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "476"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "477"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "478"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "479"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "480"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "481"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "482"
#                     },
#                     {
#                         "questionId": "189",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "483"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用面粉类食物（馒头、面包、面条、饼等）",
#                 "questionAnswer": {
#                     "questionId": "189",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "475",
#                     "comment": "",
#                     "id": "e0d96702-a95d-4e2e-b11c-7d20b195fd61",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "189"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "190",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "484"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "485"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "486"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "487"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "488"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "489"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "490"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "491"
#                     },
#                     {
#                         "questionId": "190",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "492"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用甜食、点心、蛋糕",
#                 "questionAnswer": {
#                     "questionId": "190",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "484",
#                     "comment": "",
#                     "id": "29b8081e-2ec0-43f5-886d-8c9a5c1190b4",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "190"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "191",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "493"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "494"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "495"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "496"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "497"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "498"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "499"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "500"
#                     },
#                     {
#                         "questionId": "191",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "501"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用油炸食物（油条、油饼等）",
#                 "questionAnswer": {
#                     "questionId": "191",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "497",
#                     "comment": "",
#                     "id": "056b025b-2741-4e7f-aba4-c9bdcfc5ca44",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "191"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "192",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "502"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "503"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "504"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "505"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "506"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "507"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "508"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "509"
#                     },
#                     {
#                         "questionId": "192",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "510"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用有馅类食物（包子、馄饨、饺子等）",
#                 "questionAnswer": {
#                     "questionId": "192",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "502",
#                     "comment": "",
#                     "id": "c925ff83-ef25-401b-a5b6-86fa58d19de1",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "192"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "193",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "511"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "512"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "513"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "514"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "515"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "516"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "517"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "518"
#                     },
#                     {
#                         "questionId": "193",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "519"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用食用粗杂粮（包括糙米、小米、玉米、薏米、燕麦、红小豆、绿豆等）",
#                 "questionAnswer": {
#                     "questionId": "193",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "511",
#                     "comment": "",
#                     "id": "d6a3a387-6f68-438a-bfd9-1eed03b000bb",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "193"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "194",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "520"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "521"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "522"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "523"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "524"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "525"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "526"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "527"
#                     },
#                     {
#                         "questionId": "194",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "528"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用薯类（包括红薯、土豆、芋头、山药、魔芋等）",
#                 "questionAnswer": {
#                     "questionId": "194",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "520",
#                     "comment": "",
#                     "id": "f4ec16a7-9863-4c5c-87d1-46ba4255ab37",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "194"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "195",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "529"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "530"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "531"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "532"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "533"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "534"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "535"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "536"
#                     },
#                     {
#                         "questionId": "195",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "537"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用牛奶、酸奶或奶粉",
#                 "questionAnswer": {
#                     "questionId": "195",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "529",
#                     "comment": "",
#                     "id": "f00c77b9-148a-4060-94a2-0101755b713f",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "195"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "196",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "538"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "539"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "540"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "541"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "542"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "543"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "544"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "545"
#                     },
#                     {
#                         "questionId": "196",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "546"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用鸡蛋或鸭蛋",
#                 "questionAnswer": {
#                     "questionId": "196",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "543",
#                     "comment": "",
#                     "id": "927bbb56-479b-4e8c-b7c1-810d8a755dfb",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "196"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "197",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "547"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "548"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "549"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "550"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "551"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "552"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "553"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "554"
#                     },
#                     {
#                         "questionId": "197",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "555"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用红肉类菜肴（猪、牛、羊肉等）",
#                 "questionAnswer": {
#                     "questionId": "197",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "551",
#                     "comment": "",
#                     "id": "40cb0dec-0bf8-4ba0-bffe-50d886b972b9",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "197"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "198",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "556"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "557"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "558"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "559"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "560"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "561"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "562"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "563"
#                     },
#                     {
#                         "questionId": "198",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "564"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用家禽类菜肴（鸡、鸭、鹅肉等）",
#                 "questionAnswer": {
#                     "questionId": "198",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "560",
#                     "comment": "",
#                     "id": "9143e8c1-50ab-4440-bdee-acf0c03a88cd",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "198"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "199",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "565"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "566"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "567"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "568"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "569"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "570"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "571"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "572"
#                     },
#                     {
#                         "questionId": "199",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "573"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用加工肉制品（香肠、熏肉、午餐肉、火腿等）",
#                 "questionAnswer": {
#                     "questionId": "199",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "568",
#                     "comment": "",
#                     "id": "c59cfe23-5129-4a86-ad97-c053603ea9c8",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "199"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "200",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "574"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "575"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "576"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "577"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "578"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "579"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "580"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "581"
#                     },
#                     {
#                         "questionId": "200",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "582"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用河鲜类菜肴（青鱼、鲈鱼、鲢鱼、河虾等）",
#                 "questionAnswer": {
#                     "questionId": "200",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "576",
#                     "comment": "",
#                     "id": "360a8295-a92f-4387-b3cf-4cac75609d2e",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "200"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "201",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "583"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "584"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "585"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "586"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "587"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "588"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "589"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "590"
#                     },
#                     {
#                         "questionId": "201",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "591"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用海鲜类菜肴（带鱼、鲳鱼、黄鱼、海虾等）",
#                 "questionAnswer": {
#                     "questionId": "201",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "585",
#                     "comment": "",
#                     "id": "c35036d9-460e-4214-8002-7f0de143c2d5",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "201"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "202",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "592"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "593"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "594"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "595"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "596"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "597"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "598"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "599"
#                     },
#                     {
#                         "questionId": "202",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "600"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用豆制品菜肴（豆腐、香干、素鸡等）",
#                 "questionAnswer": {
#                     "questionId": "202",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "595",
#                     "comment": "",
#                     "id": "fdbbe08e-545e-47af-8e59-f9f46b353aeb",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "202"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "203",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "601"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "602"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "603"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "604"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "605"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "606"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "607"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "608"
#                     },
#                     {
#                         "questionId": "203",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "609"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用坚果类（西瓜子、葵花子、核桃、花生、开心果等）",
#                 "questionAnswer": {
#                     "questionId": "203",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "601",
#                     "comment": "",
#                     "id": "f090fd6c-86de-4527-b515-65e7a3d23e43",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "203"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "204",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "610"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "611"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "612"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "613"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "614"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "615"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "616"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "617"
#                     },
#                     {
#                         "questionId": "204",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "618"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用深色蔬菜类（青菜、菠菜、空心菜、番茄、青椒、胡萝卜等）",
#                 "questionAnswer": {
#                     "questionId": "204",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "613",
#                     "comment": "",
#                     "id": "fd83b37f-7174-4af6-932b-199ceecc5ef3",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "204"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "205",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "619"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "620"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "621"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "622"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "623"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "624"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "625"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "626"
#                     },
#                     {
#                         "questionId": "205",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "627"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用浅色蔬菜类（白菜、萝卜、黄瓜等）",
#                 "questionAnswer": {
#                     "questionId": "205",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "622",
#                     "comment": "",
#                     "id": "2cc9964c-6d15-4c94-abea-00d934b6fb79",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "205"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "206",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "628"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "629"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "630"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "631"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "632"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "633"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "634"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "635"
#                     },
#                     {
#                         "questionId": "206",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "636"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用菌菇类（香菇、草菇、平菇等）",
#                 "questionAnswer": {
#                     "questionId": "206",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "631",
#                     "comment": "",
#                     "id": "203086f1-d464-404c-b584-5a359b073579",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "206"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "207",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "637"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "638"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "639"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "640"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "641"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "642"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "643"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "644"
#                     },
#                     {
#                         "questionId": "207",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "645"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否食用水果（苹果、梨、香蕉等）",
#                 "questionAnswer": {
#                     "questionId": "207",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "642",
#                     "comment": "",
#                     "id": "7a2fd016-9f10-4329-8b2b-93fca49e6149",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "207"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "208",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "646"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "647"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "648"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "649"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "650"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "651"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "652"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "653"
#                     },
#                     {
#                         "questionId": "208",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "654"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否饮用甜饮料（可乐、雪碧、冰红茶、运动饮料等）",
#                 "questionAnswer": {
#                     "questionId": "208",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "647",
#                     "comment": "",
#                     "id": "88ef9621-fb63-49bf-a8fc-af7cd85a9825",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "208"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "209",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "655"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "656"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "657"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "658"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "659"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "660"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "661"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "662"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "209",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "663"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否饮用啤酒",
#                 "questionAnswer": {
#                     "questionId": "209",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "655",
#                     "comment": "",
#                     "id": "f015ca2d-2c18-4ac6-a23a-35061cc965a3",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "209"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "210",
#                         "optionValue": "{}毫升",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "664"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "饮用啤酒的量（毫升）",
#                 "questionAnswer": {},
#                 "id": "210"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "211",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "665"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "666"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "667"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "668"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "669"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "670"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "671"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "672"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "211",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "673"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否饮用黄酒",
#                 "questionAnswer": {
#                     "questionId": "211",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "665",
#                     "comment": "",
#                     "id": "957f4d08-eef0-4216-962b-37966637c2d6",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "211"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "212",
#                         "optionValue": "{}两",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "674"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "饮用黄酒的量（两）",
#                 "questionAnswer": {},
#                 "id": "212"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "213",
#                         "optionValue": "不食用",
#                         "questionnaireId": "3",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "675"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每月小于一次",
#                         "questionnaireId": "3",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "676"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每月1-3次",
#                         "questionnaireId": "3",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "677"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每周1-2次",
#                         "questionnaireId": "3",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "678"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每周3-4次",
#                         "questionnaireId": "3",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "679"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每周5-6次",
#                         "questionnaireId": "3",
#                         "optionSort": 6,
#                         "fillEnabled": 0,
#                         "id": "680"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每天1次",
#                         "questionnaireId": "3",
#                         "optionSort": 7,
#                         "fillEnabled": 0,
#                         "id": "681"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每天2次",
#                         "questionnaireId": "3",
#                         "optionSort": 8,
#                         "fillEnabled": 0,
#                         "id": "682"
#                     },
#                     {
#                         "associatedJumpId": "1",
#                         "questionId": "213",
#                         "optionValue": "每天3次以上",
#                         "questionnaireId": "3",
#                         "optionSort": 9,
#                         "fillEnabled": 0,
#                         "id": "683"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "是否饮用白酒",
#                 "questionAnswer": {
#                     "questionId": "213",
#                     "questionnaireId": "3",
#                     "userId": "11",
#                     "optionId": "675",
#                     "comment": "",
#                     "id": "b3517ac7-ec9d-4990-85e9-47caaccb350c",
#                     "submitId": "c748756e-d21e-49ce-b23c-d6619301100d",
#                     "createDate": 1662965632000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "213"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "214",
#                         "optionValue": "{}两",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "684"
#                     }
#                 ],
#                 "questionnaireId": "3",
#                 "questionName": "饮用白酒的量（两）",
#                 "questionAnswer": {},
#                 "id": "214"
#             }
#         ],
#         "4": [
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "141",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "300"
#                     },
#                     {
#                         "questionId": "141",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "301"
#                     },
#                     {
#                         "questionId": "141",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "302"
#                     },
#                     {
#                         "questionId": "141",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "303"
#                     },
#                     {
#                         "questionId": "141",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "304"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "当意想不到的事情发生时，感到烦躁",
#                 "questionAnswer": {
#                     "questionId": "141",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "300",
#                     "comment": "",
#                     "id": "14ae0273-170b-4b3b-ba81-d8d00a7c6f21",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "141"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "142",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "305"
#                     },
#                     {
#                         "questionId": "142",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "306"
#                     },
#                     {
#                         "questionId": "142",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "307"
#                     },
#                     {
#                         "questionId": "142",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "308"
#                     },
#                     {
#                         "questionId": "142",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "309"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "感到自己无法控制生活中重要的事情",
#                 "questionAnswer": {
#                     "questionId": "142",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "305",
#                     "comment": "",
#                     "id": "0d17821f-05d9-4aa0-9812-65ffa3b97074",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "142"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "143",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "310"
#                     },
#                     {
#                         "questionId": "143",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "311"
#                     },
#                     {
#                         "questionId": "143",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "312"
#                     },
#                     {
#                         "questionId": "143",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "313"
#                     },
#                     {
#                         "questionId": "143",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "314"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "感到紧张和压力",
#                 "questionAnswer": {
#                     "questionId": "143",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "310",
#                     "comment": "",
#                     "id": "19cae3ba-bf10-48ed-a8cd-61040f85aec3",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "143"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "144",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "315"
#                     },
#                     {
#                         "questionId": "144",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "316"
#                     },
#                     {
#                         "questionId": "144",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "317"
#                     },
#                     {
#                         "questionId": "144",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "318"
#                     },
#                     {
#                         "questionId": "144",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "319"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "成功地解决了令人烦恼的生活琐事",
#                 "questionAnswer": {
#                     "questionId": "144",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "318",
#                     "comment": "",
#                     "id": "db8e0a4a-57cc-489e-a117-f5ff32eed7b5",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "144"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "145",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "320"
#                     },
#                     {
#                         "questionId": "145",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "321"
#                     },
#                     {
#                         "questionId": "145",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "322"
#                     },
#                     {
#                         "questionId": "145",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "323"
#                     },
#                     {
#                         "questionId": "145",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "324"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得自己正在有效地处理生活中发生的重大变化",
#                 "questionAnswer": {
#                     "questionId": "145",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "321",
#                     "comment": "",
#                     "id": "af05c720-34aa-4bc3-91c4-943cb1e9a794",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "145"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "146",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "325"
#                     },
#                     {
#                         "questionId": "146",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "326"
#                     },
#                     {
#                         "questionId": "146",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "327"
#                     },
#                     {
#                         "questionId": "146",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "328"
#                     },
#                     {
#                         "questionId": "146",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "329"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得自己有信心能够处理个人问题",
#                 "questionAnswer": {
#                     "questionId": "146",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "328",
#                     "comment": "",
#                     "id": "6a89b554-411e-4d8f-be9a-2db3a2be88e8",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "146"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "147",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "330"
#                     },
#                     {
#                         "questionId": "147",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "331"
#                     },
#                     {
#                         "questionId": "147",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "332"
#                     },
#                     {
#                         "questionId": "147",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "333"
#                     },
#                     {
#                         "questionId": "147",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "334"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得事情正在和你希望的一样发展",
#                 "questionAnswer": {
#                     "questionId": "147",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "332",
#                     "comment": "",
#                     "id": "10def0d2-772e-41e0-86c2-ab5ebc25b161",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "147"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "148",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "335"
#                     },
#                     {
#                         "questionId": "148",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "336"
#                     },
#                     {
#                         "questionId": "148",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "337"
#                     },
#                     {
#                         "questionId": "148",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "338"
#                     },
#                     {
#                         "questionId": "148",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "339"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得自己不能处理所有必须做的事情",
#                 "questionAnswer": {
#                     "questionId": "148",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "336",
#                     "comment": "",
#                     "id": "7da26e06-1185-4226-9a3b-1929d2e563c1",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "148"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "149",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "340"
#                     },
#                     {
#                         "questionId": "149",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "341"
#                     },
#                     {
#                         "questionId": "149",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "342"
#                     },
#                     {
#                         "questionId": "149",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "343"
#                     },
#                     {
#                         "questionId": "149",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "344"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得自己能控制生活中的一些恼怒情绪",
#                 "questionAnswer": {
#                     "questionId": "149",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "342",
#                     "comment": "",
#                     "id": "e7b4d9ae-5c16-41d0-960b-8d7dd9001d0c",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "149"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "150",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "345"
#                     },
#                     {
#                         "questionId": "150",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "346"
#                     },
#                     {
#                         "questionId": "150",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "347"
#                     },
#                     {
#                         "questionId": "150",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "348"
#                     },
#                     {
#                         "questionId": "150",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "349"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得自己能安排一切",
#                 "questionAnswer": {
#                     "questionId": "150",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "348",
#                     "comment": "",
#                     "id": "739f2fbb-1d8b-4e77-bce7-0195c4e91937",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "150"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "151",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "350"
#                     },
#                     {
#                         "questionId": "151",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "351"
#                     },
#                     {
#                         "questionId": "151",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "352"
#                     },
#                     {
#                         "questionId": "151",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "353"
#                     },
#                     {
#                         "questionId": "151",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "354"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "由于无法掌控发生的事情，感到生气了",
#                 "questionAnswer": {
#                     "questionId": "151",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "352",
#                     "comment": "",
#                     "id": "dfd6a5a5-d3a1-4d53-88b9-6338f066148f",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "151"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "152",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "355"
#                     },
#                     {
#                         "questionId": "152",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "356"
#                     },
#                     {
#                         "questionId": "152",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "357"
#                     },
#                     {
#                         "questionId": "152",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "358"
#                     },
#                     {
#                         "questionId": "152",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "359"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "认为自己必须完成某件事情了",
#                 "questionAnswer": {
#                     "questionId": "152",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "358",
#                     "comment": "",
#                     "id": "393e5c6d-9817-4c0e-ba5a-9038911aa04a",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "152"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "153",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "360"
#                     },
#                     {
#                         "questionId": "153",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "361"
#                     },
#                     {
#                         "questionId": "153",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "362"
#                     },
#                     {
#                         "questionId": "153",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "363"
#                     },
#                     {
#                         "questionId": "153",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "364"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得自己能控制时间安排的方式",
#                 "questionAnswer": {
#                     "questionId": "153",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "364",
#                     "comment": "",
#                     "id": "a3b841e2-b23e-4818-beb0-879157b446df",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "153"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "154",
#                         "optionValue": "从来没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "365"
#                     },
#                     {
#                         "questionId": "154",
#                         "optionValue": "几乎没有",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "366"
#                     },
#                     {
#                         "questionId": "154",
#                         "optionValue": "有时",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "367"
#                     },
#                     {
#                         "questionId": "154",
#                         "optionValue": "经常",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "368"
#                     },
#                     {
#                         "questionId": "154",
#                         "optionValue": "通常",
#                         "questionnaireId": "4",
#                         "optionSort": 5,
#                         "fillEnabled": 0,
#                         "id": "369"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "觉得困难积累得太大而无法克服",
#                 "questionAnswer": {
#                     "questionId": "154",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "366",
#                     "comment": "",
#                     "id": "257e7b67-9548-4f32-923b-c84c5eb0e5a4",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "154"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "155",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "370"
#                     },
#                     {
#                         "questionId": "155",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "371"
#                     },
#                     {
#                         "questionId": "155",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "372"
#                     },
#                     {
#                         "questionId": "155",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "373"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我因一些小事而烦恼",
#                 "questionAnswer": {
#                     "questionId": "155",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "371",
#                     "comment": "",
#                     "id": "0caa376a-7022-49d3-bcb4-ad29e21ee335",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "155"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "156",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "374"
#                     },
#                     {
#                         "questionId": "156",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "375"
#                     },
#                     {
#                         "questionId": "156",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "376"
#                     },
#                     {
#                         "questionId": "156",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "377"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我在做事时很难集中精力",
#                 "questionAnswer": {
#                     "questionId": "156",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "375",
#                     "comment": "",
#                     "id": "6278f2ab-2f4c-463f-9633-741ff740534c",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "156"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "157",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "378"
#                     },
#                     {
#                         "questionId": "157",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "379"
#                     },
#                     {
#                         "questionId": "157",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "380"
#                     },
#                     {
#                         "questionId": "157",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "381"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我感到情绪低落",
#                 "questionAnswer": {
#                     "questionId": "157",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "379",
#                     "comment": "",
#                     "id": "300499bd-08b7-4c0c-83c5-99a7098d5ec7",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "157"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "158",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "382"
#                     },
#                     {
#                         "questionId": "158",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "383"
#                     },
#                     {
#                         "questionId": "158",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "384"
#                     },
#                     {
#                         "questionId": "158",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "385"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我觉得做任何事都很费劲",
#                 "questionAnswer": {
#                     "questionId": "158",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "383",
#                     "comment": "",
#                     "id": "7d65daf0-bb6f-4f2c-afa1-349533ae955d",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "158"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "159",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "386"
#                     },
#                     {
#                         "questionId": "159",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "387"
#                     },
#                     {
#                         "questionId": "159",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "388"
#                     },
#                     {
#                         "questionId": "159",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "389"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我对未来充满希望",
#                 "questionAnswer": {
#                     "questionId": "159",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "389",
#                     "comment": "",
#                     "id": "b0899a6d-a0a3-49fa-a0e7-f91f2f548d50",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "159"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "160",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "390"
#                     },
#                     {
#                         "questionId": "160",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "391"
#                     },
#                     {
#                         "questionId": "160",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "392"
#                     },
#                     {
#                         "questionId": "160",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "393"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我感到害怕",
#                 "questionAnswer": {
#                     "questionId": "160",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "391",
#                     "comment": "",
#                     "id": "5d06091b-5435-4f53-ab1a-7f2a93209372",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "160"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "161",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "394"
#                     },
#                     {
#                         "questionId": "161",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "395"
#                     },
#                     {
#                         "questionId": "161",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "396"
#                     },
#                     {
#                         "questionId": "161",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "397"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我的睡眠不好",
#                 "questionAnswer": {
#                     "questionId": "161",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "395",
#                     "comment": "",
#                     "id": "b7a41e73-167f-4b86-ba11-3aa2e0ee9ede",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "161"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "162",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "398"
#                     },
#                     {
#                         "questionId": "162",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "399"
#                     },
#                     {
#                         "questionId": "162",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "400"
#                     },
#                     {
#                         "questionId": "162",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "401"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我很愉快",
#                 "questionAnswer": {
#                     "questionId": "162",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "400",
#                     "comment": "",
#                     "id": "3278d7a1-03a2-444c-b6c5-a35f848bcb42",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "162"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "163",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "402"
#                     },
#                     {
#                         "questionId": "163",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "403"
#                     },
#                     {
#                         "questionId": "163",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "404"
#                     },
#                     {
#                         "questionId": "163",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "405"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我感到孤独",
#                 "questionAnswer": {
#                     "questionId": "163",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "402",
#                     "comment": "",
#                     "id": "3a37b583-bf70-4e42-9f21-2a488854dc2f",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "163"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "164",
#                         "optionValue": "很少或者根本没有",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "406"
#                     },
#                     {
#                         "questionId": "164",
#                         "optionValue": "不太多",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "407"
#                     },
#                     {
#                         "questionId": "164",
#                         "optionValue": "有时或者说有一半的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "408"
#                     },
#                     {
#                         "questionId": "164",
#                         "optionValue": "大多数的时间",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "409"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我觉得我无法继续我的生活",
#                 "questionAnswer": {
#                     "questionId": "164",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "407",
#                     "comment": "",
#                     "id": "c4286e60-8fbd-49f1-845e-982aba0d801d",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "164"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "165",
#                         "optionValue": "完全不会",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "414"
#                     },
#                     {
#                         "questionId": "165",
#                         "optionValue": "有几天",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "415"
#                     },
#                     {
#                         "questionId": "165",
#                         "optionValue": "一半以上的天数",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "416"
#                     },
#                     {
#                         "questionId": "165",
#                         "optionValue": "几乎每天",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "417"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我经常感到不安、担心或急切",
#                 "questionAnswer": {
#                     "questionId": "165",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "414",
#                     "comment": "",
#                     "id": "99d73be9-60ae-46cf-9902-0c13da842e39",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "165"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "166",
#                         "optionValue": "完全不会",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "418"
#                     },
#                     {
#                         "questionId": "166",
#                         "optionValue": "有几天",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "419"
#                     },
#                     {
#                         "questionId": "166",
#                         "optionValue": "一半以上的天数",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "420"
#                     },
#                     {
#                         "questionId": "166",
#                         "optionValue": "几乎每天",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "421"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我总是不能停止或无法控制担心",
#                 "questionAnswer": {
#                     "questionId": "166",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "418",
#                     "comment": "",
#                     "id": "14359c22-8a0b-46cc-a1a9-2f0f03c64b3c",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "166"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "167",
#                         "optionValue": "完全不会",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "422"
#                     },
#                     {
#                         "questionId": "167",
#                         "optionValue": "有几天",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "423"
#                     },
#                     {
#                         "questionId": "167",
#                         "optionValue": "一半以上的天数",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "424"
#                     },
#                     {
#                         "questionId": "167",
#                         "optionValue": "几乎每天",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "425"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我对各种各样的事情担忧过多",
#                 "questionAnswer": {
#                     "questionId": "167",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "422",
#                     "comment": "",
#                     "id": "f7b27889-2bcd-40b0-8c42-b384f6e66afb",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "167"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "168",
#                         "optionValue": "完全不会",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "426"
#                     },
#                     {
#                         "questionId": "168",
#                         "optionValue": "有几天",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "427"
#                     },
#                     {
#                         "questionId": "168",
#                         "optionValue": "一半以上的天数",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "428"
#                     },
#                     {
#                         "questionId": "168",
#                         "optionValue": "几乎每天",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "429"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我很紧张，无法放松",
#                 "questionAnswer": {
#                     "questionId": "168",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "426",
#                     "comment": "",
#                     "id": "0a54a269-7693-417b-9dad-6e3d2ca9251e",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "168"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "169",
#                         "optionValue": "完全不会",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "430"
#                     },
#                     {
#                         "questionId": "169",
#                         "optionValue": "有几天",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "431"
#                     },
#                     {
#                         "questionId": "169",
#                         "optionValue": "一半以上的天数",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "432"
#                     },
#                     {
#                         "questionId": "169",
#                         "optionValue": "几乎每天",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "433"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我非常焦躁，以至无法静坐",
#                 "questionAnswer": {
#                     "questionId": "169",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "430",
#                     "comment": "",
#                     "id": "1e5a028c-3087-4ff2-a62d-34032fdd1a6b",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "169"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "170",
#                         "optionValue": "完全不会",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "434"
#                     },
#                     {
#                         "questionId": "170",
#                         "optionValue": "有几天",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "435"
#                     },
#                     {
#                         "questionId": "170",
#                         "optionValue": "一半以上的天数",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "436"
#                     },
#                     {
#                         "questionId": "170",
#                         "optionValue": "几乎每天",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "437"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我最近变得很易怒或躁动",
#                 "questionAnswer": {
#                     "questionId": "170",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "434",
#                     "comment": "",
#                     "id": "75fc6e65-af95-4b07-901f-a41781ca03ac",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "170"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "171",
#                         "optionValue": "完全不会",
#                         "questionnaireId": "4",
#                         "optionSort": 1,
#                         "fillEnabled": 0,
#                         "id": "438"
#                     },
#                     {
#                         "questionId": "171",
#                         "optionValue": "有几天",
#                         "questionnaireId": "4",
#                         "optionSort": 2,
#                         "fillEnabled": 0,
#                         "id": "439"
#                     },
#                     {
#                         "questionId": "171",
#                         "optionValue": "一半以上的天数",
#                         "questionnaireId": "4",
#                         "optionSort": 3,
#                         "fillEnabled": 0,
#                         "id": "440"
#                     },
#                     {
#                         "questionId": "171",
#                         "optionValue": "几乎每天",
#                         "questionnaireId": "4",
#                         "optionSort": 4,
#                         "fillEnabled": 0,
#                         "id": "441"
#                     }
#                 ],
#                 "questionnaireId": "4",
#                 "questionName": "我总是担忧会有不祥的事情发生",
#                 "questionAnswer": {
#                     "questionId": "171",
#                     "questionnaireId": "4",
#                     "userId": "11",
#                     "optionId": "438",
#                     "comment": "",
#                     "id": "21cbd140-1213-4d54-9d63-be937c361309",
#                     "submitId": "40838672-8f8d-46e6-b732-65f4ec8d7ee1",
#                     "createDate": 1662965717000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "171"
#             }
#         ],
#         "5": [
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "172",
#                         "optionValue": "{}cm",
#                         "questionnaireId": "5",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "442"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的身高",
#                 "questionAnswer": {
#                     "questionId": "172",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "442",
#                     "comment": "160",
#                     "id": "45d5f1d7-263b-479d-bcb0-c0ac382738e7",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "172"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "173",
#                         "optionValue": "{}Kg",
#                         "questionnaireId": "5",
#                         "optionSort": 2,
#                         "fillEnabled": 1,
#                         "id": "443"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的体重",
#                 "questionAnswer": {
#                     "questionId": "173",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "443",
#                     "comment": "100",
#                     "id": "36cd0407-ffcd-4998-8e64-191a00e0cfd8",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "173"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "174",
#                         "optionValue": "{}cm",
#                         "questionnaireId": "5",
#                         "optionSort": 3,
#                         "fillEnabled": 1,
#                         "id": "444"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的腰围",
#                 "questionAnswer": {
#                     "questionId": "174",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "444",
#                     "comment": "60",
#                     "id": "bb0468e8-e3ed-4005-a68a-796f3f8b6436",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "174"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "175",
#                         "optionValue": "{}mmHg",
#                         "questionnaireId": "5",
#                         "optionSort": 4,
#                         "fillEnabled": 1,
#                         "id": "445"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的血压(请用/分割高低血压)",
#                 "questionAnswer": {
#                     "questionId": "175",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "445",
#                     "comment": "114/68",
#                     "id": "8a4c0fda-5986-4f55-bc58-8c5930a10645",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "175"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "176",
#                         "optionValue": "{}次/分钟",
#                         "questionnaireId": "5",
#                         "optionSort": 5,
#                         "fillEnabled": 1,
#                         "id": "446"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的心率",
#                 "questionAnswer": {
#                     "questionId": "176",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "446",
#                     "comment": "111",
#                     "id": "cb2b7a1b-7011-4742-a2aa-9c4afa233eca",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 1,
#                 "id": "176"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "177",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 6,
#                         "fillEnabled": 1,
#                         "id": "447"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的空腹血糖（FBG）",
#                 "questionAnswer": {
#                     "questionId": "177",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "447",
#                     "comment": "",
#                     "id": "be476322-99bc-4180-b298-42c039196bcd",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "177"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "178",
#                         "optionValue": "{}%",
#                         "questionnaireId": "5",
#                         "optionSort": 7,
#                         "fillEnabled": 1,
#                         "id": "448"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的糖化血红蛋白（HbA1c）",
#                 "questionAnswer": {
#                     "questionId": "178",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "448",
#                     "comment": "",
#                     "id": "15df7eec-bc60-4838-9466-ab1d94a6b6ad",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "178"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "179",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 8,
#                         "fillEnabled": 1,
#                         "id": "449"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的总胆固醇（TCHO）",
#                 "questionAnswer": {
#                     "questionId": "179",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "449",
#                     "comment": "",
#                     "id": "1f382b57-f179-421f-a74f-abef7696ee6e",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "179"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "180",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 9,
#                         "fillEnabled": 1,
#                         "id": "450"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的甘油三脂（TG）",
#                 "questionAnswer": {
#                     "questionId": "180",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "450",
#                     "comment": "",
#                     "id": "1ff0f797-6f97-4820-9920-5ca546197ed3",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "180"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "181",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 10,
#                         "fillEnabled": 1,
#                         "id": "451"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的血清低密度脂蛋白胆固醇（LDL-C）",
#                 "questionAnswer": {
#                     "questionId": "181",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "451",
#                     "comment": "",
#                     "id": "e56db9cf-8f35-4549-92e2-7c7b011b615f",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "181"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "182",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 11,
#                         "fillEnabled": 1,
#                         "id": "452"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的血清高密度脂蛋白胆固醇（HDL-C）",
#                 "questionAnswer": {
#                     "questionId": "182",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "452",
#                     "comment": "",
#                     "id": "70cde434-b418-4af3-93ea-454e76bb6273",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "182"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "183",
#                         "optionValue": "{}μmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 12,
#                         "fillEnabled": 1,
#                         "id": "453"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的尿酸（UA）",
#                 "questionAnswer": {
#                     "questionId": "183",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "453",
#                     "comment": "",
#                     "id": "26aaf55f-6355-4fa2-9817-b41c908ef6cd",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "183"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "184",
#                         "optionValue": "{}ml",
#                         "questionnaireId": "5",
#                         "optionSort": 13,
#                         "fillEnabled": 1,
#                         "id": "454"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的肺活量",
#                 "questionAnswer": {
#                     "questionId": "184",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "454",
#                     "comment": "",
#                     "id": "1e7db5b7-8792-41ca-808e-6b76ce79138a",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "184"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "185",
#                         "optionValue": "{}kg",
#                         "questionnaireId": "5",
#                         "optionSort": 14,
#                         "fillEnabled": 1,
#                         "id": "455"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的左手握力",
#                 "questionAnswer": {
#                     "questionId": "185",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "455",
#                     "comment": "",
#                     "id": "6fe97415-c72b-48d6-b6e1-5756e0d3ca73",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "185"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "186",
#                         "optionValue": "{}kg",
#                         "questionnaireId": "5",
#                         "optionSort": 15,
#                         "fillEnabled": 1,
#                         "id": "456"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "您的右手握力",
#                 "questionAnswer": {
#                     "questionId": "186",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "456",
#                     "comment": "",
#                     "id": "b7cd42b7-f30d-43b4-a4f7-3d095a3aa252",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "186"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "225",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "755"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "血清总钙浓度（mmol/L）",
#                 "questionAnswer": {
#                     "questionId": "225",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "755",
#                     "comment": "",
#                     "id": "a4ba9995-0dd2-442e-aebb-720402c10321",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "225"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "226",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "756"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "血清离子钙浓度（mmol/L）",
#                 "questionAnswer": {
#                     "questionId": "226",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "756",
#                     "comment": "",
#                     "id": "9766d1fb-2a2c-45af-8996-58680235d89f",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "226"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "227",
#                         "optionValue": "{}mmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "757"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "血清离子镁浓度（mmol/L）",
#                 "questionAnswer": {
#                     "questionId": "227",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "757",
#                     "comment": "",
#                     "id": "6df960a4-dd47-4ea8-8154-8c22959c58a7",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "227"
#             },
#             {
#                 "optionInformationList": [
#                     {
#                         "questionId": "228",
#                         "optionValue": "{}μmol/L",
#                         "questionnaireId": "5",
#                         "optionSort": 1,
#                         "fillEnabled": 1,
#                         "id": "758"
#                     }
#                 ],
#                 "questionnaireId": "5",
#                 "questionName": "同型半胱氨酸（μmol/L）",
#                 "questionAnswer": {
#                     "questionId": "228",
#                     "questionnaireId": "5",
#                     "userId": "11",
#                     "optionId": "758",
#                     "comment": "",
#                     "id": "f4e09cf1-93bb-4de8-b509-f6481d4f8b25",
#                     "submitId": "40fd8579-221e-4888-84dd-557c4963053a",
#                     "createDate": 1662965747000
#                 },
#                 "requiredEnabled": 0,
#                 "id": "228"
#             }
#         ],
#         "user": {
#             "性别": "女",
#             "年龄": "22"
#         }
#     },
#     "userId": "11"
# }
#
#
# if __name__ == "__main__":
#     # print(A["questionnaire"]['2'])
#     ql_sport = QuestionnaireModel(A["questionnaire"]['5'])
#
#     print(ql_sport.get_question(id=28))
