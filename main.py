X1=[[1,1],[1,0]]
X2=[[0,0],[0,1]]
A = [-1,-1,-1,-1]

# Convierte una matriz bidimensional en un vector unidimensional.
def expandir_matriz(X):
    matriz_expandida=[]

    for fila in X:
        for elemento in fila:
            matriz_expandida.append(elemento)
    return matriz_expandida

# Convierte un vector en una matriz de una fila si es necesario.
def vector_a_matriz(X):
    Y=[]
    if not isinstance(X[0], list):
        Y.append(X)
    else:
        Y=X
    return Y

# Sustituye todos los valores 0 del vector por -1.
def ceros_por_menos_unos(X):
    for i in range(len(X)):
        if X[i] == 0:
            X[i]=-1
    return X

# Calcula la matriz transpuesta intercambiando filas por columnas.
def transpuesta(X):
    X=vector_a_matriz(X)

    filas = len(X)
    columnas = len(X[0])

    matriz_transpuesta=[]

    for j in range(columnas):
        fila=[]
        for i in range(filas):
            fila.append(X[i][j])

        matriz_transpuesta.append(fila)

    return matriz_transpuesta

# Multiplica dos matrices siempre que sus dimensiones sean compatibles.
def multiplicar_matrices(X1, X2):
    fila=[]
    matriz_resultante=[]
    X1=vector_a_matriz(X1)
    X2=vector_a_matriz(X2)
    filas_X1 = len(X1)
    columnas_X1 = len(X1[0])
    filas_X2 = len(X2)
    columnas_X2 = len(X2[0])

    if columnas_X1 != filas_X2:
        print("Error, no se pueden multiplicar las matrices")
    else:
        for i in range(filas_X1):
            for j in range(columnas_X2):
                suma = 0
                for k in range(filas_X2):
                    suma = suma + (X1[i][k] * X2[k][j])
                fila.append(suma)
            matriz_resultante.append(fila)
            fila=[]
    return matriz_resultante

# Suma dos matrices elemento por elemento si tienen la misma dimensión.
def sumar_matrices(X1, X2):
    fila=[]
    matriz_resultante=[]
    filas_X1 = len(X1)
    columnas_X1 = len(X1[0])
    filas_X2 = len(X2)
    columnas_X2 = len(X2[0])
    if filas_X1 != filas_X2 or columnas_X1 != columnas_X2:
        print("Error, no se pueden sumar las matrices porque no son de la misma dimension")
        return 0
    else:
        for i in range(filas_X1):
            for j in range(columnas_X1):
                fila.append(X1[i][j]+ X2[i][j])
                #print(fila)
            matriz_resultante.append(fila)
            fila = []
    return matriz_resultante

# Sustituye por 0 todos los elementos de la diagonal principal.
def diagonal_por_ceros(X):
    filas = len(X)
    columnas = len(X[0])
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                X[i][j]=0
    return X

# Calcula la matriz de pesos de la red Hopfield a partir de los patrones.
def mat_de_pesos(X_uno, X_dos):
    X_uno_expandida=expandir_matriz(X_uno)
    X_dos_expandida=expandir_matriz(X_dos)
    X_uno=ceros_por_menos_unos(X_uno_expandida)
    X_dos=ceros_por_menos_unos(X_dos_expandida)
    X_uno_t=transpuesta(X_uno)
    X_dos_t=transpuesta(X_dos)
    X_uno_mult=multiplicar_matrices(X_uno_t,X_uno)
    X_dos_mult=multiplicar_matrices(X_dos_t,X_dos)
    suma_mat=sumar_matrices(X_uno_mult,X_dos_mult)
    mat_de_pesos=diagonal_por_ceros(suma_mat)
    return mat_de_pesos

# Ejecuta la red Hopfield hasta que el estado deje de cambiar.
def main(A):
    A=vector_a_matriz(A)
    T=mat_de_pesos(X1,X2)
    while True:
        A_x_T=multiplicar_matrices(A,T)
        U=escalonada(A_x_T,A)
        if A != U:
            A=U
        else:
            break
    return A

# Aplica la función de activación conservando el estado anterior cuando el valor es 0.
def escalonada(X, estado_anterior):
    filas = len(X)
    columnas = len(X[0])

    for i in range(filas):
        for j in range(columnas):
            if X[i][j] > 0:
                X[i][j] = 1
            elif X[i][j] < 0:
                X[i][j] = -1
            else:
                X[i][j] = estado_anterior[i][j]
    return X

if __name__ == "__main__":
    print(main(A))
