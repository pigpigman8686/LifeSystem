from .Constant.TCMInfo import TCMInfo, PointSort, PointLink, MusicLink
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


class TCM:

    def __init__(self, sleepless, mental_results):
        try:
            # print("Is Sleepless:", sleepless)
            # print("Mental Result:", mental_results)
            self.sleepless = sleepless
            self.is_a = mental_results['A']
            self.is_d = mental_results['D']
            self.is_p = mental_results['P']
            self.recommendTCM = self.get_proposal()
        except Exception as err:
            logger.error("中医模块故障:" + str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            raise Exception("TCM Model Breakdown")

    def get_proposal(self):
        all_points = {
            "穴位": [],
            "五行音乐": []
        }
        recommend_tcm = {"穴位按摩": {"头颈部穴位按摩": [],
                                      "上肢穴位按摩": [],
                                      "下肢穴位按摩": [],
                                      "腹部穴位按摩": [],
                                      "耳部穴位按摩": []
                                      },
                         "五行音乐": [],
                         "穴位按摩注意事项": [
                             "(1)在定位穴位的过程中常使用“寸”为单位进行表述，如半寸=半个拇指的宽度，1寸=拇指的宽度，1.5寸=食指和中指并拢的宽度，3寸=四指(除拇指外）并拢的宽度，确定穴位时需用自己的手指进行定位;",
                             "(2)如果伴有出血性疾病,皮肤破损、有伤口或有脓肿，有瘢痕处不宜按摩;",
                             "(3)按摩前可适当修剪指甲，以防损伤皮肤;",
                             "(4)按摩时用力要均匀、柔和、持久、禁用暴力、相反力，以防组织损伤;",
                             "(5)按摩时若有不适应及时调整手法或停止;",
                             "(6)按摩后注意保暖，防止受凉。"]
                         }
        # 用户通用
        all_points["穴位"] = all_points["穴位"] + TCMInfo["系统用户通用"]["穴位"]
        # all_points["五行音乐"] = all_points["五行音乐"] + TCMInfo["睡眠不佳的人群"]["五行音乐"]  # 空的
        if self.sleepless:
            # print(TCMInfo["睡眠不佳的人群"])
            all_points["穴位"] = all_points["穴位"] + TCMInfo["睡眠不佳的人群"]["穴位"]
            all_points["五行音乐"] = all_points["五行音乐"] + TCMInfo["睡眠不佳的人群"]["五行音乐"]
        if self.is_a >= 5:
            # print(TCMInfo["焦虑的人群"])
            all_points["穴位"] = all_points["穴位"] + TCMInfo["焦虑的人群"]["穴位"]
            all_points["五行音乐"] = all_points["五行音乐"] + TCMInfo["焦虑的人群"]["五行音乐"]
        if self.is_d >= 10:
            # print(TCMInfo["抑郁的人群"])
            all_points["穴位"] = all_points["穴位"] + TCMInfo["抑郁的人群"]["穴位"]
            all_points["五行音乐"] = all_points["五行音乐"] + TCMInfo["抑郁的人群"]["五行音乐"]
        if self.is_p >= 25:
            # print(TCMInfo["压力感的人群"])
            all_points["穴位"] = all_points["穴位"] + TCMInfo["压力感的人群"]["穴位"]
            all_points["五行音乐"] = all_points["五行音乐"] + TCMInfo["压力感的人群"]["五行音乐"]
        # print(all_points)
        for point in all_points["穴位"]:
            temp_point = {point: PointLink[point]}
            if point in PointSort["头颈部穴位按摩"] and temp_point not in recommend_tcm["穴位按摩"][
                "头颈部穴位按摩"]:  # 头颈部穴位按摩
                recommend_tcm["穴位按摩"]["头颈部穴位按摩"].append(temp_point)
            elif point in PointSort["上肢穴位按摩"] and temp_point not in recommend_tcm["穴位按摩"][
                "上肢穴位按摩"]:  # 上肢穴位按摩
                recommend_tcm["穴位按摩"]["上肢穴位按摩"].append(temp_point)
            elif point in PointSort["下肢穴位按摩"] and temp_point not in recommend_tcm["穴位按摩"][
                "下肢穴位按摩"]:  # 下肢穴位按摩
                recommend_tcm["穴位按摩"]["下肢穴位按摩"].append(temp_point)
            elif point in PointSort["腹部穴位按摩"] and temp_point not in recommend_tcm["穴位按摩"][
                "腹部穴位按摩"]:  # 腹部穴位按摩
                recommend_tcm["穴位按摩"]["腹部穴位按摩"].append(temp_point)
            elif point in PointSort["耳部穴位按摩"] and temp_point not in recommend_tcm["穴位按摩"][
                "耳部穴位按摩"]:  # 耳部穴位按摩
                recommend_tcm["穴位按摩"]["耳部穴位按摩"].append(temp_point)
        for music in all_points["五行音乐"]:
            temp_music = {music: MusicLink[music]}
            recommend_tcm["五行音乐"].append(temp_music)
        # recommend_tcm["五行音乐"] = all_points["五行音乐"]
        # print(recommend_tcm)
        return recommend_tcm
