import math

def verificar_cedula(cedula=""):
    """
    Funcion para validar la cedula de un usuario
    parametros:
        cedula
    return:
        True si la cedula es valida, False si la cedula es invalida
    """
    
    if cedula=='no declara':
        return True
    else:
        
        if len(cedula) != 10:
            return False
        else:
            multiplicador = [2, 1, 2, 1, 2, 1, 2, 1, 2]
            ced_array = list(map(lambda k: int(k), list(cedula)))[0:9]
            ultimo_digito = int(cedula[9])
            resultado = []
            arr = map(lambda x, j: (x, j), ced_array, multiplicador)
            for (i, j) in arr:
                if i * j < 10:
                    resultado.append(i * j)
                else:
                    resultado.append((i * j)-9)
            
            if ultimo_digito == int(math.ceil(float(sum(resultado)) / 10) * 10) - sum(resultado):
                return True
            else:
                return False


