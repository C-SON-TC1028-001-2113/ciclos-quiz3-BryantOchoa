def main():
    #escribe tu código abajo de esta línea
     x = int(input())
     suma = 0 
     for i in range(x):
        y = float(input())
        suma = suma + y
        promedio = suma / x
     print(promedio)
if __name__=='__main__':
    main()
