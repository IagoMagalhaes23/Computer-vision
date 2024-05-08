# Computer Vision

## Introdução
Buscando aprender mais sobre Visão Computacional e seus principais recursos. Tenho buscado conhecimento em diferentes plataformas e desenvolvendo aplicações em Python para praticar e criar habilidades nesse campo. Neste repositório busco aprender sobre Yolo e suas versões, Detectron 2, MediaPipe, OpenCV, Scikit Image e et.

## Projetos

### Projeto 1:
- Análise facial para detecção de sono
Na primeira etapa do curso aprendir sobre como estruturar um projeto de visão computacional, utilizar a captura de imagens em tempo real com OpenCv, detectar faces com MediaPipe Face Mesh e construir uma visualização de pontos daciais. O resultado pode ser visualizado na imagem abaixo.

Na segunda etapa do curso foi apresentado como identificar as coordenadas e os pontos da solução Face mesh, localizar e exibir os pontos que representam os olhos direito e esquerdo, interpretar as coordenadas do mediapipe e calcular o valor de EAR.

Na terceira aula foi abordado sobre como localizar e exibir os pontos que representam a boca, e por fim formular e implementar o cálculo do índice de nível de abertura da boca, o MAR.

Na última aula, conseguir aprender sobre como utilizar as funcionalidades do mediapipe para identificar o olho, contar o número de piscadas, verificar a frequencia de eventos e identificar se o usuário está dormindo ou não.

Sugestões de melhorias futuras: integrar o projeto de análise facial ao um sistema com microcontrolador e emitir bips ou efeitos sonoros e luminosos para ajudar o usuário acordar e alertar as pessoas em volta para auxiliar na situação.

### Projeto 2:
- Depth Anything: Como Criar Mapas de Profundidade

A percepção de profundidade é o que nos permite interpretar o mundo tridimensional a partir de imagens bidimensionais projetadas em nossas retinas. Essa habilidade evoluiu como um aspecto crucial para a sobrevivência, possibilitando aos humanos navegar pelo ambiente, evitar predadores e localizar recursos.

O cérebro humano realiza essa façanha por meio de uma série de interpretações das informações visuais, onde a sobreposição do campo visual binocular fornece uma rica percepção de profundidade.

Além da visão binocular, essa percepção é enriquecida por várias pistas monoculares (depth cues), elementos no ambiente que permitem ao observador único inferir a profundidade mesmo com um olho fechado. Entre essas pistas estão occlusão, tamanho relativo, sombras projetadas, e perspectiva linear.

Esses mesmos princípios e mecanismos de percepção encontram um paralelo na Visão Computacional, onde a essência da estimativa também reside em capturar a estrutura espacial de uma cena para representar com precisão seus aspectos tridimensionais.

O modelo Depth Anything, introduzido no trabalho “Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data”, representa um avanço significativo em estimativa de profundidade monocular. Baseado na arquitetura DPT (Dense Prediction Transformer), foi treinado em um vasto conjunto de dados com mais de 62 milhões de imagens não rotuladas.

O sucesso desta abordagem é atribuído a duas estratégias principais.

- A utilização de ferramentas de data augmentation para estabelecer um target de otimização mais desafiador.
- Uso de supervisão auxiliar para assegurar a herança de priores semânticos a partir de codificadores pré-treinados.

A capacidade de generalização do Depth Anything, testada em seis conjuntos de dados públicos e em fotografias capturadas aleatoriamente, superou algumas métricas de modelos existentes, como MiDaS v3.1 e ZoeDepth.

Essência da Percepção de Profundidade Monocular: A estimativa de profundidade monocular é fundamental para compreender a estrutura espacial de uma cena a partir de uma única imagem, permitindo aplicações como reconstrução 3D de cenas.

Avanços com Depth Anything: Representando um salto significativo na percepção de profundidade monocular, o modelo Depth Anything utiliza a arquitetura DPT e foi treinado em um conjunto de dados extenso, mostrando excelente capacidade de generalização.

Aplicação Prática: O artigo fornece instruções detalhadas para testar a estimativa de profundidade com imagens e vídeos, facilitando a experimentação prática e a visualização dos resultados do modelo Depth Anything. A imagem 01 apresenta um pouco de como o algoritmo pode ser utilizado.

![image](https://github.com/IagoMagalhaes23/Computer-vision/assets/65053026/82f76c6e-5d49-46ee-b817-e13306d28d15)

### Projeto 3:
- YOLO: Segmentação de Objetos | A Poderosa Capacidade do YOLO Explorada Passo a Passo
Descubra a incrível capacidade de segmentação de objetos do YOLO neste tutorial abrangente! 🚀 Aprenda como o YOLO (You Only Look Once) pode identificar e delimitar objetos em tempo real, revolucionando a visão computacional. Aqui exploramos as várias funcionalidades do YOLO, incluindo detecção de objetos, classificação e segmentação, fornecendo insights valiosos para iniciantes e entusiastas avançados de IA e visão computacional.

### Projeto 4:
No projeto 04, com a ajuda do canal WellingtonDev25 (nome de usuário no GitHub) criamos um pequeno programa para prever a distânica da mão em relação a camera.

## Referências
- (Projeto Análise facial): Curso de Visão Computacional: Análise facial; Curso presente na Alura com aulas ministradas pela professora Mirla Costa.
- [Depth Anything: Como Criar Mapas de Profundidade](https://sigmoidal.ai/depth-anything-como-criar-mapas-de-profundidade/)
- [YOLO: Segmentação de Objetos | A Poderosa Capacidade do YOLO Explorada Passo a Passo](https://youtu.be/r6tQtIeWXu8?si=uIERQkTcDl0OFMCq)
- [Distância Mão](https://github.com/WellingtonDev25/distancia_mao/tree/main