import time
import cv2
import serial
import numpy as np
import matplotlib.pyplot as plt
import kociemba

# Envoi d'instructions à l'Arduino
def send_instructions(instructions):
    arduino.write(instructions.encode())
    print("Instructions sent to the Arduino:", instructions)


# Connexion à l'Arduino
arduino_port = 'COM14'  # Port COMX
baud_rate = 9600
arduino = serial.Serial(arduino_port, baud_rate)
print("Serial connection established with Arduino")

send_instructions("END")

# Ouverture de la vidéo
url = 'http://10.238.13.64:4747/video'
vid = cv2.VideoCapture(url)
win_size = [1920, 1080]

# Définition des positions des faces
rec_int = [200, 100]
rec_size = [300, 300]
front_pos = [400, 300]
pos = []
gap = int(rec_size[0] / 3)
small_rec_size = [10, 10]
for trash in range(3):
    for i in range(3):
        pos.append([rec_int[0] + 50 + gap * i, rec_int[1] + 50 + gap * trash])

# Initialisation de la liste core
core = []

# Capture du Rubik's Cube
rubik = []
casename = ['Up', 'Right', 'Front', 'Down', 'Left', 'Back']  # Liste des noms de faces
for i in range(6):
    color = np.array([])
    while(1):
        ret, frame = vid.read()
        cv2.rectangle(frame, rec_int, (rec_int[0] + rec_size[0], rec_int[1] + rec_size[1]), (0, 255, 0), 2)
        for trash in range(9):
            cv2.rectangle(frame, pos[trash], (pos[trash][0] + small_rec_size[0], pos[trash][1] + small_rec_size[1]), (255, 0, 0), 2)
        cv2.imshow(casename[i], frame)
        if cv2.waitKey(10) == ord('Z'):
            for trash in range(9):
                color = np.append(color, frame[pos[trash][1] + int(small_rec_size[0] / 2), pos[trash][0] + int(small_rec_size[1] / 2)])
                cv2.rectangle(frame, pos[trash], (pos[trash][0] + small_rec_size[0], pos[trash][1] + small_rec_size[1]), color[-3:], 2)
            corlor = color.reshape(9, 3)
            core.append(corlor[4])
            rubik.append(corlor)
            cv2.imshow(casename[i], frame[rec_int[1]:rec_int[1] + rec_size[1], rec_int[0]:rec_int[0] + rec_size[0]])
            if (casename[i] == 'Up'):
                cv2.moveWindow(casename[i], front_pos[0] - rec_size[0], front_pos[1])
            elif (casename[i] == 'Right'):
                cv2.moveWindow(casename[i], front_pos[0], front_pos[1] - rec_size[0] - 30)
            elif (casename[i] == 'Front'):
                cv2.moveWindow(casename[i], front_pos[0], front_pos[1])
            elif (casename[i] == 'Down'):
                cv2.moveWindow(casename[i], front_pos[0] + rec_size[0], front_pos[1])
            elif (casename[i] == 'Left'):
                cv2.moveWindow(casename[i], front_pos[0], front_pos[1] + rec_size[0] + 30)
            elif (casename[i] == 'Back'):
                cv2.moveWindow(casename[i], front_pos[0] + 2 * rec_size[0], front_pos[1])
            time.sleep(1)
            break
cv2.destroyAllWindows()
vid.release()

# Compare color
case = ['U','R','F','D','L','B']  # Liste des noms de faces
cube = ""
for trash in range(6):
    for i in range(9):
        cube = cube + case[sum(abs(rubik[trash][i] - core).transpose()).argmin()]

# Résolution du Rubik's Cube
solver = kociemba.solve (cube)
solution = solver
print("Solution:", solution)

# Attendre que l'on appuie sur une touche pour continuer
input("Press enter to start Rubik Solver...")
print("Arduino starting:")

# Envoi des instructions à l'Arduino
send_instructions("MOVE")
time.sleep(1.5)
send_instructions(solution)
send_instructions(" ")
#time.sleep()
#end_instructions("END")

# Fermeture de la communication série avec l'Arduino
arduino.close()
print("Serial Communication With Arduino is Closed")
