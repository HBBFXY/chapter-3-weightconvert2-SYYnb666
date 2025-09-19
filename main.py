# 获取用户输入的初始体重
initial_weight = float（input（））
# 每年增长的体重
annual_gain = 0.5
# 月球体重是地球的比例
moon_ratio = 0.165
for year in range（1, 11）:
    # 计算地球上当年的体重
    earth_weight = initial_weight + annual_gain * year
    # 计算月球上当年的体重
    moon_weight = earth_weight * moon_ratio
    # 使用 format 控制输出格式，保留两位小数，使输出美观
    print（"{}\t{:.2f}\t\t{:.2f}".format（year, earth_weight, moon_weight））
