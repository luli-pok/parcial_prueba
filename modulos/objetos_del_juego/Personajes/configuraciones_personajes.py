import pygame as py


def reescalar_imagenes(diccionario_animaciones, tamaño):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (tamaño))

def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes



personaje_quieto = [py.image.load(r"assets\imagenes\personaje_principal\InuYasha_quieto.png")]

personaje_camina_derecha = [py.image.load(r"assets\imagenes\personaje_principal\InuYasha_caminando_derecha_1.png"),
                            py.image.load(r"assets\imagenes\personaje_principal\InuYasha_caminando_derecha_2.png")]

personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta_izquierda = [py.image.load(r"assets\imagenes\personaje_principal\InuYasha_saltando-1.png (1).png")]

personaje_salta_derecha = rotar_imagen(personaje_salta_izquierda)
