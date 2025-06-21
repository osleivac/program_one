# Codigo Proyecto 1 - GitHub
def leer_nota(dato):
    while True:
        try:
            entrada = float(input(dato))
            if entrada >= 1.0 and entrada <= 7.0:
                return entrada
            else:
                print('Debe ingresar una nota entre 1.0 y 7.0')
        except:
            print('Valor no válido. Intente nuevamente.')
