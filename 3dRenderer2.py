import pygame
import sys
from pygame.locals import*
from OpenGL.GL import*
from OpenGL.GLU import*

#######get faces indicies/ points########
"""import bpy

obj = bpy.context.object
mesh = obj.data

print("coor: ")
file1 = open("C:\\Users\\kondi\\OneDrive\\Desktop\\CordsFIles\\modelVerticies.txt", 'a')
for vert in mesh.vertices:
   xyz = vert.co.xyz
   print(f"{xyz[0]}, {xyz[1]}, {xyz[2]}")
   file1.write(f"({xyz[0]}, {xyz[1]}, {xyz[2]}),\n")




print("indices: ")
for face in mesh.polygons:
   print(f"{face.vertices[0]}, {face.vertices[1]}, {face.vertices[2]}")
   file2 = open("C:\\Users\\kondi\\OneDrive\\Desktop\\CordsFIles\\modelFaces.txt", 'a')
   file2.write(f"({face.vertices[0]}, {face.vertices[1]}, {face.vertices[2]}),\n")
"""



vertstxt = "C:\\Users\\kondi\\OneDrive\\Desktop\\CordsFIles\\modelVerticies.txt"
facestxt = "C:\\Users\\kondi\\OneDrive\\Desktop\\CordsFIles\\modelFaces.txt"
paints = [
    (255,0,0), #red
    (255,255,0), #yellow
    (0,255,0), #green
    (0,255,255), #cyan
    (255,0,0), #red
    (0,0,255)      #blue
        ]
def get_list(txtname):             #get our list from txt file and convert it to floats
    listname = []
    with open(txtname) as f:
        for line in f:
            line =line.rstrip(",\r\n").replace("(","").replace(")","").replace(" ",'')
            row = list(line.split(","))                                                 #line 41 & 42 are removing unnecessary stuff
            listname.append(row)
    listname = [[float(j) for j in i] for i in listname]           #convert each string to a float
    return listname
modelVerts = get_list(vertstxt)  #assign our values to the right lists
modelFaces = get_list(facestxt)
def drawpoints():                   #draw points
    glColor3fv((255,255,255))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(2.5)
    glBegin(GL_POINTS)
    for eachval in (modelVerts):
        glVertex3fv(eachval)
    glEnd()


def drawfaces():          #draw faces
    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    for eachface in (modelFaces):
        i=0
        for eachvert in eachface:

            i+=1
            if i >5:
                i = 0
            glColor3fv(paints[i])      #cool colors
            glVertex3fv(modelVerts[int(eachvert)])
    glEnd()


def main():
    pygame.init()
    display = (800,800)          #window size
    pygame.display.set_caption("OpenGLTest")  #caption
    FPS = pygame.time.Clock()        #fps
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)   #opengl display
    gluPerspective(45, 1, 0.1, 50.0)
    glTranslatef(0,-1,-5)      #set distance from screen (x,y,z)
    glRotatef(0,1,0,0)      #set rotation


    Up = False                # moving stuff around
    Down = False
    Left = False
    Right = False
    def moveObj():
        if Up:
            glRotatef(1,-90,1,1)
        if Down:
            glRotatef(1,90,1,1)
        if Left:
            glRotatef(-1, 0, 1, 0) #(angle,x,y,z)
        if Right:
            glRotatef(1, 0, 1, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_a:
                    Left = True
                if event.key == K_d:
                    Right = True
                if event.key == K_w:
                    Up = True
                if event.key == K_s:
                    Down = True
            if event.type == KEYUP:
                if event.key == K_a:
                    Left = False
                if event.key == K_d:
                    Right = False
                if event.key == K_w:
                    Up = False
                if event.key == K_s:
                    Down = False

        pygame.display.flip()

        drawfaces()
        #drawpoints()
        moveObj()
        FPS.tick(160)
main()
