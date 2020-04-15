
import os
import shutil
path='/Volumes/study/study/FYP/dataset/endoscopy-artefact-detection-_ead_-dataset/trainingData_detection/'
    

#获取该目录下所有文件，存入列表中
fileList=os.listdir(path)

for i in fileList:
    #if i[-1]=='g':
    #    from_path = os.path.join('/Volumes/study/study/FYP/dataset/endoscopy-artefact-detection-_ead_-dataset/trainingData_detection/', i)
    #    to_path='/Volumes/study/study/FYP/dataset/endoscopy-artefact-detection-_ead_-dataset/picture/'
        
    if i[-1]=='t':
        from_path = os.path.join('/Volumes/study/study/FYP/dataset/endoscopy-artefact-detection-_ead_-dataset/trainingData_detection/', i)
        to_path='/Volumes/study/study/FYP/dataset/endoscopy-artefact-detection-_ead_-dataset/labels/'

        shutil.copy(from_path,to_path)
            
    print(i)