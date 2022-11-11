from functools import reduce

def process_matrix(matrix):
    """
    recibe una lista de numeros y devuelve una nueva con los elementos cambiados
    cada elemento de la nueva, sera el promedio del valor antiguo y de sus vecinos
    """
    # Creo una lista vacia donde ire acumulando
    processed_matrix = []
    coordenates = []
    if len(matrix) == 1:
        processed_matrix = process_list(matrix[0])
    else:
            
        # por cada elemento de la lista ...
        for i, fila in enumerate(matrix):
            list_of_lists = []
            processed_matrix.append(list_of_lists)
            coordenates_list = []
            coordenates.append(coordenates_list)
            for j, value in enumerate(fila):
                
                coordenates_list.append([i, j])     
                new_element = process_element(matrix, coordenates)
                # lo aniado a la lista
                list_of_lists.append(new_element)
    # devuelvo la nueva lista
    return processed_matrix

def process_element(matrix, coordenates):
    """
    Recibe una lista y un indice de un elemento, calcula su promedio con sus vecinos
    y devuelve dicho promedio
    """
    # Obtengo la lista de vecinos
    indices = get_neighbour_indices(matrix, coordenates)
    values = get_neighbour_values(matrix, indices)

    # calculo su promedio
    average = get_average(values)

    # devuelvo el valor final
    return average
def first_coord(coordenates):
    return coordenates[0]

def second_coord(coordenates):
    return coordenates[1]


def get_neighbour_indices(matrix, list_of_coordenates):
    indexes = []
    final_list = []
    # ya tengo las coordenadas que voy a recibir de una en una, del que se va a evaluar en este momento, asi que busco sus vecinos con ifs
    # primero con las condiciones de la fila (i), y luego de la columna(j), comprobando que los vecinos existen en la matriz
    for i in list_of_coordenates:
        new_list_neighbours = []
        indexes.append(new_list_neighbours)
        clean_list = []
        final_list.append(clean_list)
        
        for j in i:

            #neighbour_right
            new_list_neighbours.append([first_coord(j), second_coord(j) +1])
            #neighbour_left
            new_list_neighbours.append([first_coord(j), second_coord(j) -1])
            #neighbour_down 
            new_list_neighbours.append([first_coord(j) +1, second_coord(j)])
            #neighbour_up
            new_list_neighbours.append([first_coord(j)-1, second_coord(j)])
            #incluyo al propio elemento como vecino de si mismo
            new_list_neighbours.append([first_coord(j), second_coord(j)])

            #new_list_neighbours = list(filter(lambda coord: coord[0] >= 0 and coord[0] < len(matrix) and coord[1] >= 0 and coord[1] < len (matrix[0]), new_list_neighbours))
            filtered_list_neighbours = filter_neighbours(matrix, new_list_neighbours)
            clean_list.append(filtered_list_neighbours)
            
    return final_list

def filter_neighbours(matrix, list_neighbours):
    new_list = []
    for lista in list_neighbours:
         if lista[0] >= 0 and lista[0] < len(matrix) and lista[1] >= 0 and lista[1] < len(matrix[0]):
            new_list.append(lista)
                    
    return new_list

def get_neighbour_values(matrix, indices):
    values = []
    for i in indices:
        for j in i:
            for e in j:
                values.append(matrix[e[0]][e[1]])
    return values               

def get_average(numbers):
    """
    Recibe una lista de numeros y devuelve su promedio
    """   
    return reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers)


def process_list(matrix):
    """
    recibe una lista de numeros y devuelve una nueva con los elementos cambiados
    cada elemento de la nueva, sera el promedio del valor antiguo y de sus vecinos
    """
    # Creo una lista vacia donde ire acumulando
    processed_list = []
    final_list = []
    if len(matrix) == 1:
        processed_list = matrix
    else: 
        
        # por cada elemento de la lista
        #obtengo el valor de sus vecinos y el suyo propio y lo aniado a una lista
        for index, element in enumerate(matrix):
            if index == 0:
                processed_list.append(matrix[index + 1])
            elif index == len(matrix) - 1:
                processed_list.append(matrix[index - 2])
            else:
                processed_list.append(matrix[index + 1])
                processed_list.append(matrix[index - 1])
            processed_list.append(matrix[index])
            #calculo sus medias
            new_element = get_average(processed_list)
            # lo aniado a la lista
            final_list.append(new_element)
    # devuelvo la nueva lista
    return final_list
