# Contador-de-Chocolate

## Descrição
Esse projeto é um exemplo prático de como a Visão Computacional pode ser usada para automatizar tarefas no setor industrial. Neste caso, a contagem de chocolates se movendo em uma esteira. Para a detecção dos chocolates foi usado o modelo yolov8n.pt (nano). Entretanto, esse modelo não possui a capacidade de detectar chocolates de forma nativa. Portanto, usei alguns frames do próprio vídeo para realizar um Aprendizado Supervisionado (o modelo, já treinado, está disponível na pasta "modelos").

## Bibliotecas Necessárias
- opencv-python
- ultralytics

## Resultado
![contador-de-chocolate](https://github.com/user-attachments/assets/fe8ac2ef-3827-4b74-a3a5-77af4c167b9a)
