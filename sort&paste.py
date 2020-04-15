import os
import shutil
def fun(xml_path,image_path,dest_path):
    for f in os.listdir(xml_path):
        name=os.path.splitext(f)[0] #取出这个文件的名字
        for i in os.listdir(image_path):
            if os.path.splitext(i)[0]==f:
                shutil.copyfile(i,dest_path)

def main():
    xml_path=input('输入xml目录')
    print('我选择的目录是:  %s' % xml_path)
    imagepath=input('输入图片库的路径')
    destination=input('输入导出图片的路径')
    fun(xml_path,imagepath,destination)

if __name__=='_main_':
    main()