'''
    Autor: Iago Magalhães
    Descrição:
        - Realiza leitura de imagens com a WebCam;
        - Identifica pontos faciais com MediaPipe;
        - Exibi imagens coletadas da webcam com pontos faciais marcados com mediapipe.
'''

import cv2
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as facemesh:
    while cap.isOpened():
        '''
            - sucesso: variável com valor booleano para status da captura;
            - frame: frame coletado através da WebCam.
        '''
        sucesso, frame = cap.read()

        if not sucesso:
            print('Ignorando o frame vazio da câmera.')
            continue

        #Trnasformando imagem obtida por padrão em BGR pelo OpenCV para RGB, formato necessário para utilização do mediapipe
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        saida_facemesh = facemesh.process(frame)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        try:
            for face_landmarks in saida_facemesh.multi_face_landmarks:
                mp_drawing.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec = mp_drawing.DrawingSpec(color=(255,102,102), thickness = 1, circle_radius = 1),
                    connection_drawing_spec = mp_drawing.DrawingSpec(color=(102,204,0), thickness = 1, circle_radius = 1))
        except:
            pass

        cv2.imshow('Imagem da WebCam', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('c'):
            break

cap.release() #Pausa a captura de imagem
cv2.destroyAllWindows() #Destroi todas as janelas geradas