from datetime import date
from time import sleep
print ("\033[33m-=-\033[m"*40)
print ("Elabore um algoritmo que leio o ano de nascimento de um jovem e informe, de acordo com sua idade:\n"
       "Se ele ainda vai servir ao serviço militar;\n"
       "Se é a hora de alistar;\n"
       "Se já passou do tempo do alistamento;\n"
       "O tempo que passou ou que falta para o alistamento.")
print ("\033[33m-=-\033[m"*40)
mes_nascimento = int (input ("Digite o mês de seu nascimento: "))
ano_nascimento = int (input ("Digite o ano de seu nascimento: "))
print ("Verificando informações a respeito de seu alistamento...")
sleep (1)
data_atual = date.today()
idade = data_atual.year - ano_nascimento
if idade == 18:
    pergunta = input ("Você já participou do alistamento obrigatório? ").strip().capitalize()
    if pergunta == "Sim":
        exit()
    else:
        if  mes_nascimento - data_atual.month > 1:
            print (f"\033[33mVocê está no período de alistamento, faltam {mes_nascimento - data_atual.month} meses para você se alistar!\033[m")
        else:
            print (f"\033[33mVocê está no período de alistamento, falta {mes_nascimento - data_atual.month} mês para você se alistar!\033[m")
elif idade > 18:
    pergunta = input ("Você já participou do alistamento obrigatório? ").strip().capitalize()
    if pergunta == "Sim":
        exit()
    else:
        if (data_atual.year - ano_nascimento) - 18 == 1:
            if mes_nascimento - data_atual.month > 1:
                print (f"\033[31Você está com 1 ano e {mes_nascimento - data_atual.month} meses do seu período de alistamento. Procure o posto militar mais próximo!\033[m")
            else:
                print (f"\033[31mVocê está com 1 ano e {mes_nascimento - data_atual.month} mês de atraso. Procure o posto militar mais próximo!\033[m")
        elif (data_atual.year - ano_nascimento) - 18 > 1:
            if mes_nascimento - data_atual.month == 1:
                print (f"\033[31mVocê está com {(data_atual.year - ano_nascimento) - 18} anos e 1 mês de atraso. Procure o posto militar mais próximo!\033[m")
            else:
                print (f"\33[31mVocê está com {(data_atual.year - ano_nascimento) - 18} anos e {data_atual.month - mes_nascimento} meses de atraso. Procure o posto militar mais próximo!\033[m")
else:
    if 18 - (data_atual.year - ano_nascimento) == 1:
        if mes_nascimento - data_atual.month == 1:
            print(f"\033[32mFalta 1 ano e 1 mês para o seu período de alistamento!\033[m")
        else:
            print(f"\033[32mFalta 1 ano e {mes_nascimento - data_atual.month} meses para o seu período de alistamento!\033[m")
    else:
        if mes_nascimento - data_atual.month > 1:
            print(f"\033[32mFaltam {data_atual.year - ano_nascimento} anos e {mes_nascimento - data_atual.month} meses para o seu período de alistamento!\033[m")
        else:
            print(f"\033[32mFaltam {data_atual.year - ano_nascimento} anos e 1 mês para o seu período de alistamento!\033[m")

#Este exercício foi corrigido em vídeo e está correto!