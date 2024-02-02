'''
    Autor: Iago Magalhães
    Descrição:
        - Realiza leitura de imagens com a WebCam;
        - Identifica pontos faciais;
        - 
'''

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    '''
        - sucesso: variável com valor booleano para status da captura;
        - frame: frame coletado através da WebCam.
    '''
    sucesso, frame = cap.read()

    if not sucesso:
        print('Ignorando o frame vazio da câmera.')
        continue

    cv2.imshow('Imagem da WebCam', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('c'):
        