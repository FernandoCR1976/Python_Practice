#tipos de libros
libEntret=6000
libJard=6500
libGastro=7000
libEmp=7500
#tipos de romprecabezas
puxxPeq=12000
puxxMed=12500
puxxGde=13000
puxxGte=13500

lc=[] # [libroClub,comprarLibro,tipoPuzz]
contador=0
vtasTot=[]
lvend=[]
entret=[]
jard=[]
gastr=[]
emp=[]
puzzVend=[]
puzzPeqVend=[]
puzzMedVend=[]
puzzGdeVend=[]
puzzGteVend=[]
conLibClub=[]



#Entradas

cantClientes=int(input("INGRESE EL NUMERO DE CLIENTES: "))

while contador<cantClientes:

    vtaClienteLibro=0
    vtacliente=0


    libroClub=int(input("Es miembro de del club ? : \n 1. SI \n 2. NO \n"))
    if libroClub==1:
        conLibClub.append(1)

      
    
    
    
    comprarLibro=int(input("Quieres comprar un libro ? : \n 1. SI \n 2. NO \n"))    
    
    if comprarLibro == 1:

        tipoLibro=int(input("Por favor indique el tipo de libro que desea comprar: \n 1. Entretenimiento \n 2. Jardinería \n 3. Gastronomía \n 4. Emprendimiento \n"))
        if tipoLibro==1:
            vtasTot.append(libEntret)
            lvend.append(libEntret)
            entret.append(1)
            vtaClienteLibro=libEntret
        elif tipoLibro==2:
            vtasTot.append(libJard)
            lvend.append(libJard)
            jard.append(1)
            vtaClienteLibro=libJard
        elif tipoLibro==3:
            vtasTot.append(libGastro)
            lvend.append(libGastro)
            gastr.append(1)
            vtaClienteLibro=libGastro
        elif tipoLibro==4:
            vtasTot.append(libEmp)
            lvend.append(libEmp)
            emp.append(1)
            vtaClienteLibro=libEmp



    comprarPuzz=int(input("Desea comprar un rompecabezas: \n 1. SI \n 2. NO \n"))

  
    if comprarPuzz==2:
        print("SU COMPRA ES DE ",vtaClienteLibro)
    if comprarPuzz==1 and libroClub==1:       
        
        tipoPuzz=int(input("Ingrese que tamaño de rompecabezas quiere: \n 1. De 500 a 1000 \n 2. De 1001 a 1500 \n 3. De 1501 a 2000 \n 4. Más de 2000 \n "))
        if tipoPuzz==1:
            vtasTot.append(puxxPeq*0.85)
            puzzVend.append(puxxPeq*0.85)
            puzzPeqVend.append(puxxPeq)
            vtacliente=puxxPeq*0.85
        elif tipoPuzz==2:
            vtasTot.append(puxxMed*0.85)
            puzzVend.append(puxxMed*0.85)
            puzzMedVend.append(puxxMed)
            vtacliente=puxxMed*0.85
        elif tipoPuzz==3:
            vtasTot.append(puxxGde*0.85)
            puzzVend.append(puxxGde*0.85)
            puzzGdeVend.append(puxxGde)
            vtacliente=puxxGde*0.85
        elif tipoPuzz==4:
            vtasTot.append(puxxGte*0.85)
            puzzVend.append(puxxGte*0.85)
            puzzGteVend.append(puxxGte)
            vtacliente=puxxGte*0.85


        print("\n SU COMPRA ES DE ",vtacliente+vtaClienteLibro," \n ")


    elif comprarPuzz==1 and libroClub==2:       
        
        tipoPuzz=int(input("Ingrese que tamaño de rompecabezas quiere: \n 1. De 500 a 1000 \n 2. De 1001 a 1500 \n 3. De 1501 a 2000 \n 4. Más de 2000 \n "))
        if tipoPuzz==1:
            vtasTot.append(puxxPeq)
            puzzVend.append(puxxPeq)
            puzzPeqVend.append(puxxPeq)
            vtacliente=puxxPeq
        elif tipoPuzz==2:
            vtasTot.append(puxxMed)
            puzzVend.append(puxxMed)
            puzzMedVend.append(puxxMed)
            vtacliente=puxxMed
        elif tipoPuzz==3:
            vtasTot.append(puxxGde)
            puzzVend.append(puxxGde)
            puzzGdeVend.append(puxxGde)
            vtacliente=puxxGde
        elif tipoPuzz==4:
            vtasTot.append(puxxGte)
            puzzVend.append(puxxGte)
            puzzGteVend.append(puxxGte)
            vtacliente=puxxGte


        print("\n SU COMPRA ES DE ",vtacliente+vtaClienteLibro," \n ") # IMPRIME CADA COMPRA
        
    
    contador=contador+1

#print(vtasTot)
#print(puzzVend)
#print(lvend)
#################ESTO AUN NO ME DEJAN USARLO############
"""
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma
"""
#######################################################

######################SUMA DE VENTAS TOTALES###################
conVtasTotales=0
sumaVtasTotales=0
while conVtasTotales<len(vtasTot):
    sumaVtasTotales=vtasTot[conVtasTotales]+sumaVtasTotales
    conVtasTotales+=1
###############################################################

#################SUMA DE VENTA DE LIBROS######################
conVtasLibros=0
sumaVtasLibros=0

while conVtasLibros<len(lvend):
    sumaVtasLibros=lvend[conVtasLibros]+sumaVtasLibros
    conVtasLibros+=1
##############################################################    

###################SUMA VENTA DE ROMPECABEZAS#####################
conVtasPuzz=0
sumaVtasPuzz=0
while conVtasPuzz<len(puzzVend):
    sumaVtasPuzz=puzzVend[conVtasPuzz]+sumaVtasPuzz
    conVtasPuzz+=1
##################################################################    
########################CALCULO DEL RPOMEDIO DE CLIENTES MIEMBROS DE LIBRO CLUB#############
promLC=(len(conLibClub)/cantClientes)*100
############################################################################################


print("EL TOTAL DE CLIENTES QUE VISITARON LA LIBRERIA FUERON: ", cantClientes,"\n")
print("LAS VENTAS TOTALES DEL DÍA SON: ",sumaVtasTotales,"\n")
print("Se vendieron ",len(lvend)," libros, para una venta total de ",sumaVtasLibros,"\n")
print("Se vendieron ",len(entret)," libros de Entretenimiento")
print("Se vendieron ",len(jard)," libros de Jardinería")
print("Se vendieron ",len(gastr)," libros de Gastronomía")
print("Se vendieron ",len(emp)," libros de Emprendimiento \n")
print("Se vendieron un total de  ",len(puzzVend)," rompecabezas para una venta total de ", sumaVtasPuzz,"\n")
print("Se vendieron ",len(puzzPeqVend)," rompecabezas de 500 a 1000 piezas")
print("Se vendieron ",len(puzzMedVend)," rompecabezas de 1001 a 1500 piezas")
print("Se vendieron ",len(puzzGdeVend)," rompecabezas de 1501 a 2000 piezas")
print("Se vendieron ",len(puzzGteVend)," rompecabezas de más de 2000 piezas","\n")
print("EL PORCENTAJE DE CLIENTE PERTENECIENTES A LIBRO CLUB ES DE: ",promLC,"%")

