#8) Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
#Ex:
#Digite uma distância em metros: 185.72
##A distância de 85.7m corresponde a:#
#0.18572Km#
#1.8572Hm#
#18.572Dam#
#1857.2dm#
#18572.0cm#
#185720.0mm#

distancia=float(input("Digite uma distância em metros:"))

milímetros = quilometros * 1000000.0
milímetros = hectômetro * 10000.0
milimetros = dacametro  * 100000.0
milimetros = metros * 1000.0
milimetros = decimentro * 10000.0
milimetros = centrimento * 10000.0

