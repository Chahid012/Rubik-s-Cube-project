import time 
import cv2
import serial
import numpy as np
import matplotlib.pyplot as plt 


arduino_port = 'COM14'
baud_rate = 9600
arduino = serial.Serial(arduino_port, baud_rate)
print("Serial connection etablished wuth Arduino")



def send_instructions(instructions):
    arduino.write(instructions.encode())
    print("Instructions sent to the l'Arduino :", instructions)


# Generate Rubik
rubik = []
core = []
case = ['U','R','F','D','L','B']
casename = ['Up','Right','Front','Down','Left','Back']
caseposition = [[]]

# Open camera
url ='http://#IP:#port/video' 
vid = cv2.VideoCapture(url)
    # camera size
win_size = [1920,1080]

# cature zone (Square)
rec_int = [200,100]
rec_size = [300,300]

front_pos = [400,300]


# Create capture position
pos = []
gap = int(rec_size[0]/3)
small_rec_size = [10,10]
    # Create 9 point coordinates
for trash in range(3):
    for i in range(3):
        pos.append([rec_int[0]+50+gap*i,rec_int[1]+50+gap*trash])
        

# capture rubik
for i in range(6):
    color = np.array([])
        
    while(1):
        # Take video
        ret, frame = vid.read()
        
        # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Draw capture zone (rect)
        cv2.rectangle(frame, rec_int, (rec_int[0] + rec_size[0], rec_int[1] + rec_size[1]), (0, 255, 0), 2)
        
        # Draw capture position
        for trash in range(9):
            cv2.rectangle(frame, pos[trash], (pos[trash][0]+small_rec_size[0], pos[trash][1] + small_rec_size[1]), (255, 0, 0), 2)
            
            # print(frame[pos[trash][0],pos[trash][1]])
        
        cv2.imshow(casename[i],frame)
        # Wait for input key
        if cv2.waitKey(10) == ord('z'):
            # Capture color
            for trash in range(9):
                color = np.append(color,frame[pos[trash][1]+int(small_rec_size[0]/2), pos[trash][0]+int(small_rec_size[1]/2)])
                
                cv2.rectangle(frame, pos[trash], (pos[trash][0]+small_rec_size[0], pos[trash][1] + small_rec_size[1]), color[-3:], 2)
                # cv2.rectangle(frame, pos[trash], (pos[trash][0]+small_rec_size[0], pos[trash][1] + small_rec_size[1]), (0, 0, 255), 2)
                
            
            corlor = color.reshape(9,3)
            # Take core color of face
            core.append(corlor[4])
            # Save face colors
            rubik.append(corlor)
            # show the captured face 
            cv2.imshow(casename[i], frame[rec_int[1]:rec_int[1] + rec_size[1],rec_int[0]:rec_int[0] + rec_size[0]])
            # Move the window positon
            if (casename[i] == 'Up'):
                cv2.moveWindow(casename[i], front_pos[0] - rec_size[0] ,front_pos[1])
            elif (casename[i] == 'Right'):
                cv2.moveWindow(casename[i], front_pos[0], front_pos[1] - rec_size[0] - 30)
            elif (casename[i] == 'Front'):
                cv2.moveWindow(casename[i], front_pos[0],front_pos[1])
            elif (casename[i] == 'Down'):
                cv2.moveWindow(casename[i], front_pos[0] + rec_size[0],front_pos[1])
            elif (casename[i] == 'Left'):
                cv2.moveWindow(casename[i], front_pos[0], front_pos[1] + rec_size[0] + 30)
            elif (casename[i] == 'Back'):
                cv2.moveWindow(casename[i], front_pos[0] + 2* rec_size[0],front_pos[1])
                
            # cv2.imshow(casename[i], frame)
            time.sleep(1)
            # cv2.destroyAllWindows()
            break
        
cv2.destroyAllWindows()
vid.release()

# Compare color
cube = ""
for trash in range(6):
    for i in range(9):
        cube = cube + case[sum(abs(rubik[trash][i]-core).transpose()).argmin()]
        
print(cube)

face = []
face_text = []
for k in range(6):
    count = 0
    img = np.empty((3,3,3))
    for j in range(3):
        for i in range(3):            
            if cube[k*9+j*3+i] == "U":
                color = np.array([core[0][2],core[0][1],core[0][0]])/255
            elif cube[k*9+j*3+i] == "R":
                color = np.array([core[1][2],core[1][1],core[1][0]])/255
            elif cube[k*9+j*3+i] == "F":
                color = np.array([core[2][2],core[2][1],core[2][0]])/255
            elif cube[k*9+j*3+i] == "D":
                color = np.array([core[3][2],core[3][1],core[3][0]])/255
            elif cube[k*9+j*3+i] == "L":
                color = np.array([core[4][2],core[4][1],core[4][0]])/255
            elif cube[k*9+j*3+i] == "B":
                color = np.array([core[5][2],core[5][1],core[5][0]])/255
            img[j,i,:] = color
    face.append(img)
    face_text.append(cube[k*9:k*9+9])

fig = plt.figure()
fig.add_subplot(3, 4, 5)
plt.imshow(face[0], interpolation='nearest')
plt.title("Up")

fig.add_subplot(3, 4, 2)
plt.imshow(face[1], interpolation='nearest')
plt.title("Right")

fig.add_subplot(3, 4, 6)
plt.imshow(face[2], interpolation='nearest')
plt.title("Front")

fig.add_subplot(3, 4, 7)
plt.imshow(face[3], interpolation='nearest')
plt.title("Down")

fig.add_subplot(3, 4, 10)
plt.imshow(face[4], interpolation='nearest')
plt.title("Left")

fig.add_subplot(3, 4, 8)
plt.imshow(face[5], interpolation='nearest')
plt.title("Back")

plt.show(block = False)

Up = face_text[0]
Right = face_text[1]
Front = face_text[2]
Down = face_text[3]
Left = face_text[4]
Back = face_text[5]

cube_new = Up + Right + Front + Down + Left + Back

print(cube_new)


# Envoi des instructions à l'Arduino
instructions = "F_CLOCKWISE_90 B_COUNTERCLOCKWISE_90 R_CLOCKWISE_90"
send_instructions(instructions)

# Fermeture de la communication série avec l'Arduino
arduino.close()
print("Serial Communication With Arduino is Close")

cv2.destroyAllWindows()







