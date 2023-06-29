from validate import validate_cpf


def teste_cpf_sequencial():
    cpf = '11111111112'
    valida = validate_cpf.validar_cpf(cpf)
    if valida['valido']:
        assert cpf != cpf[0] * 11
