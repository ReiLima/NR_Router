# -*- coding: cp1252 -*-
import cv2
import numpy as np

#Funcao que retorna a distancia euclidiana entre dois pontos
def distance ((start_x,start_y),(final_x,final_y)):

    start_x = int(start_x)
    start_y = int(start_y)
    final_x = int(final_x)
    final_y = int(final_y)
    
    distance_x = (start_x - final_x) ** 2
    distance_y = (start_y - final_y) ** 2
    distance = (distance_x + distance_y) ** 0.5
    return distance

#funcao que retorna uma matriz com o tamanho informado pelos parametros
def matrix (n_lines, n_columns):
    return [[0]*n_columns for i in range(n_lines)]

def function_properties((start_x,start_y),(final_x,final_y)):
    start_x = float(start_x)
    start_y = float(start_y)
    final_x = float(final_x)
    final_y = float(final_y)

    if(final_x == start_x):
        a = '|'
    else:
        a = (final_y - start_y)/(final_x - start_x)
        
    if(a == 0):
        b = final_y
    else:
        b = final_y - (a * final_x)    
    return (a,b)

def path((start_x,start_y),(final_x,final_y)):
    prop = function_properties((start_x,start_y),(final_x,final_y))
    a = prop[0]
    b = prop[1]

    path= []
    
    if(a == 0):
        for i in range(abs(final_x - start_x)):
            if(start_x < final_x):
                path.append((start_y,start_x + i))
            else:
                path.append((start_y,start_x - i))
    elif(a == '|'):
        for i in range(abs(final_y - start_y)):
            if(start_y < final_y):
                path.append((start_x,start_y + i))
            else:
                path.append((start_x,start_y - i))
    else:
        x = start_x
        y = start_y
        count = 0
        while((x,y) != (final_x,final_y)):
            if(start_x < final_x):
                x = start_x + count
            else:
                x = start_x - count
            y = int(a*x + b)
            path.append((x,y))
            count += 1

    final_path = []
    for i in range(len(path)):
        if(Map[path[i][0]][path[i][1]] == 0):
            final_path.append(path[i])
        else:
            break
    return final_path
    
#Abre o arquivo de imagem
img = cv2.imread("Maps/Map1.png")

#Exibe a altura da imagem
img_height = img.shape[0]
#print img_height

#Exibe a largura da imagem
img_width = img.shape[1]
#print img_width

#Cria uma matriz do mesmo tamanho da imagem
Map = matrix(img_height, img_width)

#Armazena os valores da imagem na matriz
for i in range(img_height):
    
    for j in range(img_width):
        
        #Se o ponto for branco armazena o valor 0
        if (img[j,i][0] == 255):
            Map[i][j] = 0
            
        #Se o ponto for preto armazena o valor 1
        else:
            Map[i][j] = 1

teste = path((141,50),(232,48))
#print teste[len(teste) - 1]

condicional = 0
while(condicional == 0):
    data_input = raw_input("Digite as coordenadas iniciais: ")
    startcell = data_input.split(",")
    startcell[0] = int(startcell[0])
    startcell[1] = int(startcell[1])

    if(Map[startcell[0]][startcell[1]] == 1):
        print ("\nCoordenadas Invalidas! Digite Novamente.\n")
    else:
        condicional = 1

condicional = 0
while(condicional == 0):
    data_input = raw_input("Digite as coordenadas finais: ")
    endcell = data_input.split(",")
    endcell[0] = int(endcell[0])
    endcell[1] = int(endcell[1])

    if(Map[endcell[0]][endcell[1]] ==1):
        print ("\nCoordenadas Invalidas! Digite Novamente.\n")
    else:
        condicional = 1
        
dist = distance((startcell[0],startcell[1]),(endcell[0],endcell[1]))
print 'Distancia Total:' , dist

caminho = path((startcell[0],startcell[1]),(endcell[0],endcell[1]))
for i in range(len(caminho) - 1):
        cv2.line(img,(caminho[i][0],caminho[i][1]),(caminho[i + 1][0],caminho[i + 1][1]),(255,0,255),2)

cv2.imshow('Map', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
