from validate import validate_cpf


def test_cpf_seq():
    cpf = '11111111112'
    valida = validate_cpf.validar_cpf(cpf)
    if valida['valido']:
        assert cpf != cpf[0] * 11
