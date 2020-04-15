# coding=utf-8
import os, random, shutil
def moveFile(fileDir):
    pathDir = os.listdir(fileDir)  # 取图片的原始路径
    filenumber = len(pathDir)
    rate = 0.5 # 自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber = int(filenumber * rate)  # 按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片
    for name in sample:
        shutil.move(os.path.join(fileDir,name),os.path.join(tarDir,name))
        print(name)
    return

if __name__ == '__main__':
    tarDir = '/Volumes/study/study/FYP/ImageData/test/test_xml'   # 移动到新的文件夹路径
    ori_path = '/Volumes/study/study/FYP/ImageData/test/xml_listed' # 最开始train的文件夹路径
    #for firstPath in os.listdir(ori_path):
    #    fileDir = os.path.join(ori_path, firstPath)  # 原图片文件夹路径
    moveFile(ori_path)
