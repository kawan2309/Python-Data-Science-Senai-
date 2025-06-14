def valor_hora(salario,carga):
    calculo = salario/carga
    return calculo

def extra(valor_hr):
    vh = valor_hr * 1.75
    return vh

def salario_total(salario,valor_extra,qtd_hora_extra):
    calculo = valor_extra*qtd_hora_extra
    soma    = salario+calculo
    return soma


def sistema():
    salario  = float(input('Salario: '))
    carga    = float(input('Carga Horas: '))
    qtd_hora_extra = float(input('Quantas horas? '))
    
    valor_hr = valor_hora(salario,carga)
    print('Valor hora: R$ ', round(valor_hr,3))
    
    valor_hr_extra = extra(valor_hr)
    print('Hora Extra Trabalhada: R$', round(valor_hr_extra,3))
    
    total_salario = salario_total(salario,valor_hr_extra,qtd_hora_extra)
    print('Salario Total R$ ', round(total_salario,3))

sistema()