import os
import matplotlib.pyplot as plt
import numpy as np
from utils.utils_map_confidence import get_map
from utils.plot_auto import plt_auto
ssdpath='/home/dl/zds/back/algorithm/ssd-pytorch-master/map_out/'
# 写入模型预测结果文件地址
threhold_confidence = 0.1
# 置信度初始值为0.1
while threhold_confidence <= 0.9:
    # 置信度上限为0.9
    threhold_confidence = str(threhold_confidence)
    analyse_path = os.path.join(ssdpath, "analyse")
    if not os.path.exists(os.path.join(analyse_path, threhold_confidence)):
            os.makedirs(os.path.join(analyse_path, threhold_confidence))
    confidence_path = os.path.join(analyse_path, threhold_confidence)
    threhold_confidence = float(threhold_confidence)
    # 输出分析结果地址为'/home/aiteam/algorithms/ssd-pytorch-master/map_out/analyze'
 #   with open(os.path.join(analyse_path, threhold_confidence, 'mAP', ".txt"), "a+") as new_f:
    variate = 150
    # 计算文件夹是280
    while variate<=300:
    # 计算文件夹到300以上结束    
        variate = str(variate)                                   
        map_out_path    = os.path.join(ssdpath, 'model', variate)
        print(" (ง •_•)ง  biubiubiu-> ❤ ❤ ❤  o>_<o    ❤   (ง •_•)ง  biubiubiu-> ❤ ❤ ❤  o>_<o")
        print(variate)
        get_map(MINOVERLAP = 0.5,draw_plot = True, threhold_confidence = threhold_confidence, path = map_out_path, confidence_path = confidence_path, variate = variate, ssdpath =ssdpath)           
        variate = int(variate)
        variate += 5
    print("draw_plot")
    plt_auto(confidence_path = confidence_path, threhold_confidence = threhold_confidence)
    print("draw_plot is done")    
    threhold_confidence += 0.1 
