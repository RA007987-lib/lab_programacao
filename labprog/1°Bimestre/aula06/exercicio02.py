"""Leia TOTAL_SEGUNDOS
    HORAS ← TOTAL_SEGUNDOS // 3600
    RESTO_SEGUNDOS ← TOTAL_SEGUNDOS % 3600
    MINUTOS ← RESTO_SEGUNDOS // 60
    SEGUNDOS_FINAIS ← RESTO_SEGUNDOS % 60
    Escreva HORAS, "h ", MINUTOS, "m ", SEGUNDOS_FINAIS, "s"
    """
total_segundos = int(input("Digite o total de segundos: "))
horas = total_segundos // 3600
resto_segundos = total_segundos % 3600
minutos = resto_segundos // 60
segundos_finais = resto_segundos % 60
print(horas,"h ", minutos,"m ",segundos_finais, "s")
