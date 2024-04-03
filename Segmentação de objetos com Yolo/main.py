import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

#Rodando o yolo para uma imagem, salva dados em txt e salvando as imagens com os resultados
results = model('yolo.png', save=True, save_txt=True)

img = ''

image = mpimg.imread(img)
plt.imshow(image)
plt.axis('off')
plt.show()