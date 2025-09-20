# 计算未来10年地球和月球的重量变化
earth_weight = float(input("请输入地球重量（kg）:"))
print("年份\t地球重量(kg)\t月球重量(kg)")
for year in range(1,11):
    earth_weight+=0.5
    moon_weight=earth_weight*0.165
    print(f"{year}\t{earth_weight:.2f}\t\t{moon_weight:.2f}")
