# Este programa irá retornar o pagamento com parcelas iguais
# através da entrada:
# 1. pagamento a vista (ou emprestimo)
# 2. número de parcelas
# 3. valor do juros(composto) ou taxa (composta)

# subprograma(procedimento) mensagem de abertura

continua=True
while(continua):
    def mensagens():
        print("****************************************")
        print("  Bem-Vindo ao Sistema de Financiamento ")
        print("****************************************")

    # um subprogrma(função): para calcular o termo comum

    def formulaComum(N_meses, taxa):
        Resultado = 1.0
        expressao = 1 + taxa/100
        for i in range(N_meses):
            Resultado *= expressao
        return Resultado

    # Um subprograma (função): calcular parcelas iguais

    def calcularParcelamentos(Capital, termo, taxa):
        par_iguais = Capital*((termo*taxa/100)/(termo-1))
        return par_iguais

    # Um subprograma(procedimentos): mostrar resultados

    def mostrarResultados(par_iguais, N_meses, Capital):
        print(f"As parcelas iguais serão R$ {par_iguais:.2f}")
        total_pago = par_iguais*N_meses
        print(f"Valor Total a ser pago R$ {total_pago:.2f}")
        juro_pago = total_pago - Capital
        print(f"Juro a ser pago R$ {juro_pago:.2f}")

    # Programa Principal

    mensagens()

    #Entrada de dados

    Capital = float(input("Informe o valor do empréstimo ou pagamento à vista R$ "))
    N_meses = int(input("Digite quantos meses gostaria de pagar: "))
    taxa = float(input("Informa qual será a taxa por mês (%): "))

    termo = formulaComum(N_meses, taxa)
    parcelamentosIguais = calcularParcelamentos(Capital, termo, taxa)
    mostrarResultados(parcelamentosIguais, N_meses, Capital)

    opcao=input("Deseja continuar (s/n):")
    while(opcao.upper() != 'S' and opcao.upper() != 'N'):
        opcao=input('Opção inválida !! \n Deseja continuar (s/n): ')
    if opcao.upper()=='S':
        continua=True
    else:
        continua=False
