import time
import cv2
import numpy as np

output = []

img = cv2.imread(input("Input file name: "))

height, width, channels = img.shape

print(f"height = {height} | width = {width}")
print("Формируем изображение....")
startform = time.time()
for w in range(width):
    print(f"Изображение отрисовано на {w} из {width}")
    for h in range(height):
        output.append(f"SetPixel({h},{w}, RGB({','.join(str(x) for x in list(img[h,w]))}));")
endform = time.time()

with open("output.pas", "w+") as file:
    print("Готовим файл output.txt...")
    file.write("uses GraphABC;\nbegin")
    for a in output:
        file.write("\n"+a)
    file.write("end.")
    file.flush()
    file.close()
    print("Готовый код для PascalABC.NET готов в файле output.pas")
    print(f"Затрачено времени на формирование кода: {endform-startform} sec")
    print(f"Затрачено времени на создание PascalABC.NET файла: {time.time()-endform} sec")
    input("Нажмите ENTER для закрытия данного окна...")