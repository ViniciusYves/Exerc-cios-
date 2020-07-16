# Escreva um algoritmo que leia um valor em metros e exiba sua conversão em centímetros e milimetros

print ("Insira por gentileza um valor para que a conversão possa ser feita")
m = float (input ("Digite o valor em Metros:"))
hm = float (m/100)
dam = float (m/10)
km = float (m/1000)
dm = float (m*10)
cm = float (m*100)
mm = float (m*1000)
print ("{} M pode ser escrito em:\n {} hm\n {} dam\n {} km\n {} dm\n {} cm\n {} mm".format (m,hm,dam,km,dm,cm,mm))

#Este exercício foi corrigido em vídeo e está correto


