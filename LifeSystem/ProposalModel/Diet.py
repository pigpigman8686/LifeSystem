import random
from .Constant.FoodNutritionInfo import FoodNutritionInfo
import logging

# 获取一个logger对象
logger = logging.getLogger("django")


def count_standard_calories(bmi, physical_activity_type, range_type="min"):
    if bmi["bmi_state"] == "偏瘦":
        if physical_activity_type == -1:
            return 35
        elif physical_activity_type == 0:
            return 40
        elif physical_activity_type == 1 and range_type == "min":
            return 40
        elif physical_activity_type == 1 and range_type == "max":
            return 45
    elif bmi["bmi_state"] == "正常":
        if physical_activity_type == -1:
            return 30
        elif physical_activity_type == 0:
            return 35
        elif physical_activity_type == 1:
            return 40
    else:  # 超重或肥胖
        if physical_activity_type == -1 and range_type == "min":
            return 20
        elif physical_activity_type == -1 and range_type == "max":
            return 25
        elif physical_activity_type == 0:
            return 30
        elif physical_activity_type == 1:
            return 35


def generate_food_dict(name, weight, calories, category):
    return {"名称": name, "类别": category, "重量": weight, "热量": calories}


class Diet:

    def __init__(self, user_information, bmi, standard_calories):  # physical_activity_type, standard_weight):
        try:
            self.user_information = user_information
            self.proportion = bmi['bmi'] / 21
            self.standard_calories = standard_calories
            # self.standard_calories = count_standard_calories(bmi,
            #                                                  physical_activity_type, "min") * standard_weight
            # self.standard_calories = count_standard_calories(bmi,
            #                                                  physical_activity_type, "max") * standard_weight
            # 三大营养素占比
            self.standard_protein_min = None
            self.standard_protein_max = None
            self.standard_fat_min = None
            self.standard_fat_max = None
            self.standard_carbohydrate_min = None
            self.standard_carbohydrate_max = None
            self.count_protein_fat_carbohydrate(bmi)
            # 三餐占比
            self.breakfast = None
            self.lunch = None
            self.dinner = None
            self.count_three_meals()
            # 食物种类热量占比
            # self.cereal_calories = None
            # self.vegetable_calories = None
            # self.fruits_calories = None
            # self.soybean_calories = None
            # self.milk_calories = None
            # self.count_all_kinds_calories()
            self.recommendFoods = []
            self.recommendDiet = []
            for i in range(0, 30):
                self.recommendFoods.append(self.count_diet_map())
                # 各类营养素
                self.now_calories = 0
                self.now_protein = 0
                self.now_fat = 0
                self.now_cho = 0
                self.now_fiber = 0
                self.now_niacin = 0
                self.now_vitaminc = 0
                self.now_Ca = 0
                self.now_K = 0
                self.now_Mg = 0
                self.get_sum(self.recommendFoods[i])
                while abs(self.standard_calories - self.now_calories) > 600:
                    self.recommendFoods.pop()
                    self.recommendFoods.append(self.count_diet_map())
                    self.init_var()
                    self.get_sum(self.recommendFoods[i])
                # print("index:", i, self.now_calories)
                self.recommendDiet.append(self.get_diet_proposal(self.recommendFoods[i]))
        except Exception as err:
            logger.error("食谱模块故障:" + str(err))
            logger.error(f"Error Line No:{err.__traceback__.tb_lineno}")
            raise Exception("Diet Model Breakdown")

    def init_var(self):
        self.now_calories = 0
        self.now_protein = 0
        self.now_fat = 0
        self.now_cho = 0
        self.now_fiber = 0
        self.now_niacin = 0
        self.now_vitaminc = 0
        self.now_Ca = 0
        self.now_K = 0
        self.now_Mg = 0

    def count_protein_fat_carbohydrate(self, bmi):
        if bmi["bmi_state"] == "超重" or bmi["bmi_state"] == "肥胖":
            self.standard_protein_min = self.standard_calories * 0.15
            self.standard_protein_max = self.standard_calories * 0.20
        else:  # 偏瘦或正常
            self.standard_protein_min = self.standard_calories * 0.12
            self.standard_protein_max = self.standard_calories * 0.15
        self.standard_fat_min = self.standard_calories * 0.3
        self.standard_fat_max = self.standard_calories * 0.3
        self.standard_carbohydrate_min = self.standard_calories * 0.5
        self.standard_carbohydrate_max = self.standard_calories * 0.65

    def count_three_meals(self):
        self.breakfast = self.standard_calories * 0.3
        self.lunch = self.standard_calories * 0.4
        self.dinner = self.breakfast

    # def count_all_kinds_calories(self):
    #     self.cereal_calories = self.standard_calories_min * 0.28
    #     self.vegetable_calories = self.standard_calories_min * 0.34
    #     self.fruits_calories = self.standard_calories_min * 0.23
    #     self.soybean_calories = self.standard_calories_min * 0.15
    #     self.milk_calories = 300

    def count_diet_map(self):
        food_classes = [{"谷类": 2}, {"薯类": 1}, {"蔬菜类": 2}, {"菌藻类": 2}, {"水果类": 1}, {"畜禽类": 1},
                        {"鱼虾贝类": 1},
                        {"鸡蛋类": 1}, {"大豆类": 1}, {"乳类": 1}, {"坚果类": 1}, {"油脂类": 1}]  # 食物类别：食物数量
        food_standard_weight = {"谷类": 125, "薯类": 75, "蔬菜类": 100, "菌藻类": 100, "水果类": 275, "畜禽类": 80,
                                "鱼虾贝类": 30, "鸡蛋类": 50, "大豆类": 20, "乳类": 400, "坚果类": 10,
                                "油脂类": 25}  # 食物类别：标准重量
        # all_food = FoodNutritionInfo.copy()
        recommend_foods = {}
        for food_class in food_classes:  # 按类别（包括食物类别和需求数量）添加食物到推荐列表
            for key, value in food_class.items():
                foods = random.sample(FoodNutritionInfo[key].keys(), value)
                # print(key, foods)
                key_recommend_food = []
                for food in foods:
                    key_recommend_food.append({food: food_standard_weight[key] * self.proportion})  # 食物及其标准重量加入到临时推荐列表中
                recommend_foods[key] = key_recommend_food
        return recommend_foods

    def get_sum(self, recommend_foods):
        for category in recommend_foods:
            # temp_index = 0
            for food in recommend_foods[category]:
                # print(category)  # 谷类
                # print(food)  # {'面条（干切面）': 13.392857142857142}
                # print(list(food.keys())[0])  # 面条（干切面）
                # print(list(food.values())[0])  # 13.392857142857142
                self.now_calories += FoodNutritionInfo[category][list(food.keys())[0]]["energy"] / 100 * \
                                     list(food.values())[0]
                self.now_protein += FoodNutritionInfo[category][list(food.keys())[0]]["protein"] / 100 * \
                                    list(food.values())[0]
                self.now_fat += FoodNutritionInfo[category][list(food.keys())[0]]["fat"] / 100 * list(food.values())[0]
                self.now_cho += FoodNutritionInfo[category][list(food.keys())[0]]["cho"] / 100 * list(food.values())[0]
                self.now_fiber += FoodNutritionInfo[category][list(food.keys())[0]]["fiber"] / 100 * \
                                  list(food.values())[0]
                self.now_K += FoodNutritionInfo[category][list(food.keys())[0]]["K"] / 100 * list(food.values())[0]
                # self.now_calories += FoodNutritionInfo[category][list(food.keys())[0]]["energy"] / 100 * self.recommendFood[category][temp_index][food]
                # self.now_protein += FoodNutritionInfo[category][list(food.keys())[0]]["protein"] / 100 * self.recommendFood[category][temp_index][food]
                # self.now_fat += FoodNutritionInfo[category][list(food.keys())[0]]["fat"] / 100 * self.recommendFood[category][temp_index][food]
                # self.now_cho += FoodNutritionInfo[category][list(food.keys())[0]]["cho"] / 100 * self.recommendFood[category][temp_index][food]
                # self.now_fiber += FoodNutritionInfo[category][list(food.keys())[0]]["fiber"] / 100 * self.recommendFood[category][temp_index][food]
                # self.now_K += FoodNutritionInfo[category][list(food.keys())[0]]["K"] / 100 * self.recommendFood[category][temp_index][food]
                # temp_index += 1
        # print(self.now_calories)
        # print(self.now_protein)
        # print(self.now_fat)
        # print(self.now_cho)
        # print(self.now_fiber)
        # print(self.now_K)

    def get_diet_proposal(self, recommend_foods):
        recommend_diet = {}
        # 总热量模块
        proportion_unit = {"占比": int(self.now_protein / (self.now_protein + self.now_cho + self.now_fat) * 100),
                           "重量": int(self.now_protein)}
        cho_unit = {"占比": int(self.now_cho / (self.now_protein + self.now_cho + self.now_fat) * 100),
                    "重量": int(self.now_cho)}
        fat_unit = {"占比": int(self.now_fat / (self.now_protein + self.now_cho + self.now_fat) * 100),
                    "重量": int(self.now_fat)}
        recommend_diet["总热量"] = {"碳水化合物": cho_unit, "蛋白质": proportion_unit, "脂肪": fat_unit}

        # 膳食建议模块
        recommend_diet["膳食建议"] = [
            # "继续保持蛋类的摄入频率",
            "不食用油炸和加工肉制品"
        ]

        # 食谱模块
        recommend_diet["食谱"] = {
            "早餐": [],
            "午餐": [],
            "晚餐": []
        }
        index = \
            {
                "早餐": [
                    {"谷类": [0]},
                    {"鸡蛋类": [0]},
                    {"乳类": [0]},
                ],
                "午餐": [
                    {"谷类": [1]},
                    {"薯类": [0]},
                    {"蔬菜类": [0]},
                    {"菌藻类": [0]},
                    {"水果类": [0]},
                    {"畜禽类": [0]},
                    {"鱼虾贝类": [0]},
                ],
                "晚餐": [
                    {"蔬菜类": [1]},
                    {"菌藻类": [1]},
                    {"大豆类": [0]},
                    {"坚果类": [0]},
                    {"油脂类": [0]}
                ]
            }
        for meal, categorys in index.items():
            for category in categorys:
                key = list(category.keys())[0]  # 食物类别，如：谷类
                for i in category[key]:
                    name = list(recommend_foods[key][i].keys())[0]  # 食物名称，如：大米
                    weight = recommend_foods[key][i][name]
                    calories = FoodNutritionInfo[key][name]["energy"] / 100 * weight
                    recommend_diet["食谱"][meal].append(generate_food_dict(name, weight, calories, key))
        # # 谷类
        # category = "谷类"
        # three_meal = "早餐"
        # name = list(self.recommendFoods[category][0].keys())[0]
        # weight = self.recommendFoods[category][0][name]
        # calories = FoodNutritionInfo[category][name]["energy"] / 100 * weight
        # self.recommendDiet["食谱"][three_meal].append(generate_food_dict(name, weight, calories))
        # category = "谷类"
        # three_meal = "午餐"
        # name = list(self.recommendFoods[category][1].keys())[0]
        # weight = self.recommendFoods[category][1][name]
        # calories = FoodNutritionInfo[category][name]["energy"] / 100 * weight
        # self.recommendDiet["食谱"][three_meal].append(generate_food_dict(name, weight, calories))

        # 健康教育模块
        recommend_diet["健康教育"] = [
            {
                "健康要加油，生活要减“油”": "https://mp.weixin.qq.com/s?__biz=Mzg3NzY0NTIxNw==&mid=2247484106&idx=1&sn=ed0aea78990139ad955efcbdba1c8a22&chksm=cf1e9e04f8691712009e86a2af0c4821a4f6bc82e7dc2cca87b203a1bc5837727cba8359f34b#rd"},
            {
                "“盐”多必失，控盐防病": "https://mp.weixin.qq.com/s?__biz=Mzg3NzY0NTIxNw==&mid=2247484105&idx=1&sn=45b68d2a03e06d580355a1521ab45e57&chksm=cf1e9e07f869171174f29c396156ff25c465ea5eb0ed1ed9feb8aaf1508b0da47f81be1d0cc9#rd"},
            {
                "前方高“糖”，避免“甜蜜的负担”": "https://mp.weixin.qq.com/s?__biz=Mzg3NzY0NTIxNw==&mid=2247484107&idx=1&sn=b78c3f02d67045470dc1a07e28dc058d&chksm=cf1e9e05f8691713ffe1232b0b85d0597e1ab4cc1a330514312eb3099638a5b2d89e4d6b716d#rd"},
            {
                "吞云吐雾，危害几何": "https://mp.weixin.qq.com/s?__biz=Mzg3NzY0NTIxNw==&mid=2247484110&idx=1&sn=387d55f46084c7d2f9c700336e471a1f&chksm=cf1e9e00f8691716cd690f1532319aced3cd31bc6b4f73b6a70a9b766e9f5b231e4021d3ba91#rd"},
            {
                "饮酒需有度，最好不饮酒": "https://mp.weixin.qq.com/s?__biz=Mzg3NzY0NTIxNw==&mid=2247484111&idx=1&sn=894b68678f60554d2cd8e3a18d078fd3&chksm=cf1e9e01f86917173ce41b422c0afee5dc1b0ba53914f8285c84b3cc051735d638534bb7214a#rd"}
        ]
        # print(recommend_diet)
        return recommend_diet
