'''
import os
import random
from tqdm import tqdm


# ==================可能需要修改的地方=====================================#
g_root_path = "/Users/maxgeng/Study/FYP/Code/dataset/Latest/Sorted_3_21_latest/"
xmlfilepath = "Train_AUG_annotation"  # 标注文件存放路径
saveBasePath = "/Users/maxgeng/Study/FYP/Code/dataset/Latest/Sorted_3_21_latest/"  # ImageSets信息生成路径
# ==================可能需要修改的地方=====================================#

os.chdir(g_root_path)
total_xml = os.listdir(xmlfilepath)
num=len(total_xml)
print("train  size", num)

for j in total_xml:
    name=os.path.splitext(j)[0]+"\n"
    ftrain=open(saveBasePath + "train_aug.txt", "w")
    ftrain.write(name)
ftrain.close
'''


import os
import random
from tqdm import tqdm

for i in tqdm(range(1000)):
    # ==================可能需要修改的地方=====================================#
    g_root_path = "/Users/maxgeng/Study/FYP/Code/dataset/theFianlVocDateset/"
    xmlfilepath = "TrainAugAnnCopy"  # 标注文件存放路径
    saveBasePath = "/Users/maxgeng/Study/FYP/Code/dataset/theFianlVocDateset/ImageSet/ "  # ImageSets信息生成路径
    # ==================可能需要修改的地方=====================================#

    os.chdir(g_root_path)
    total_xml = os.listdir(xmlfilepath)
    num = len(total_xml)
    xml_list = range(num)
    #tv = int(num * trainval_percent)
    #tr = int(tv * train_percent)
    #trainval = random.sample(xml_list, tv)
    #train = random.sample(trainval, tr)

    #print("train and val size", tv)
    print("train  size", num)
    #ftrainval = open(saveBasePath + "trainval.txt", "w")
    #ftest = open(saveBasePath + "test.txt", "w")
    ftrain = open(saveBasePath + "finalTrain.txt", "w")
    #fval = open(saveBasePath + "val.txt", "w")

    for i in xml_list:
        name = total_xml[i][:-4] + "\n"
        ftrain.write(name)

    #ftrainval.close()
    ftrain.close()
    #fval.close()
    #ftest.close()
    pass
