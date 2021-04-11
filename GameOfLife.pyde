#Juego de la vida de Conway_ Por Jimmy Amezquita.
#Click en las celdas para manualmente dar o quitar la vida.
#Pulsa "r" para celdas aleatorias.
#Pulsa "b" para borrar las celdas.
#Pulsa "espacio" para pausar o ejecutar el juego.
#"+" para aumentar la velocidad. 
#"-" para reducir la velocidad.
#Pulsa 1,2,3,o 4 para ver los patrones configurados "Recuerda borrar"

import random
boton=False
lista=[]
ve=30
w=20
h=20

for i in range(25):
    sublista=[]
    for a in range(25):
        sublista.append(False)
    
    lista.append(sublista)





def setup():

    background(0)
    frameRate(10)
    size(500,600)
    k=0
    #Dibujar las lineas de las celdas
    for i in range(25):
     fill(0, 0, 0)
     stroke(16)
     line(k,0,k,500)
     line(0,k,500,k)
     k+=20


    
def draw():
    global x
    global y
    global boton
    global pos_x
    global pos_y
    
    if mouseY<500:
        pos_x=int(mouseX/20)
        pos_y=int(mouseY/20)
      
        x=20*pos_x
        y=20*pos_y
    
    for i in range(25):
        for b in range(25):
            if lista[b][i]==False:
                fill(0)
                square(i*20,b*20,20)
            else:
                fill(255)
                square(i*20,b*20,20)
    juego_pausa()
    
    
#Verifica y busca que celdas viven y que celdas mueren   
def Vef_vida():
    vivira=[]
    morira=[]
    for i in range(25):
        for a in range(25):
            if lista[a][i]==True:
                
                p=reglas_juego(a,i)
                
                if p==3 or p==2:
                    vivira.append([a,i])
            
                else:
                    morira.append([a,i])

                                        
            else:
                p=reglas_juego(a,i)
                if p==3:

                    vivira.append([a,i])
                                                                                
         
    for i in range(len(vivira)):
        lista[vivira[i][0]][vivira[i][1]]=True                
    
    for i in range(len(morira)):
        lista[morira[i][0]][morira[i][1]]=False                
    
#Evalua la vida de los vecinos de una celda.
def reglas_juego(a,i):
     
        p=0
        if i<24 and lista[a][i+1]==True:
            p+=1
        if i<24 and a>0 and lista[a-1][i+1]==True:
            p+=1     
        if i<24 and a<24 and lista[a+1][i+1]==True:
            p+=1                                  
        
        if i>0 and lista[a][i-1]==True:
            p+=1
        
        if i<24 and a>0 and lista[a-1][i-1]==True:
            p+=1     
        if i>0 and a<24 and lista[a+1][i-1]==True:
            p+=1   
            
                                                
        if a<24 and lista[a+1][i]==True:
            p+=1
        if a>0 and lista[a-1][i]==True:
            p+=1 
        
        return p    
def juego_pausa():
    if boton:
        fill(0)
        triangle(230, 520, 230, 570, 270, 545 )
        fill(255)
        rect(230, 520, 15, 50)
        rect(260 , 520,15, 50)            
        Vef_vida()
    else:     
        fill(0) 
    
        rect(230, 520, 15, 50)
        rect(260 , 520, 15, 50)
        fill(255)
        triangle(230, 520, 230, 570, 270, 545 )
         
        
def keyPressed():
    global boton
    global ve
    if boton and key==" ":

        boton=False
    
    else:

        boton=True        
    if key=="r":
        
        for i in range(25):
        
            for a in range(25):
                d=random.randint(1,2)
                if d==1:
                    lista[a][i]=True
                else:lista[a][i]=False    

    if key=="b":
        for i in range(25):
            for a in range(25):
                    lista[a][i]=False
    if key=="+":
        if ve<120:
         print(ve)
         ve+=3
         frameRate(ve)
    if key=="-":
        if ve>3:
         print(ve)
         ve-=3      
         frameRate(ve)      
  ##Patrones configurados
    if key=="1":##Blinker
        lista[13][13]=True
        lista[13][14]=True
        lista[13][15]=True   

    if key=="2":##Toad
        lista[13][13]=True
        lista[13][14]=True
        lista[13][15]=True   
        
        lista[14][12]=True
        lista[14][13]=True
        lista[14][14]=True

    if key=="3":##glider
        lista[13][13]=True
        lista[11][14]=True
        lista[13][14]=True
        lista[12][15]=True 
        lista[13][15]=True   
        
    if key=="4":##Penta-decathlon
        lista[6][12]=True
        lista[7][12]=True
        lista[8][11]=True
        lista[8][13]=True
        lista[9][12]=True
        lista[10][12]=True
        lista[11][12]=True
        lista[12][12]=True
        lista[13][11]=True
        lista[13][13]=True
        lista[14][12]=True
        lista[15][12]=True

def mouseClicked():
    if(mouseX>x and mouseX<x+w and mouseY> y and mouseY<y+h):

        if lista[pos_y][pos_x]==False :
            lista[pos_y][pos_x]=True

        else:
            lista[pos_y][pos_x]=False

        
    





                          
