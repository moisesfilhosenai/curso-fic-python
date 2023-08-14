"""
Exemplo de função com parâmetro padrão
"""

MEDIA_PADRAO = 9.5


def calcula_gasto_combustivel(km_percorrido, valor, media_km=MEDIA_PADRAO):
    valor_total = (km_percorrido / media_km) * valor
    return valor_total


km = 350
valor_gasolina = 5.09
km_litro = 10.5

resultado_01 = calcula_gasto_combustivel(km, valor_gasolina, km_litro)
print("O valor gasto na viagem para percorrer %d quilometros com média %2.1f vai ser R$ %5.2f"
      % (km, km_litro, resultado_01))


resultado_02 = calcula_gasto_combustivel(km, valor_gasolina)
print("O valor gasto na viagem para percorrer %d quilometros com média %2.1f vai ser R$ %5.2f"
      % (km, MEDIA_PADRAO, resultado_02))
