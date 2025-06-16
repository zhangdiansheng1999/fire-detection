import os
import xml.etree.ElementTree as ET

from PIL import Image
from tqdm import tqdm

from ssd import SSD
from utils.utils import get_classes
import os

model_dir_path='/home/dl/zds/back/algorithm/ssd-pytorch-master/logs'
# 写入权重所在文件夹
ssdpath='/home/dl/zds/back/algorithm/ssd-pytorch-master'
# 写入ssd所在文件夹
variate = 150
while variate<=300:    
    variate = str(variate)
    model_path             = os.path.join(model_dir_path, variate +'.pth')
    if __name__ == "__main__":

        classes_path    = 'model_data/voc_classes.txt'

        VOCdevkit_path  = '/home/dl/zds/back/datasets/test_datasets/VOCdevkit'

        map_out_path    = 'map_out/model'
        map_out_path    = os.path.join(ssdpath, map_out_path, variate)

        image_ids = open(os.path.join(VOCdevkit_path, "VOC2007/ImageSets/Main/test.txt")).read().strip().split()

        if not os.path.exists(map_out_path):
            os.makedirs(map_out_path)

        if not os.path.exists(os.path.join(map_out_path, 'detection-results')):
            os.makedirs(os.path.join(map_out_path, 'detection-results'))


        class_names, _ = get_classes(classes_path)


        #开始生成预测框
        print("Load model.")
        ssd = SSD(confidence = 0.1, nms_iou = 0.5, model_path = model_path)
        print("Load model done.")
        print("Get predict result.")
        for image_id in tqdm(image_ids):
            image_path  = os.path.join(VOCdevkit_path, "VOC2007/JPEGImages/"+image_id+".jpg")
            image       = Image.open(image_path)                
            ssd.get_map_txt(image_id, image, class_names, map_out_path)
        print("Get predict result done.")
            
    variate = int(variate)
    variate += 5

#生成存放原图和标准框的文件夹
if not os.path.exists(os.path.join(ssdpath, 'map_out','ground-truth')):
    os.makedirs(os.path.join(ssdpath, 'map_out','ground-truth'))
if not os.path.exists(os.path.join(ssdpath, 'map_out', 'images-optional')):
    os.makedirs(os.path.join(ssdpath, 'map_out', 'images-optional'))

#生成原图
image.save(os.path.join(ssdpath, 'map_out', "images-optional/" + image_id + ".jpg"))

#生成标准框
print("Get ground truth result.")
if not os.path.exists(os.path.join(ssdpath, 'map_out','ground-truth')):
    os.makedirs(os.path.join(ssdpath, 'map_out','ground-truth'))
if not os.path.exists(os.path.join(ssdpath, 'map_out', 'images-optional')):
    os.makedirs(os.path.join(ssdpath, 'map_out', 'images-optional'))
for image_id in tqdm(image_ids):
    with open(os.path.join(ssdpath, 'map_out', "ground-truth/"+image_id+".txt"), "w") as new_f:
        root = ET.parse(os.path.join(VOCdevkit_path, "VOC2007/Annotations/"+image_id+".xml")).getroot()
        for obj in root.findall('object'):
            difficult_flag = False
            if obj.find('difficult')!=None:
                difficult = obj.find('difficult').text
                if int(difficult)==1:
                    difficult_flag = True
            obj_name = obj.find('name').text
            if obj_name not in class_names:
                continue
            bndbox  = obj.find('bndbox')
            left    = bndbox.find('xmin').text
            top     = bndbox.find('ymin').text
            right   = bndbox.find('xmax').text
            bottom  = bndbox.find('ymax').text

            if difficult_flag:
                new_f.write("%s %s %s %s %s difficult\n" % (obj_name, left, top, right, bottom))
            else:
                new_f.write("%s %s %s %s %s\n" % (obj_name, left, top, right, bottom))


