import operator
def cambiar_letras(char1,char2,texto):
    nt=list(texto)
    cont=0
    for i in nt:
        if(i==char1):
            nt[cont]=char2
        elif(i==char2):
            nt[cont]=char1
        cont=cont+1
    nuevot="".join(nt)
    print(nuevot)
    return nuevot

def descifrar(texto,tupla):
    ntexto=""
    for i in texto:
        if(i!=" "and i!=","and i!="." and i!="\n" and i.isdigit()==False):
            caracter=str(tupla.get(i))
            ntexto=ntexto+caracter
        else:
            ntexto=ntexto+i
    print(ntexto)
    return ntexto
def crearlistadef(lfrecor,frecgen):
    dicfin={}
    lfrecor_tupla=*lfrecor,
    frecgen_tupla=*frecgen,
    j=len(lfrecor_tupla)
    for i in range (j):
        dicfin[lfrecor_tupla[i]]=frecgen_tupla[i]
    return dicfin
def descifrado():
    texto=""
    dir = input("introduce el directorio del archivo \n")
    with open(dir, 'r') as f:
        for linea in f:
            texto=texto+linea
    cont = 0
    listafrecuencias = {}
    for i in texto:
        if (listafrecuencias.get(
                i) == None and i != " " and i != "," and i != "." and i != "\n" and i.isdigit() == False):
            listafrecuencias[i] = texto.count(i)
    sorted_tuples = sorted(listafrecuencias.items(), key=operator.itemgetter(1), reverse=True)
    listafrecuenciasordenada = {k: v for k, v in sorted_tuples}
    lordenada=*listafrecuenciasordenada,
    frecuenciasgenerales = ["E", "A", "O", "L", "S", "N", "D", "R", "U", "I", "T", "C", "P", "M", "Y", "Q", "B",
                            "H", "G", "F", "V", "J", "Ñ", "Z", "X", "K", "W"]
    dic=crearlistadef(lordenada,frecuenciasgenerales)
    nt=descifrar(texto,dic)
    while(True):
        l1=input("que letra quieres cambiar 1\n")
        l2=input("que letra quieres cambiar 2\n")
        nt=cambiar_letras(l2,l1, nt)

if __name__ == '__main__':
    descifrado()

