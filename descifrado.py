import operator
texto=""
with open('/home/fran/lab1.txt', 'r') as f:
    for linea in f:
        texto=texto+linea
print(texto)
cont = 0
listafrecuencias = {}
for i in texto:
    if (listafrecuencias.get(i) == None and i!=" "and i!=","and i!="." and i!="\n" and i.isdigit()==False):
        listafrecuencias[i] = texto.count(i)

sorted_tuples = sorted(listafrecuencias.items(), key=operator.itemgetter(1), reverse=True)
listafrecuenciasordenada = {k: v for k, v in sorted_tuples}
print(listafrecuenciasordenada)
lordenada=*listafrecuenciasordenada,
frecuenciasgenerales = ["E", "A", "O", "L", "S", "N", "D", "R", "U", "I", "T", "C", "P", "M", "Y", "Q", "B",
                        "H", "G", "F", "V", "J", "Ñ", "Z", "X", "K", "W"]
ntexto=""

