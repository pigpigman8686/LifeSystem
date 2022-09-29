class Physical:

    def __init__(self, Sports):
        self.PhysicalActivityType = Sports.physical_activity_type
        self.BloodCalcium = Sports.blood_calcium
        self.BloodMagnesium = Sports.blood_magnesium
        self.Homocysteine = Sports.homocysteine

        self.PhysicalLevel = {}
        self.get_physical_proposal()

    def get_physical_proposal(self):
        # 体力活动情况
        pat = "低体力活动"
        if self.PhysicalActivityType == 0:  # 1:高体力活动  0:中体力活动 -1:低体力活动
            pat = "中体力活动"
        if self.PhysicalActivityType == 1:
            pat = "高体力活动"

        # 血钙情况
        bc = None
        if self.BloodCalcium == -1:
            bc = "血钙偏低"
        if self.BloodCalcium == 0:
            bc = "血钙正常"
        if self.BloodCalcium == 1:
            bc = "血钙偏高"

        # 血镁情况
        bm = None
        if self.BloodMagnesium == -1:
            bm = "血镁偏低"
        if self.BloodMagnesium == 0:
            bm = "血镁正常"
        if self.BloodMagnesium == 1:
            bm = "血镁偏高"

        # 同型半胱氨酸情况
        hcy = None
        if self.Homocysteine == 0:
            hcy = "同型半胱氨酸正常"
        if self.Homocysteine == 1:
            hcy = "同型半胱氨酸轻度升高"
        if self.Homocysteine == 2:
            hcy = "同型半胱氨酸中度升高"
        if self.Homocysteine == 3:
            hcy = "同型半胱氨酸重度升高"

        self.PhysicalLevel["体力活动情况"] = pat
        self.PhysicalLevel["血钙情况"] = bc
        self.PhysicalLevel["血镁情况"] = bm
        self.PhysicalLevel["同型半胱氨酸情况"] = hcy
