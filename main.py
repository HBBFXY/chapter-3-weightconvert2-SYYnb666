# 初始能力值
ability = 1
# 遍历365天
for day in range（1, 366）:
    # 计算当天在周期内的位置（1 - 7）
    day_in_cycle = day % 7
    # 若为0，说明是第7天，修正为7
    if day_in_cycle == 0:
        day_in_cycle = 7
    # 第4 - 7天，能力值增长1%
    if 4 ＜= day_in_cycle ＜= 7:
        ability *= 1.01
# 输出结果，保留6位小数
print（"连续学习365天后的能力值为：{:.6f}".format（ability））
