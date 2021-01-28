import os
import shutil

def CreateIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

imgExt = ['.png','.jpg','.jpeg']
docExt = ['.txt','.docx','.doc','.pdf','.xls','.xlsx','.ppt','.pptx','.odt','.ods']
mediaExt = ['.mp3','.mp4','.mkv','.gif','.flv']

files = os.listdir()
# remove current file name
files.remove(__file__.split('\\')[-1])

# print(files)
for file in files:
    if os.path.splitext(file)[1] == "":
        continue
    else:
        if os.path.splitext(file)[1] in imgExt:
            folder = CreateIfNotExist('images')
            shutil.move(file, folder)
        elif os.path.splitext(file)[1] in docExt:
            folder = CreateIfNotExist('documents')
            shutil.move(file, folder)
        elif os.path.splitext(file)[1] in mediaExt:
            folder = CreateIfNotExist('media')
            shutil.move(file, folder)
        else:
            folder = CreateIfNotExist(os.path.splitext(file)[1][1:])
            shutil.move(file, folder)
            


    
