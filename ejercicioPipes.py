'''
Created on 20 ene. 2021

@author: Isaac Morcuende

uno de los dos procesos con input pide que meta tantas cadenas como quiera hasta q diga salir, se las envia al proceso hijo y las muestra con readline

'''
import os 

r,w = os.pipe()

pid = os.fork()

if pid > 0: 
    os.close(r) 
    
    salir = 1
    texto = ""
    
    print("Proceso padre") 
    
    while(salir!="0"):
        texto = input("\nPADRE: Introduce una frase: ") + "\n"
        text = texto.encode(encoding="utf-8") 
        os.write(w, text) 
        salir = input("Introduce 0 si quieres salir: ")
        
    os.close(w)
    print("Written text:", text.decode()) 
      
else: 
    os.close(w) 
  
    r = os.fdopen(r) 
    linea=r.readline()
    
    while(linea):
        print("linea: ", linea)
        linea = r.readline()
    
    r.close()
