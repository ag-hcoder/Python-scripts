import os
files = os.listdir()
os.chdir(os.getcwd())
files.remove('main.py')


def move(files, foldername):
    for file in files:
        os.replace(file, f'{foldername}/{file}')


def createFolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


createFolder('png')
createFolder('jpeg')
createFolder('jpg')

pngimg = [file for file in files
          if (os.path.splitext(file)[1].lower() == '.png')]
# print(pngimg)
jpgimg = [file for file in files
          if (os.path.splitext(file)[1].lower() == '.jpg')]
jpegimg = [file for file in files
           if (os.path.splitext(file)[1].lower() == '.jpeg')]
move(pngimg, 'png')
move(jpgimg, 'jpg')
move(jpegimg, 'jpeg')
