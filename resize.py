import os
from PIL import Image

print("Скрипт пропорционально  уменьшает размер картинки.")
print("------------------------------------------")
zzz = int(input("Введите наибольшую сторону фотки в пикселах: "))
d = input("Введите каталог: ")

ff = 0
dd = 0

def res(file_name, zzz_f):
    try:
        original_image = Image.open(file_name)
        width, height = original_image.size
        print('Размер {wide}  {height} '.format(wide=width, height=height))
        if width > zzz_f or height > zzz_f:
            original_image.thumbnail([zzz_f, zzz_f], Image.ANTIALIAS)
            original_image.save(file_name)
    except:
        pass

for dirpath, dirnames, filenames in os.walk(d):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
        dd += 1
    # перебрать файлы
    for filename in filenames:
        ext = os.path.splitext(filename)[1]
        if "jpg" in ext or "png" in ext or "jpeg" in ext or "JPG" in ext:
            print(os.path.join(dirpath, filename))
            res(os.path.join(dirpath, filename), zzz)
            ff += 1

input("DONE")
