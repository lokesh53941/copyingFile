import os
import shutil
scr=input("enter path: ")
#a=os.path.dirname(scr)
#fileName=os.path.basename(scr)
#print(fileName)
base = os.path.splitext(scr)[1]
if base==".py":
    ext = os.path.splitext(scr)[0]
    dst=str(ext) + str('- Copy.py')
elif base==".pdf":
    ext = os.path.splitext(scr)[0]
    dst=str(ext) + str('- Copy.pdf')
elif base==".txt":
    ext = os.path.splitext(scr)[0]
    dst=str(ext) + str('- Copy.txt')
else:
    ext = os.path.splitext(scr)[0]
    dst=str(ext) + str('- Copy')
print(dst)
shutil.copy(scr,dst)

