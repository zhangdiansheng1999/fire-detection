import os
from utils.utils_map_confidence import get_map
ssdpath='/home/dl/zds/back/algorithm/ssd-pytorch-master/map_out/model'
# 写入模型预测结果文件地址
variate = 150
# 计算文件夹是280
while variate <= 300:
# 计算文件夹到300以上结束
    threhold_confidence = 0.1
    # 置信度初始值为0.1
    while threhold_confidence <= 0.9:
    # 置信度上限为0.9    
        variate = str(variate)                                   
        map_out_path    = os.path.join(ssdpath, variate)
        print("(ง •_•)ง  biubiubiu-> ❤ ❤ ❤  o>_<o    ❤   (ง •_•)ง  biubiubiu-> ❤ ❤ ❤  o>_<o")
        print(variate)
        get_map(MINOVERLAP = 0.5,draw_plot = True, threhold_confidence = threhold_confidence, path = map_out_path)           
        threhold_confidence += 0.1
    variate = int(variate)
    variate += 5 
