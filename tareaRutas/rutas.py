import numpy as np

matriz = np.array ([[-3,-3,2,-3,3,-2,-2,1,2,0,2,0,1],
                    [2,3,np.nan,-1,-1,3,2,0,-3,-3,2,2,1],
                    [1,-3,-3,2,3,1,3,3,2,1,-2,-2,3],
                    [0,0,3,0,3,-3,-2,-3,0,2,2,1,1],
                    [2,-1,-1,-3,3,3,0,-3,1,-2,2,0,1],
                    [0,3,-1,1,-1,-2,2,-2,2,-1,-2,-3,0],
                    [0,3,2,0,1,1,2,3,-1,-3,0,0,-2],
                    [3,3,-3,-2,3,-3,-1,-3,3,-2,2,-2,-1],
                    [-2,-2,1,0,-1,0,3,0,0,-2,2,-3,-1],
                    [-3,3,0,-1,-3,1,2,-3,2,-3,0,2,-2],
                    [-3,-3,-3,3,-2,0,-2,-3,1,0,1,-1,-2],
                    [-1,0,1,2,1,0,np.nan,0,-3,3,3,-2,-1],
                    [1,-3,1,0,1,2,3,1,-2,3,3,0,3]])

def checarAlrededor(pos,cola,finish,tipo):
    print(f'Estoy en: {pos} -> {matriz[pos]}')
    cola.append(pos)
    y,x = pos
    yf,xf = finish
    arriba = (max([0,y-1]),x)
    abajo = (min([12,y+1]),x)
    izq = (y,max([0,x-1]))
    der = (y,min([12,x+1]))
    min_max_found = [(0,0),(0,0),False,(0,0)]

    if arriba == finish:
        print("Voy arriba")
        cola.append(arriba)
        return [(0,0),(0,0),True, arriba]
    if abajo == finish:
        print("Voy abajo")
        cola.append(abajo)
        return [(0,0),(0,0),True, abajo]
    if izq == finish:
        print("Voy izquierda")
        cola.append(izq)
        return [(0,0),(0,0),True, izq]
    if der == finish:
        print("Voy derecha")
        cola.append(der)
        return [(0,0),(0,0),True, der]
    
    direcciones = [arriba,abajo,izq,der]

    if cola.count((y-1,x)) or y == 0:
        # si el de arriba esta en la cola, removerlo
        direcciones.remove(arriba)
    if cola.count((y+1,x)) or y == yf or y == 12:
        # si el de abajo esta en la cola, removerlo
        direcciones.remove(abajo)
    if cola.count((y,x-1)) or x == 0 or (y == yf and x < xf):
        # si el de la izq esta en la cola, removerlo
        direcciones.remove(izq)
    if cola.count((y,x+1)) or x == 12 or (y == yf and x > xf):
        # si el de la der esta en la cola, removerlo
        direcciones.remove(der)

    if not direcciones:
          print("Sin ruta valida, haciendo rollback")
          min_max_found = checarAlrededor(cola[len(cola)-2],cola,finish,tipo)
          return min_max_found
    
    filtered = []
    for dir in direcciones:
        filtered.append(matriz[dir])
    
    # Para la ruta minima
    if tipo == 'min':
        minimo = min(filtered)
        if matriz[abajo] == minimo and direcciones.count(abajo):
                min_max_found[0] = (y+1,x)
                print("Voy abajo")
        elif matriz[der] == minimo and direcciones.count(der):
                min_max_found[0] = (y,x+1)
                print("Voy derecha")
        elif matriz[izq] == minimo and direcciones.count(izq):
                min_max_found[0] = (y,x-1)
                print("Voy izquierda")
        elif matriz[arriba] == minimo and direcciones.count(arriba):
                min_max_found[0] = (y-1,x)
                print("Voy arriba")

    #Para la ruta maxima
    if tipo == 'max':
        maximo = max(filtered)
        if matriz[abajo] == maximo and direcciones.count(abajo):
                min_max_found[1] = (y+1,x)
                print("Voy abajo")
        elif matriz[der] == maximo and direcciones.count(der):
                min_max_found[1] = (y,x+1)
                print("Voy derecha")
        elif matriz[izq] == maximo and direcciones.count(izq):
                min_max_found[1] = (y,x-1)
                print("Voy izquierda")
        elif matriz[arriba] == maximo and direcciones.count(arriba):
                min_max_found[1] = (y-1,x)
                print("Voy arriba")

    
    return min_max_found

def ruta(tipo):
    start = (1,2)
    finish = (11,6)
    costo = 0
    pos_actual = start
    cola = [start]
    print("================================================================")
    while pos_actual != finish:
          print(f'Costo acumulado: {costo}')
          if tipo == 'max' :
            minPos, maxPos, found, fpos = checarAlrededor(pos_actual,cola,finish,tipo)
            pos_actual = maxPos
          if tipo == 'min' :
            minPos, maxPos, found, fpos = checarAlrededor(pos_actual,cola,finish,tipo)
            pos_actual = minPos
          if found: pos_actual = fpos
          if not found: costo += matriz[pos_actual]
          print(cola)
          input("Continuar [Enter]...\n")
          
    if tipo == 'max' : print('RUTA MAXIMA ENCONTRADA:')
    if tipo == 'min' : print('RUTA MINIMA ENCONTRADA:')
    print(f'Costo total: {costo}\nRuta: {(start, finish)} ->\n {cola}\n')
    print("================================================================")

def algoritmoDeRutas():
    opcion = ""
    while opcion != '3':
      print(matriz)
      print("================================================================")
      opcion = input("Elige la ruta a calcular\n 1.- Ruta Minima de 'I' a 'F' (1,2) - (11,6)\n 2.- Ruta Maxima de 'I' a 'F' (1,2) - (11,6)\n 3. Salir\n Opcion: ")
      if opcion == "1":
        ruta("min")
      elif opcion == "2":
        ruta("max")
      elif opcion == "3":
        print("Fin de la ejecucion")
      else:
        print("Opcion inválida")
        print("================================================================")

algoritmoDeRutas()