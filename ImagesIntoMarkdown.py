import os

TempPath=r'...' #Your destination path
TempFile=os.path.join(TempPath,'_Temp.md')
Help='''Command:
name, iname, ctime, mtime; named, ... : Sort source Files according to file name, the integar in file name, created time, or modified time. 'd' signals descending. 
Else is default.
'''

while(True):
    Input=input('Input source path or "help" : ')
    if Input=='help':
        print(Help)
        continue
    SourcePath=Input
    Command=input('Input command: ')
    SourcePictures=os.listdir(SourcePath)
    os.chdir(SourcePath)
    if Command=='name':
        sort(SourcePictures)
    elif Command=='iname':
        SourcePictures.sort(key=lambda File:int(File.split('.')[0]))
    elif Command=='ctime':
        SourcePictures.sort(key=lambda File:os.path.getctime(File))
    elif Command=='mtime':
        SourcePictures.sort(key=lambda File:os.path.getmtime(File))
    elif Command=='named':
        SourcePictures.sort(reverse)
    elif Command=='inamed':
        SourcePictures.sort(key=lambda File:int(File.split('.')[0]),reverse=True)
    elif Command=='ctimed':
        SourcePictures.sort(key=lambda File:os.path.getctime(File),reverse=True)
    elif Command=='mtimed':
        SourcePictures.sort(key=lambda File:os.path.getmtime(File),reverse=True)
    with open(TempFile,'w') as TempFileH:
        for SourcePicture in SourcePictures:
            TempFileH.write(r'![](%s)'%(os.path.join(SourcePath,SourcePicture)))
    os.startfile(TempFile)
    break
