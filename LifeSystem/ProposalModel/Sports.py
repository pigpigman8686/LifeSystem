import json
import random
# from ..DB.Query import query
from .Constant.SportInfo import PhysicalActivityMET, ResistanceSportInfo
from .Constant.SportInfo import AerobicSportInfo, WarmingUp
from .Constant.SportInfo import MildAerobictNames, MiddleAerobicNames, HeightAerobicNames
from .Constant.SportInfo import MildResistanceNames, MiddleResistanceNames, GripPowerInfo
from .QuestionnaireModel import QuestionnaireModel
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


def count_standard_calories(bmi, physical_activity_type):
    if bmi["bmi_state"] == "偏瘦":
        if physical_activity_type == -1:
            return 35
        elif physical_activity_type == 0:
            return 40
        elif physical_activity_type == 1:
            return 43
    elif bmi["bmi_state"] == "正常":
        if physical_activity_type == -1:
            return 30
        elif physical_activity_type == 0:
            return 35
        elif physical_activity_type == 1:
            return 40
    else:  # 超重或肥胖
        if physical_activity_type == -1:
            return 23
        elif physical_activity_type == 0:
            return 30
        elif physical_activity_type == 1:
            return 35


def format_data(questionnaire_sports: QuestionnaireModel):  # 将问卷结果格式化
    format_sports_data = {
        'Work': {
            'Mild': {
                'time': 0,
                'day': 0
            },
            'Middle': {
                'time': 0,
                'day': 0
            },
            'Height': {
                'time': 0,
                'day': 0
            }
        },
        'Traffic': {
            'Mild': {
                'time': 0,
                'day': 0
            },
            'Middle': {
                'time': 0,
                'day': 0
            },
            'Height': {
                'time': 0,
                'day': 0
            }
        },
        'Homework': {
            'Mild': {
                'time': 0,
                'day': 0
            },
            'Middle': {
                'time': 0,
                'day': 0
            },
            'Height': {
                'time': 0,
                'day': 0
            }
        },
        'Relaxation': {
            'Mild': {
                'time': 0,
                'day': 0
            },
            'Middle': {
                'time': 0,
                'day': 0
            },
            'Height': {
                'time': 0,
                'day': 0
            }
        },
    }
    index = {
        # Work
        30: [
            'Work', 'Height', 'day'
        ],
        31: [
            'Work', 'Height', 'time'
        ],
        33: [
            'Work', 'Middle', 'day'
        ],
        34: [
            'Work', 'Middle', 'time'
        ],
        36: [
            'Work', 'Mild', 'day'
        ],
        37: [
            'Work', 'Mild', 'time'
        ],
        # Traffic
        39: [
            'Traffic', 'Mild', 'day'
        ],
        40: [
            'Traffic', 'Mild', 'time'
        ],
        42: [
            'Traffic', 'Height', 'day'
        ],
        43: [
            'Traffic', 'Height', 'time'
        ],
        45: [
            'Traffic', 'Middle', 'day'
        ],
        46: [
            'Traffic', 'Middle', 'time'
        ],
        # Homework
        48: [
            'Homework', 'Height', 'day'
        ],
        49: [
            'Homework', 'Height', 'time'
        ],
        51: [
            'Homework', 'Middle', 'day'
        ],
        52: [
            'Homework', 'Middle', 'time'
        ],
        # # Relaxation
        54: [
            'Relaxation', 'Mild', 'day'
        ],
        55: [
            'Relaxation', 'Mild', 'time'
        ],
        57: [
            'Relaxation', 'Height', 'day'
        ],
        58: [
            'Relaxation', 'Height', 'time'
        ],
        60: [
            'Relaxation', 'Middle', 'day'
        ],
        61: [
            'Relaxation', 'Middle', 'time'
        ],
    }
    for count in index:
        # print(questionnaire_sports[count])
        question = questionnaire_sports.get_question(id=count)
        if question.questionAnswer.comment:
            format_sports_data[index[count][0]][index[count][1]][index[count][2]] = int(question.questionAnswer.comment)
    # print(format_sports_data)
    return format_sports_data


def count_sum_homework_traffic_work_calories(homework, traffic, work, weight):
    cnt = 0
    #
    cnt += homework.HeightActivity.PhysicalActivityLevel
    cnt += homework.MiddleActivity.PhysicalActivityLevel
    cnt += homework.MildActivity.PhysicalActivityLevel

    cnt += traffic.HeightActivity.PhysicalActivityLevel
    cnt += traffic.MiddleActivity.PhysicalActivityLevel
    cnt += traffic.MildActivity.PhysicalActivityLevel

    cnt += work.HeightActivity.PhysicalActivityLevel
    cnt += work.MiddleActivity.PhysicalActivityLevel
    cnt += work.MildActivity.PhysicalActivityLevel

    return cnt * 0.0167 * weight / 7.0


class Sports:

    def __init__(self, questionnaire_normal: QuestionnaireModel, questionnaire_sports: QuestionnaireModel,
                 questionnaire_mental: QuestionnaireModel, questionnaire_physiology: QuestionnaireModel,
                 questionnaire_user, bmi, standard_weight):
        try:
            self.bmi = bmi
            self.proportion = bmi['bmi'] / 21
            self.format_sports_data = format_data(questionnaire_sports)  # ******重要：格式化数据******
            self.work = PhysicalActivity('Work', self.format_sports_data['Work'])
            self.traffic = PhysicalActivity('Traffic', self.format_sports_data['Traffic'])
            self.homework = PhysicalActivity('Homework', self.format_sports_data['Homework'])
            self.Relaxation = PhysicalActivity('Relaxation', self.format_sports_data['Relaxation'])

            self.physical_activity_type = None  # 1:高体力活动  0:中体力活动 -1:低体力活动
            self.count_physical_activity_type()

            self.standard_calories = count_standard_calories(self.bmi,
                                                             self.physical_activity_type) * standard_weight  # 标准卡路里
            self.sum_homework_traffic_work_calories = count_sum_homework_traffic_work_calories(self.homework,
                                                                                               self.traffic, self.work,
                                                                                               bmi["weight"])
            self.voluntary_body_activity_calories = self.standard_calories * 0.2 - self.sum_homework_traffic_work_calories  # 取20%

            self.normal_vital_capacity = True  # 肺活量是否正常
            self.is_normal_vital_capacity(questionnaire_physiology, questionnaire_user)
            self.normal_grip_power = True  # 握力是否正常
            self.is_normal_grip_power(questionnaire_physiology, questionnaire_user)
            self.sleepless = False  # 睡眠不足
            self.is_sleepless(questionnaire_sports, questionnaire_mental)
            self.usual_site = False  # 久坐
            self.is_usual_site(questionnaire_sports)
            self.is_usual_practice(questionnaire_normal)
            self.is_usual_sport = -1  # -1:不经常运动 0:经常运动 1:每天运动
            self.recommendSports = []
            count = 0  # 用于四种运动循环推荐
            for i in range(0, 30):  # 生成n次运动建议
                if self.is_usual_sport == -1 and (i % 7 == 2 or i % 7 == 4 or i % 7 == 6):  # 不经常运动人群
                    self.recommendSports.append({})
                elif self.is_usual_sport == 0 and (i % 7 == 2 or i % 7 == 5):
                    self.recommendSports.append({})
                else:
                    self.recommendSports.append(self.get_sports_proposal(questionnaire_sports, self.proportion, count))
                    count += 1
        except Exception as err:
            logger.error("运动模块故障:" + str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            raise Exception("Sports Model Breakdown")

    def count_physical_activity_type(self):
        # 判断是否是重体力活动
        height_physical_activity_day = self.sum_height_physical_activity_day()
        all_physical_activity_level = self.sum_all_physical_activity_level()
        if height_physical_activity_day >= 3 and all_physical_activity_level >= 1500:
            self.physical_activity_type = 1
            return
        all_physical_activity_day = self.sum_all_physical_activity_day()
        if all_physical_activity_day >= 7 and all_physical_activity_level >= 300:
            self.physical_activity_type = 1
            return

        # 判断是否是中体力活动
        at_least_20min_all_physical_activity_day = self.sum_at_least_20min_all_physical_activity_day()
        if at_least_20min_all_physical_activity_day >= 3:
            self.physical_activity_type = 0
            return
        at_least_30min_middle_walk_physical_activity_day = self.sum_at_least_30min_middle_walk_physical_activity_day()
        if at_least_30min_middle_walk_physical_activity_day >= 5:
            self.physical_activity_type = 0
            return
        if all_physical_activity_day >= 5 and all_physical_activity_level >= 600:
            self.physical_activity_type = 0
            return

        # 否则是轻体力活动
        self.physical_activity_type = -1

    def sum_height_physical_activity_day(self):
        cnt = 0
        cnt = cnt + self.work.HeightActivity.ActivityDay
        cnt = cnt + self.traffic.HeightActivity.ActivityDay
        cnt = cnt + self.homework.HeightActivity.ActivityDay
        cnt = cnt + self.Relaxation.HeightActivity.ActivityDay
        return cnt

    def sum_all_physical_activity_day(self):
        cnt = 0
        cnt += self.work.HeightActivity.ActivityDay + \
               self.work.MildActivity.ActivityDay + \
               self.work.MiddleActivity.ActivityDay
        cnt += self.traffic.HeightActivity.ActivityDay + \
               self.traffic.MildActivity.ActivityDay + \
               self.traffic.MiddleActivity.ActivityDay
        cnt += self.homework.HeightActivity.ActivityDay + \
               self.homework.MildActivity.ActivityDay + \
               self.homework.MiddleActivity.ActivityDay
        cnt += self.Relaxation.HeightActivity.ActivityDay + \
               self.Relaxation.MildActivity.ActivityDay + \
               self.Relaxation.MiddleActivity.ActivityDay
        return cnt

    def sum_all_physical_activity_level(self):
        cnt = 0
        cnt += self.work.MildActivity.PhysicalActivityLevel + \
               self.work.MiddleActivity.PhysicalActivityLevel + \
               self.work.HeightActivity.PhysicalActivityLevel
        return cnt

    def sum_at_least_20min_all_physical_activity_day(self):
        cnt = 0
        if self.work.HeightActivity.ActivityTime >= 20:
            cnt += 1
        if self.traffic.HeightActivity.ActivityTime >= 20:
            cnt += 1
        if self.homework.HeightActivity.ActivityTime >= 20:
            cnt += 1
        if self.Relaxation.HeightActivity.ActivityTime >= 20:
            cnt += 1
        return cnt

    def sum_at_least_30min_middle_walk_physical_activity_day(self):
        cnt = 0
        if self.work.MildActivity.ActivityTime >= 30:  # 步行类
            cnt += 1
        if self.work.MiddleActivity.ActivityTime >= 30:
            cnt += 1
        if self.traffic.MiddleActivity.ActivityTime >= 30:
            cnt += 1
        if self.homework.MiddleActivity.ActivityTime >= 30:
            cnt += 1
        if self.Relaxation.MildActivity.ActivityTime >= 30:  # 步行类
            cnt += 1
        if self.Relaxation.MiddleActivity.ActivityTime >= 30:
            cnt += 1
        return cnt

    def is_normal_vital_capacity(self, questionnaire_physiology: QuestionnaireModel, questionnaire_user):
        question = questionnaire_physiology.get_question(id=184)
        if questionnaire_user["性别"] == "男" and int(question.questionAnswer.comment) < 3500:
            self.normal_vital_capacity = False
            return
        if questionnaire_user["性别"] == "女" and int(question.questionAnswer.comment) < 2500:
            self.normal_vital_capacity = False

    def is_normal_grip_power(self, questionnaire_physiology: QuestionnaireModel, questionnaire_user):
        age = int(questionnaire_user["年龄"])  # 原始年龄
        question_left_grip_power = questionnaire_physiology.get_question(id=185)  # 握力
        if age < 18 or age > 59:
            return
        if age != 18 and age != 19:
            age = int(age / 5) * 5  # 年龄的左区间，以5为一个区间
        if questionnaire_user["性别"] == "男":
            if int(question_left_grip_power.questionAnswer.comment) < GripPowerInfo["男"][age]:
                self.normal_grip_power = False
        else:  # 女
            if int(question_left_grip_power.questionAnswer.comment) < GripPowerInfo["女"][age]:
                self.normal_grip_power = False

    def is_sleepless(self, questionnaire_sports: QuestionnaireModel, questionnaire_mental: QuestionnaireModel):
        question_sleep = questionnaire_mental.get_question(id=161)
        if question_sleep.questionAnswer.optionId == "396" or question_sleep.questionAnswer.optionId == "397":
        # if questionnaire_mental[20]["questionAnswer"]["optionId"] == "396" or \
        #         questionnaire_mental[20]["questionAnswer"][
        #             "optionId"] == "397":  # 问卷4表二第七个问题：我的睡眠不好，选择3：有时或者说一半的时间或4：大多数时间，为睡眠不足
            self.sleepless = True
            return
        sleep_time = int(questionnaire_sports.get_question(id=64).questionAnswer.comment)  # 睡眠时间
        print("sleep time:", sleep_time)
        if sleep_time < 6 * 60:  # 工作日睡眠时间小于360分钟，也为睡眠不足
            self.sleepless = True

    def is_usual_site(self, questionnaire_sports: QuestionnaireModel):
        site_time = int(questionnaire_sports.get_question(id=62).questionAnswer.comment)  # 坐姿时间
        # print(questionnaire_sports[34]['questionName'])
        # print(int(questionnaire_sports[34]['questionAnswer']['comment']))
        if site_time >= 6 * 60:
            self.usual_site = True

    def is_usual_practice(self, questionnaire_normal: QuestionnaireModel):
        question_is_sport = questionnaire_normal.get_question(id=16)
        if question_is_sport.questionAnswer.optionId == "46":  # 从不参加运动
            self.is_usual_sport = -1
        else:
            question_sport_time = questionnaire_normal.get_question(id=17)
            if question_sport_time.questionAnswer.optionId == "47" or \
                    question_sport_time.questionAnswer.optionId == "48":  # 每月1-3次或每周1-2次则为不经常运动
                self.is_usual_sport = -1
            elif question_sport_time.questionAnswer.optionId == "49":
                self.is_usual_sport = 0
            elif question_sport_time.questionAnswer.optionId == "50":
                self.is_usual_sport = 1

    def get_sports_proposal(self, questionnaire_sports, proportion, count):
        aerobic_all_sports = AerobicSportInfo.copy()  # 有氧运动深拷贝
        resistance_all_sports = ResistanceSportInfo.copy()  # 抗阻运动深拷贝
        all_sports = dict(aerobic_all_sports, **resistance_all_sports)  # 有氧运动 + 抗阻运动 合并为同一个字典
        # 开始推荐运动
        if self.bmi["bmi_state"] == "超重" or self.bmi["bmi_state"] == "肥胖" or \
                not self.normal_grip_power or not self.normal_vital_capacity:  # 超重、肥胖、握力弱、肺活量低只推荐中低强度
            aerobic_sport_name = random.sample(list(MildAerobictNames + MiddleAerobicNames), 1)[0]
            resistance_sport_name = random.sample(list(MildResistanceNames + MiddleResistanceNames), 1)[0]
        elif self.is_usual_sport == -1:  # 不经常运动者四种循环
            four_sports = ["中速步行（5km/h）", "快速步行（5.5-6km/h）", "很快速步行（7km/h）",
                           "走跑结合（慢跑成分不超过10min）"]
            aerobic_sport_name = four_sports[count % 4]
            resistance_sport_name = random.sample(list(MildResistanceNames + MiddleResistanceNames), 1)[0]
        else:
            aerobic_sport_name = random.sample(AerobicSportInfo.keys(), 1)[0]  # 随机1种有氧运动
            resistance_sport_name = random.sample(ResistanceSportInfo.keys(), 1)[0]  # 随机1种抗阻运动
        sports_names = [aerobic_sport_name, resistance_sport_name]
        proposal_sports = {
            "运动前热身": [],
            "具体的运动": [],
            "运动后拉伸": [],
            "健康教育": [],
            "注意事项": ["（1）运动时间的选择：一般可选择中午、下午或晚上进行，且饭后不宜即刻运动，需在饭后30分钟后进行；",
                         "（2）运动前应注意：①如果温度太热或太冷，请勿在户外运动；②若天气较凉，最好在户外运动时多穿一层衣服；③穿支撑性、合脚的跑步鞋或步行鞋，当鞋子出现老化迹象时及时更换（如：开裂、鞋面与鞋底分离等）；④运动前应进行5-10分钟的热身。",
                         "（3）运动后应注意：可通过舒缓的身体放松活动、补充营养、肌肉按摩等物理手段以及充足睡眠进行调整与恢复。",
                         "（4）如出现以下情况应终止运动：①胸部、颈部、肩部或手臂有疼痛和压迫感；②面色苍白、大汗，感到头晕、恶心；③肌肉痉挛，关节、足踝和下肢发生急性疼痛；④严重疲劳、严重下肢痛或间歇跛行；⑤严重呼吸困难、发绀。",
                         "（5）自身对运动强度的判断：当你运动时心率达到100-140次/分、呼吸比较急促、或主观体力感觉稍累时就已经达到中等强度的体育锻炼了。"]
        }
        # 具体运动和拉伸推荐
        for sport in sports_names:
            all_warm_up_name = all_sports[sport]["牵拉运动"]
            # 具体的运动
            recommend_sports_info = all_sports[sport].copy()
            recommend_sports_info["名称"] = sport
            del recommend_sports_info["牵拉运动"]
            if sport in AerobicSportInfo:  # 有氧运动
                # time = 40 * self.proportion * (4.5 / recommend_sports_info["MET"])
                time = self.voluntary_body_activity_calories / (
                        recommend_sports_info["MET"] * 0.0167 * self.bmi["weight"])
                if time < 60:
                    time = 60
                elif time > 90:
                    time = 90
                proposal_sports["具体的运动"].append(
                    {"推荐具体运动信息": recommend_sports_info, "推荐具体运动持续时间": int(time)})
            if sport in ResistanceSportInfo:  # 抗阻运动
                proposal_sports["具体的运动"].append(
                    {"推荐具体运动信息": recommend_sports_info, "推荐具体运动持续时间": 15})
            # 运动前热身
            warm_up_front_name = random.sample(all_warm_up_name, 1)[0]
            warm_up_front_info = WarmingUp[warm_up_front_name]
            warm_up_front_info["名称"] = warm_up_front_name
            proposal_sports["运动前热身"].append({"推荐热身运动信息": warm_up_front_info, "推荐热身运动持续时间": 3})
            # 运动后拉伸
            warm_up_back_name = random.sample(all_warm_up_name, 1)[0]
            warm_up_back_info = WarmingUp[warm_up_back_name]
            warm_up_back_info["名称"] = warm_up_back_name
            proposal_sports["运动后拉伸"].append({"运动后拉伸信息": warm_up_back_info, "运动后拉伸持续时间": 2})
            # print(sport, warm_up_name_front, warm_up_name_back)
        # print(sports)

        #  健康教育
        if self.usual_site:
            proposal_sports["健康教育"].append({
                "你还在久坐么？": "https://mp.weixin.qq.com/s?__biz=Mzg3NzY0NTIxNw==&mid=2247484108&idx=1&sn=9cca0b20269fcde4c264b3afd4010f05&chksm=cf1e9e02f86917141dcbc9b82051e0f816450b1f6724a232a9a840e3be3e2ad44d15969d12a9#rd"})
        if self.sleepless:
            proposal_sports["健康教育"].append({
                "拿什么拯救你的睡眠？": "https://mp.weixin.qq.com/s?__biz=Mzg3NzY0NTIxNw==&mid=2247484109&idx=1&sn=81ab7e2655069cafccb9c2bb37f48458&chksm=cf1e9e03f8691715563d18d4bc32e3ac9c84e455a575303e8e367191d87fa6579d22c88eefd7#rd"})
        return proposal_sports


class Activity:

    def __init__(self, classfication, strength, activityinfo):
        self.ActivityDay = activityinfo['day']
        self.ActivityTime = activityinfo['time']
        self.ActivityMET = PhysicalActivityMET[strength + classfication + 'MET']
        self.PhysicalActivityLevel = self.ActivityTime * self.ActivityMET * self.ActivityDay


class PhysicalActivity:

    def __init__(self, classfication, classficationinfo):
        self.classfication = classfication

        self.MildActivity = Activity(self.classfication, 'Mild', classficationinfo['Mild'])

        self.MiddleActivity = Activity(self.classfication, 'Middle', classficationinfo['Middle'])

        self.HeightActivity = Activity(self.classfication, 'Height', classficationinfo['Height'])
        # 'relaxation': {
        #     'mild': {
        #         'time': 10,
        #         'day': 7
        #     },
        #     'middle': {
        #         'time': 10,
        #         'day': 7
        #     }
        #     ,
        #     'height': {
        #         'time': 10,
        #         'day': 7
        #     }
        # },
