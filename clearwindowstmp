import os,shutil
def clearfile(dir):
    for file in os.listdir(dir):
        fullpath=os.path.join(dir,file)
        if os.access(fullpath,os.F_OK):
            shutil.rmtree(fullpath,ignore_errors=True)
if __name__=='__main__':
    deldir=[r'C:\Users\user\AppData\Local',r'C:\Users\user\Documents\Tencent Files\qqnumber\Image']
    for Del_dir in deldir:
        clearfile(Del_dir)

        
