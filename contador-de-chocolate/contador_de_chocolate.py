import cv2 as cv
from ultralytics import YOLO

# importando o modelo customizado e o vídeo usado como exemplo
modelo = YOLO('./modelos/detector_de_chocolate.pt')
video = cv.VideoCapture('./videos/chocolates.mp4')
chocolates_contados = []

# faz um looping em cada frame do vídeo
while video.isOpened():
    rect, frame = video.read()

    if rect:
        # reduzindo o tamanho da imagem
        frame_reduzido = cv.resize(frame, (1000, 700))

        # variaveis que vão ajudar a criar os contornos
        largura, comprimento, _ = frame_reduzido.shape
        linha = [(0, largura//2), (comprimento, largura//2)]

        # detectando os chocolates
        resultado = modelo.track(frame_reduzido, show=False, classes=[0], verbose=False, persist=True)[0]
        caixas = resultado.boxes

        # desenhando a caixa de texto (total de chocolates)
        (comprimento_texto, largura_texto), _ = cv.getTextSize(f'Total = {len(chocolates_contados) + 5}', cv.FONT_HERSHEY_DUPLEX, 1, 2)
        cv.rectangle(frame_reduzido, (0, 0), (comprimento_texto + 65, 50), (255, 255, 255), -1)
        cv.putText(frame_reduzido, f'Total = {len(chocolates_contados) + 5}', (7, 37), cv.FONT_HERSHEY_DUPLEX, 1.3, (0, 0, 255), 2)
        
        # desenhando contornos nos chocolates
        for caixa in caixas:
            esquerda, cima, direita, baixo = caixa.xyxy.int().tolist()[0]
            circulo = (esquerda+(direita-esquerda)//2, cima+(baixo-cima)//2)
            cv.rectangle(frame_reduzido, (esquerda, cima), (direita, baixo), (255, 0, 0), 2)
            cv.circle(frame_reduzido, circulo, 0, (0, 0, 255), -1)

            # realizando a contagem
            if linha[0][0] < circulo[0] < linha[1][0] and linha[0][1] - 5 < circulo[1] < linha[0][1] + 5:
                if caixa.id not in chocolates_contados:
                    chocolates_contados.append(caixa.id)

        # desenhando a linha de contagem
        cv.line(frame_reduzido, linha[0], linha[1], (0, 0, 255), 2)

        # apresentando os frames
        cv.imshow('Contador de Chocolate', frame_reduzido)

        # pressione "q" para finalizar o código
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# fechando todas as janelas
video.release()
cv.destroyAllWindows()