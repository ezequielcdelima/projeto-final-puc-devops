import re


def validar_cpf(cpf):
    cpf = re.sub(u'[^0-9]', '', cpf)

    if len(cpf) != 11 or not cpf.isdigit():
        return {'cpf': cpf, 'valido': False}

    # Verifica o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito_verificador_1 = 0 if resto < 2 else 11 - resto
    if int(cpf[9]) != digito_verificador_1:
        return {'cpf': cpf, 'valido': False}

    # Verifica o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito_verificador_2 = 0 if resto < 2 else 11 - resto
    if int(cpf[10]) != digito_verificador_2:
        return {'cpf': cpf, 'valido': False}

    return {'cpf': cpf, 'valido': True}
