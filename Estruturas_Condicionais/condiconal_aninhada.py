conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Nao foi possivel realizar o saque, saldo insuficente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficente")
else:
    print("Sistema nao reconheceu seu tipo de conta, entre em contato com seu gerente")
