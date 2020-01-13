# Descrição
# A cada dia uma planta cresce em upSpeedmetros. Todas as noites a altura da planta diminui
# em downSpeedmetros devido à falta de calor do sol. Inicialmente, a planta tem 0 metros de altura.
# Plantamos a semente no início de um dia. Queremos saber quando a altura da planta atingirá um certo nível.
#
# Exemplo
# Pois upSpeed = 100, downSpeed = 10 and desiredHeight = 910, a saída deve ser 10.
#
#  After day 1 --> 100
#  After night 1 --> 90
#  After day 2 --> 190
#  After night 2 --> 180
#  After day 3 --> 280
#  After night 3 --> 270
#  After day 4 --> 370
#  After night 4 --> 360
#  After day 5 --> 460
#  After night 5 --> 450
#  After day 6 --> 550
#  After night 6 --> 540
#  After day 7 --> 640
#  After night 7 --> 630
#  After day 8 --> 730
#  After night 8 --> 720
#  After day 9 --> 820
#  After night 9 --> 810
#  After day 10 --> 910

# Pois upSpeed = 10, downSpeed = 9 and desiredHeight = 4, a saída deve ser 1.
#
# Porque a planta atinge a altura desejada no dia 1 (10 metros).
#
#  After day 1 --> 10
# Entrada / Saída
# [input] inteiro upSpeed
#
# Um número inteiro positivo que representa o crescimento diário.
#
# Restrições: 5 ≤ upSpeed ≤ 100.
#
# [input] inteiro downSpeed
#
# Um número inteiro positivo representando o declínio noturno.
#
# Restrições: 2 ≤ downSpeed < upSpeed.
#
# [input] inteiro desiredHeight
#
# Um número inteiro positivo que representa o limite.
#
# Restrições: 4 ≤ desiredHeight ≤ 1000.
#
# [output] um inteiro
#
# O número de dias que a planta alcançará / ultrapassará a Altura desejada (incluindo o último dia na contagem total).


class Days:
    def __init__(self):
        self.upspeed = 100
        self.downspeed = 10
        self.desired = 910

    def grow(self):

        if self.upspeed >= 5 and self.upspeed <= 100 and self.downspeed >= 2 and self.downspeed < self.upspeed and self.desired >= 4 and self.desired <= 1000:
            plant = 0
            day = 1
            while plant <= self.desired:
                plant += self.upspeed
                if plant >= self.desired:
                    break
                plant -= self.downspeed
                day += 1

            return int(day)





