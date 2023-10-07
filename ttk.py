import cv2

# Inicialize a câmera
cap = cv2.VideoCapture(0)

while True:
    # Capture quadro a quadro
    ret, frame = cap.read()

    # operações no quadro vêm aqui
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Exiba o quadro resultante
    cv2.imshow('frame', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Quando tudo estiver pronto, libere a captura
cap.release()
cv2.destroyAllWindows()


