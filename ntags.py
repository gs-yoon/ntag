import os

COMMAND = "attach"
# COMMAND = "remove"

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
        cntFiles +=1

        if COMMAND == 'attach':
            if "#ntag" in name:
                continue
            dirpath = f'./{ntag}/'
            newfname = f'{name}#ntag_{ntag}{ext}'
            os.rename(dirpath + file, dirpath + newfname )
            cntTouched+=1
        else: #remove 
            if "#ntag" not in name:
                continue
            dirpath = f'./{ntag}/'
            idx = name.find('#ntag')
            newfname = f'{name[:idx]}{ext}'
            os.rename(dirpath + file, dirpath + newfname )
            cntTouched+=1
        

print(f"!! {cntTouched}/{cntFiles} is completed !!")