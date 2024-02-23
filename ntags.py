import os
import pywintypes, win32file, win32con

def changeFileCreationTime(fname, newtime):
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    win32file.SetFileTime(winfile, wintime, None, None)

    winfile.close()


# COMMAND = "attach"
# COMMAND = "remove"
COMMAND = "ctime"

# eidtCtimeCmd = True

cntFiles   = 0
cntTouched = 0

ntags = os.listdir('.')
print(ntags)
for ntag in ntags :
    if not os.path.isdir(ntag):
        continue
    files = os.listdir(f'./{ntag}')
    for file in files:
        name, ext = os.path.splitext(file)
        dirpath = f'./{ntag}/'
        cntFiles +=1

        if COMMAND == 'attach':
            if "#ntag" in name:
                continue
            newfname = f'{name}#ntag_{ntag}{ext}'
            os.rename(dirpath + file, dirpath + newfname )
            cntTouched+=1
        elif COMMAND =='remove': #remove 
            if "#ntag" not in name:
                continue
            idx = name.find('#ntag')
            newfname = f'{name[:idx]}{ext}'
            os.rename(dirpath + file, dirpath + newfname )
            cntTouched+=1
        
        elif COMMAND =='ctime': #remove 
            changeFileCreationTime(dirpath + file,  os.path.getmtime(dirpath + file))
            cntTouched+=1

        else:
            break

print(f"!! {cntTouched}/{cntFiles} is completed !!")
