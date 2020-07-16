import math
angulo = float (input ("Digite um ângulo para iniciar: "))
escolha = int (input ('O que você deseja calcular?\nSeno (1) Cosseno (2) Tangente (3) ou Todas as opções (4): '))
if escolha == 1:
    print ("O valor de seno do ângulo {} é {:.2f}!".format(angulo,math.sin(math.radians(angulo))))
elif escolha == 2:
    print ("O valor de cosseno do ângulo {} é {:.2f}!".format(angulo,math.cos(math.radians(angulo))))
elif escolha == 3:
    print ("O valor da tangente de {} é {:.2f}!".format(angulo,math.tan(math.radians(angulo))))
else:
    print (" O valor do Seno, Cosseno e Tangente do angulo {} é {:.2f},{:.2f} e {:.2f}".format(angulo,math.sin(math.radians(angulo)),math.cos(math.radians(angulo)),math.tan(math.radians(angulo))))

#Exercício corrigido em vídeo e está correto