import datetime

import os

class Medico:
    crm = []
    nome = ""
    data = ""
    sexo = ""
    especialidade = ""
    universidade = ""
    email = []
    telefone = []


class Paciente:
    cpf = []
    nome = ""
    data = ""
    sexo = ""
    plano = ""
    email = []
    telefone = []

class Consulta:
    crm = []
    cpf = []
    data = ""
    hora = ""
    diagnostico = ""
    medicamento = []

#--------------------------------------------------- MENU --------------------------------------------------------------


def menu():
    print("----------------")
    print(" Menu de opções ")
    print("----------------")
    print("1. Médicos")
    print("2. Pacientes")
    print("3. Consultas")
    print("4. Relatórios")
    print("5. Sair")
    opcao = input("-> ")
    return opcao


#--------------------------------------------------MENU-MÉDICO----------------------------------------------------------

def sub_menu_medico():
    print("|------------------------|")
    print("Adicionar médicos........1")
    print("Listar os médicos........2")
    print("Listar um médico.........3")
    print("Alterar médico...........4")
    print("Excluir médico...........5")
    print("Sair.....................0")
    opcao = input("-> ")
    return opcao


def menu_medico(medicos):
    j = ""
    while j != "0":
        j = sub_menu_medico()
        if j == '1':
            inserir_medico(medicos)

        elif j == '2':
            listar_medico(medicos)

        elif j == '3':
            listar_um_medico(medicos)

        elif j == '4':
            alterar_medico(medicos)

        elif j == '5':
            excluir_medico(medicos)

        elif j != "0":
            print("Opção inválida.")


#-------------------------------------------------MENU-PACIENTE---------------------------------------------------------


def sub_menu_paciente():
    print("--------------------------")
    print("Adicionar pacientes......1")
    print("Listar os pacientes......2")
    print("Listar um paciente.......3")
    print("Alterar paciente.........4")
    print("Excluir paciente.........5")
    print("Sair.....................0")
    opcao = input("-> ")
    return opcao



def menu_paciente(pacientes):
    j = ""
    while j != "0":
        j = sub_menu_paciente()
        if j == '1':
            inserir_paciente(pacientes)

        elif j == '2':
            listar_paciente(pacientes)

        elif j == '3':
            listar_um_paciente(pacientes)

        elif j == '4':
            alterar_paciente(pacientes)

        elif j == '5':
            excluir_paciente(pacientes)

        elif j != "0":
            print("Opção inválida.")


#-------------------------------------------------MENU-CONSULTAS--------------------------------------------------------

def sub_menu_consulta():
    print("|------------------------|")
    print("Adicionar consulta.......1")
    print("Listar as consultas......2")
    print("Listar uma consulta......3")
    print("Alterar consulta.........4")
    print("Excluir consulta.........5")
    print("Sair.....................0")
    opcao = input("-> ")
    return opcao


def menu_consulta(consultas,medicos,pacientes):
    j = ""
    while j != "0":
        j = sub_menu_consulta()
        if j == '1':
            inserir_consulta(consultas,medicos,pacientes)

        elif j == '2':
            listar_consulta(consultas)

        elif j == '3':
            listar_uma_consulta(consultas)

        elif j == '4':
            alterar_consulta(consultas)

        elif j == '5':
            excluir_consulta(consultas)

        elif j != "0":
            print("Opção inválida.")


#-------------------------------------------------MENU-RELATÓRIOS-------------------------------------------------------

def sub_menu_relatorio():
    print("|--------------------------------------------------|")
    print("Dados dos médicos a partir da especialidade........1")
    print("Dados dos pacientes a partir da idade..............2")
    print("Lista de consultas a partir da data fornecida......3")
    print("Sair...............................................0")
    opcao = input("-> ")
    return opcao


def menu_relatorio(consultas,medicos,pacientes):
    j = ""
    while j != "0":
        j = sub_menu_relatorio()
        if j == '1':
            buscar_dados_medicos_especialidade(medicos)

        elif j == '2':
            dados_pacientes_a_partir_da_idade(pacientes)

        elif j == '3':
            listar_consulta_a_partir_da_data(consultas,medicos,pacientes)

        elif j != "0":
            print("Opção inválida.")


#---------------------------------------------------RELATÓRIOS----------------------------------------------------------

def buscar_dados_medicos_especialidade(lista_medico):
    especialidade_buscada = input("Insira a especialidade da qual você quer extrair os dados dos médicos: ")
    achei_especialidade = False
    i = 0
    while i < len(lista_medico):
        if lista_medico[i].especialidade == especialidade_buscada:
            achei_especialidade = True
            imprime_medico(lista_medico[i])
        i = i+1

    if achei_especialidade == False:
        print("Não há especialidade cadastrada!")




def dados_pacientes_a_partir_da_idade(lista_paciente):                               #essa funçao cria uma lista de idades e de ano de nascimento dos pacientes que foram cadastrados a partir da data de nascimento no formato "XX/XX/XXXX"
    lista_anos = []
    i = 0
    while i < len(lista_paciente):
        ano_achado = lista_paciente[i].data.split("/")                          #como o formato é sempre "XX/XX/XXXX", foi colocado um split para guardar o ano de nascimento dos pacientes
        k = 2                                                                   #por exemplo, a lista_paciente guarda a data ["15/09/1997"], já a ano_achado guarda: ["15","09","1997"). A partir disso, o k é igual à 2 porque o ano de nascimento começa na posição 2 da lista
        while k < len(ano_achado):
            lista_anos.append(int(ano_achado[k]))
            k = k+3                                                             # k recebe +3 porque o ano sempre vai estar 3 posições à frente
        i = i+1

    lista_idades = []
    ano_atual = datetime.datetime.now()
    m = 0
    while m < len(lista_anos):
        idades_ = ano_atual.year - lista_anos[m]
        lista_idades.append(idades_)                                  #adiciona na lista_idades o ano que estamos menos o ano de nascimento do paciente que foi cadastrado no sistema
        m = m+1


    idade_buscada = int(input("Insira a idade da qual você quer extrair os dados dos pacientes mais novos: "))
    achei_idade_buscada = False
    j = 0
    while j < len(lista_idades):
        if int(lista_idades[j]) < idade_buscada:                     #percorre a lista de idades e compara com a idade que o usuário forneceu (para ver se é menor ou maior)
            imprime_paciente(lista_paciente[j])
            achei_idade_buscada = True
            print(f"Paciente com {lista_idades[j]} anos.")
            print("-------------------------------------")
        j=j+1

    if achei_idade_buscada == False:
        print(f"Não há nenhum paciente com idade menor do que {idade_buscada} anos!")





def listar_consulta_a_partir_da_data(lista_consultas,lista_medicos,lista_pacientes):
    lista_datas = []
    ultimos_x_dias = int(input("Insira o número de dias atrás que deseja buscar as consultas: "))
    i = 0
    while i < len(lista_consultas):
        d1 = lista_consultas[i].data                 #formato: [2022-12-12]
        data_atual = datetime.date.today()
        diferenca = data_atual - d1
        lista_datas.append(diferenca.days)                                                           #a lista_datas guarda a diferença de dias da data atual menos a data cadastrada no menu "Consultas"
        i = i+1

    j = 0
    achei_o_dia = False
    while j < len(lista_datas):
        if lista_datas[j] < ultimos_x_dias:
            imprime_consulta_mais_nome_do_medico_e_do_paciente(lista_consultas[j],lista_medicos[j],lista_pacientes[j])
            achei_o_dia = True
        j = j+1

    if achei_o_dia == False:
        print(f"Nenhuma consulta foi encontrada nos últimos {ultimos_x_dias} dias!")



def imprime_consulta_mais_nome_do_medico_e_do_paciente(c, m, p):
    i = 0
    medicamento = ''
    while i < len(c.medicamento):
        medicamento = c.medicamento[i] + " - " + medicamento
        i = i + 1

    print(c.crm + " - " + m.nome + " / " + c.cpf + " - " + p.nome + " / " + str(c.data) + " / " + str(c.hora) + " / " + c.diagnostico + " / " + medicamento)



#------------------------------------BUSCA, INSERIR, LISTAR UM, EXCLUIR, ALTERAR - MÉDICO ------------------------------
def busca_medico(lista_medico,crm):
    i = 0
    while i < len(lista_medico):
        if lista_medico[i].crm == crm:
            return i
        i = i+1

    return -1


def listar_um_medico(lista_medicos):
    if len(lista_medicos) > 0:
        CRM_a_ser_buscado = input("Insira o CRM do médico a ser listado: ")
        indice = busca_medico(lista_medicos, CRM_a_ser_buscado)

        if indice == -1:
            print("CRM não cadastrado!")
        else:
            imprime_medico(lista_medicos[indice])

    else:
        print("Ainda não há médicos cadastrados!")



def excluir_medico(lista_medicos):
    if len(lista_medicos) > 0:
        CRM_a_ser_excluido = input("Insira o CRM do médico a ser excluído: ")
        indice = busca_medico(lista_medicos,CRM_a_ser_excluido)


        if indice == -1:
            print("CRM não cadastrado!")

        else:
            del(lista_medicos[indice])
            print("Médico excluído!")

    else:
        print("Ainda não há médicos cadastrados!")



def alterar_medico(lista_medicos):
    if len(lista_medicos) > 0:
        CRM_a_ser_alterado = input("Insira o CRM do médico a ser alterado: ")
        indice = busca_medico(lista_medicos, CRM_a_ser_alterado)

        if indice == -1:
            print("CRM não está cadastrado!")

        else:
            lista_medicos[indice].nome = input("Insira o nome do médico: ")
            lista_medicos[indice].data = input("Insira a data de nascimento do médico: ")
            lista_medicos[indice].sexo = input("Insira o sexo do médico: ")
            lista_medicos[indice].especialidade = input("Insira a especialidade do médico: ")
            lista_medicos[indice].universidade = input("Insira a universidade do médico: ")
            lista_medicos[indice].email = []
            lista_medicos[indice].telefone = []

            j = 0
            while j != '0':
                lista_medicos[indice].email.append(input("Insira o email: "))
                j = input("Deseja inserir um novo email? Se sim, digite 1. Se não, digite 0: ")
            j = 0
            while j != '0':
                lista_medicos[indice].telefone.append(input("Insira o telefone: "))
                j = input("Deseja inserir um novo telefone? Se sim, digite 1. Se não, digite 0: ")

    else:
        print("Ainda não há médicos cadastrados!")


def inserir_medico(lista_medicos):
    m = Medico()
    print("Dados do médico a serem inseridos: ")
    m.crm = input("Informe o CRM: ")
    indice = busca_medico(lista_medicos,m.crm)

    if indice == -1:
        m.nome = input("Informe o nome: ")
        m.data = input("Insira a data de nascimento: ")
        m.sexo = input("Insira o sexo: ")
        m.especialidade = input("Informe a especialidade: ")
        m.universidade = input("Informe a universidade na qual o médico se formou: ")


        escolhaEmail = ""
        m.email = []
        while escolhaEmail != '0':
            email = input("Insira o email: ")
            m.email.append(email)
            escolhaEmail = input("Deseja inserir mais um e-mail? Se sim, digite 1. Se não, digite 0: ")



        escolhaTelefone = ""
        m.telefone = []
        while escolhaTelefone != '0':
            telefone = input("Insira o número de telefone: ")
            m.telefone.append(telefone)
            escolhaTelefone = input("Deseja inserir mais um número de telefone? Se sim, digite 1. Se não, digite 0: ")

        lista_medicos.append(m)
        print("Médico inserido com sucesso!")


    else:
        print("O CRM já está cadastrado no sistema!")



#----------------------------------BUSCA, INSERIR, LISTAR UM, EXCLUIR, ALTERAR - PACIENTE ------------------------------

def busca_paciente(lista_paciente,cpf):
    i = 0
    while i < len(lista_paciente):
        if lista_paciente[i].cpf == cpf:
            return i
        i = i+1

    return -1


def listar_um_paciente(lista_pacientes):
    if len(lista_pacientes) > 0:
        CPF_a_ser_buscado = input("Insira o CPF do paciente a ser listado: ")
        indice = busca_paciente(lista_pacientes, CPF_a_ser_buscado)

        if indice == -1:
            print("CPF não cadastrado!")
        else:
            (imprime_paciente(lista_pacientes[indice]))

    else:
        print("Ainda não há pacientes cadastrados!")



def excluir_paciente(lista_pacientes):
    if len(lista_pacientes) > 0:
        CPF_a_ser_excluido = input("Insira o CPF do paciente a ser excluído: ")
        indice = busca_paciente(lista_pacientes, CPF_a_ser_excluido)


        if indice == -1:
            print("CPF não cadastrado!")

        else:
            del(lista_pacientes[indice])
            print("Paciente excluído!")

    else:
        print("Ainda não há pacientes cadastrados!")


def alterar_paciente(lista_pacientes):
    if len(lista_pacientes) > 0:
        CPF_a_ser_alterado = input("Insira o CPF do paciente a ser alterado: ")
        indice = busca_paciente(lista_pacientes, CPF_a_ser_alterado)

        if indice == -1:
            print("CPF não está cadastrado!")

        else:
            lista_pacientes[indice].nome = input("Insira o nome do paciente: ")
            lista_pacientes[indice].data = input("Insira a data de nascimento do paciente: ")
            lista_pacientes[indice].sexo = input("Insira o sexo do paciente: ")
            lista_pacientes[indice].plano = input("Insira o plano do paciente: ")
            lista_pacientes[indice].email = []
            lista_pacientes[indice].telefone = []

            j = 0
            while j != '0':
                lista_pacientes[indice].email.append(input("Insira o email: "))
                j = input("Deseja inserir um novo email? Se sim, digite 1. Se não, digite 0: ")
            j = 0
            while j != '0':
                lista_pacientes[indice].telefone.append(input("Insira o telefone: "))
                j = input("Deseja inserir um novo telefone? Se sim, digite 1. Se não, digite 0: ")

    else:
        print("Ainda não há pacientes cadastrados!")



def inserir_paciente(lista_pacientes):
    p = Paciente()
    print("Dados do paciente a serem inseridos: ")
    p.cpf = input("Informe o CPF: ")
    indice = busca_paciente(lista_pacientes, p.cpf)

    if indice == -1:
        p.nome = input("Informe o nome: ")
        p.data = input("Insira a data de nascimento no formato (XX/XX/XXXX) - dia, mês, ano: ")
        p.sexo = input("Insira o sexo: ")
        p.plano = input("Insira o plano de saúde: ")

        escolhaEmail = ""
        p.email = []
        while escolhaEmail != '0':
            email = input("Insira o email: ")
            p.email.append(email)
            escolhaEmail = input("Deseja inserir mais um e-mail? Se sim, digite 1. Se não, digite 0: ")

        escolhaTelefone = ""
        p.telefone = []
        while escolhaTelefone != '0':
            telefone = input("Insira o número de telefone: ")
            p.telefone.append(telefone)
            escolhaTelefone = input("Deseja inserir mais um número de telefone? Se sim, digite 1. Se não, digite 0: ")


        lista_pacientes.append(p)
        print("Paciente inserido com sucesso!")

    else:
        print("O CPF já está cadastrado no sistema!")


#---------------------------------BUSCA, INSERIR, LISTAR UM, EXCLUIR, ALTERAR - CONSULTAS ------------------------------

def busca_consulta(lista_consulta,crm,cpf,data,hora):
    i = 0
    while i < len(lista_consulta):
        if lista_consulta[i].crm == crm and lista_consulta[i].cpf == cpf and str(lista_consulta[i].data) == data and str(lista_consulta[i].hora) == hora:         #str para data e hora porque elas são inseridas como "int", e na hora de comparar, o usuário fornece o dado em str
            return i
        i = i+1

    return -1


def busca_datas_horas_iguais(lista_consulta,crm,cpf,data,hora):                   #função para identificar se já existe uma consulta cadastrada no mesmo dia/horário com o mesmo CRM ou o mesmo CPF
    i = 0
    while i < len(lista_consulta):
        if lista_consulta[i].crm == crm and str(lista_consulta[i].data) == data and str(lista_consulta[i].hora) == hora:       #para CRM
            return "achei"                                                                                                     #aqui retorna a string "achei", pois o intuito é achar horas e datas iguais (como consequência, a consulta não vai ser adicionada se forem iguais)
        if lista_consulta[i].cpf == cpf and str(lista_consulta[i].data) == data and str(lista_consulta[i].hora) == hora:       #para CPF
            return "achei"
        else:
            if lista_consulta[i].crm == crm and lista_consulta[i].cpf == cpf and str(lista_consulta[i].data) == data and str(lista_consulta[i].hora) == hora:
                return i
        i = i+1

    return -1



def listar_uma_consulta(lista_consultas):
    if len(lista_consultas) > 0:
        print("Informe os dados a seguir para listar uma consulta: ")
        CRM_a_ser_buscado = input("Insira o CRM do médico: ")
        CPF_a_ser_buscado = input("Insira o CPF do paciente: ")
        DATA_a_ser_buscada = input("Insira a data da consulta: ")
        HORA_a_ser_buscada = input("Insira o horário da consulta: ")
        check_consulta = busca_consulta(lista_consultas,CRM_a_ser_buscado,CPF_a_ser_buscado,DATA_a_ser_buscada,HORA_a_ser_buscada)      #(*)

        if check_consulta == -1:
            print("A consulta não está cadastrada!")
        else:
            imprime_consulta(lista_consultas[check_consulta])

    else:
        print("Ainda não há consultas cadastradas!")



def excluir_consulta(lista_consultas):
    if len(lista_consultas) > 0:
        CRM_a_ser_excluido = input("Informe o CRM do médico: ")
        CPF_a_ser_excluido = input("Informe o CPF do paciente: ")
        DATA_a_ser_excluida = input("Informe a data: ")
        HORA_a_ser_excluida = input("Informe o horário: ")

        check_consulta = busca_consulta(lista_consultas,CRM_a_ser_excluido,CPF_a_ser_excluido,DATA_a_ser_excluida,HORA_a_ser_excluida)       #(*)

        if check_consulta == -1:
            print("Consulta não cadastrada!")

        else:
            del(lista_consultas[check_consulta])
            print("Consulta excluída!")

    else:
        print("Ainda não há consultas cadastradas!")



def alterar_consulta(lista_consulta):
    if len(lista_consulta) > 0:
        CRM_a_ser_alterado = input("Informe o CRM do médico: ")
        CPF_a_ser_alterado = input("Informe o CPF do paciente: ")
        DATA_a_ser_alterada = input("Informe a data: ")
        HORA_a_ser_alterada = input("Informe o horário: ")
        check_consulta = busca_consulta(lista_consulta,CRM_a_ser_alterado,CPF_a_ser_alterado,DATA_a_ser_alterada,HORA_a_ser_alterada)        #(*)

        if check_consulta == -1:
            print("Não há consulta cadastrada!")

        else:
            lista_consulta[check_consulta].diagnostico = input("Insira o diagnóstico a ser alterado: ")
            lista_consulta[check_consulta].medicamento = []
            j = 0
            while j != '0':
                lista_consulta[check_consulta].medicamento.append(input("Insira o medicamento a ser alterado: "))
                j = input("Deseja inserir um novo medicamento? Se sim, digite 1. Se não, digite 0: ")

    else:
        print("Ainda não há consultas cadastradas!")




def inserir_consulta(lista_consulta,lista_medicos,lista_pacientes):
    c = Consulta()
    print("Dados da consulta a serem inseridos: ")
    c.crm = input("Informe o CRM: ")
    check_medico = busca_medico(lista_medicos,c.crm)

    if check_medico != -1:
        c.cpf = input("Informe o CPF: ")
        check_paciente = busca_paciente(lista_pacientes, c.cpf)
        if check_paciente != -1:
            ano = int(input("Informe o ano: "))
            mes = int(input("Informe o mês: "))
            dia = int(input("Informe o dia: "))
            c.data = datetime.date(ano,mes,dia)
            horas = int(input("Informe a hora: "))
            minutos = int(input("Informe os minutos: "))
            c.hora = datetime.time(horas,minutos)
            check_data_e_hora = busca_datas_horas_iguais(lista_consulta,c.crm,c.cpf,c.data,c.hora)                       #check's (*) identificam se tal informação já existe cadastrada na lista. Logo em seguida, check's retornam o índice achado, se não houver o índice, retornam -1
            if check_data_e_hora == -1:
                c.diagnostico = input("Informe o diagnóstico: ")

                escolhaMedicamento = ""
                c.medicamento = []
                while escolhaMedicamento != '0':
                    medicamento = input("Insira o medicamento: ")
                    c.medicamento.append(medicamento)
                    escolhaMedicamento = input("Deseja inserir mais um medicamento? Se sim, digite 1. Se não, digite 0: ")

                lista_consulta.append(c)
                print("Consulta cadastrada com sucesso!")

            else:
                print("Data e horas iguais. Impossível cadastrar essa consulta!")


        else:
            print("O CPF não está cadastrado no sistema!")


    else:
        print("O CRM não está cadastrado no sistema!")

#----------------------------------------------LISTAR E IMPRIMIR - MÉDICO ----------------------------------------------


def listar_medico(lista_medicos):
    if len(lista_medicos) > 0:
        i = 0
        while i < len(lista_medicos):
            imprime_medico(lista_medicos[i])
            i = i+1

    else:
        print("Não há médicos cadastrados!")



def imprime_medico(m):
    i = 0
    email = ''
    while i < len(m.email):
        email = m.email[i] + " - " + email
        i = i+1

    j = 0
    telefone = ''
    while j < len(m.telefone):
        telefone = m.telefone[j] + " - " + telefone
        j = j+1

    print(m.crm + " / " + m.nome + " / " + m.data + " / " + m.sexo + " / " + m.especialidade + " / " + m.universidade + " / " + email + " / " + telefone)


#-------------------------------------------LISTAR E IMPRIMIR - PACIENTE -----------------------------------------------


def listar_paciente(lista_pacientes):
    if len(lista_pacientes) > 0:
        i = 0
        while i < len(lista_pacientes):
            imprime_paciente(lista_pacientes[i])
            i = i+1

    else:
        print("Não há pacientes cadastrados!")


def imprime_paciente(p):
    i = 0
    email = ''
    while i < len(p.email):
        email = p.email[i] + " - " + email
        i = i+1

    j = 0
    telefone = ''
    while j < len(p.telefone):
        telefone = p.telefone[j] + " - " + telefone
        j = j+1
    print(p.cpf + " / " + p.nome + " / " + p.data + " / " + p.sexo + " / " + p.plano + " / " + email + " / " + telefone)




#----------------------------------------------LISTAR E IMPRIMIR - CONSULTA --------------------------------------------


def listar_consulta(lista_consultas):
    if len(lista_consultas) > 0:
        i = 0
        while i < len(lista_consultas):
            imprime_consulta(lista_consultas[i])
            i = i+1

    else:
        print("Não há consultas cadastradas!")



def imprime_consulta(c):
    i = 0
    medicamento = ''
    while i < len(c.medicamento):
        medicamento = c.medicamento[i] + " - " + medicamento
        i = i+1

    print(c.crm + " / " + c.cpf + " / " + str(c.data) + " / " + str(c.hora) + " / " + c.diagnostico + " / " + medicamento)

#--------------------------------------------------ARQUIVOS-MEDICOS-----------------------------------------------------

def escreve_arquivo_medicos(medicos,dados_medicos):
    arq = open(dados_medicos, "w")
    i = 0
    while i < len(medicos):
        m = medicos[i]
        arq.write(m.crm + ";" + m.nome + ";" + m.data + ";" + m.sexo + ";" + m.especialidade + ";" + m.universidade + ";" + str(m.email) + ";" + str(m.telefone) + "\n")
        i = i+1
    arq.close()


def ler_arquivo_medicos(dados_medicos):
    medicos = []
    arq = open(dados_medicos, "w")
    arq.close()
    arq = open(dados_medicos, "r")
    for linha in arq:
        infos = linha.split(";")
        m = Medico()
        m.crm = infos[0]
        m.nome = infos[1]
        m.data = infos[2]
        m.sexo = infos[3]
        m.especialidade = infos[4]
        m.universidade = infos[5]
        m.email = infos[6]
        m.telefone = infos[7]
        medicos.append(m)
    arq.close()
    return medicos



#--------------------------------------------------ARQUIVOS-PACIENTES---------------------------------------------------

def escreve_arquivo_pacientes(pacientes,dados_pacientes):
    arq = open(dados_pacientes, "w")
    i = 0
    while i < len(pacientes):
        p = pacientes[i]
        arq.write(p.cpf + ";" + p.nome + ";" + p.data + ";" + p.sexo + ";" + p.plano + ";" + str(p.email) + ";" + str(p.telefone) + "\n")
        i = i+1
    arq.close()


def ler_arquivo_pacientes(dados_pacientes):
    pacientes = []
    arq = open(dados_pacientes, "w")
    arq.close()
    arq = open(dados_pacientes, "r")
    for linha in arq:
        infos = linha.split(";")
        m = Medico()
        p.cpf = infos[0]
        p.nome = infos[1]
        p.data = infos[2]
        p.sexo = infos[3]
        p.plano = infos[4]
        p.email = infos[5]
        p.telefone = infos[6]
        pacientes.append(p)
    arq.close()
    return pacientes


#--------------------------------------------------ARQUIVOS-CONSULTAS---------------------------------------------------

def escreve_arquivo_consultas(consultas,dados_consultas):
    arq = open(dados_consultas, "w")
    i = 0
    while i < len(consultas):
        c = consultas[i]
        arq.write(c.crm + ";" + c.cpf + ";" + str(c.data) + ";" + str(c.hora) + ";" + c.diagnostico + ";" + str(c.medicamento) + "\n")
        i = i+1
    arq.close()


def ler_arquivo_consultas(dados_consultas):
    consultas = []
    arq = open(dados_consultas, "w")
    arq.close()
    arq = open(dados_consultas, "r")
    for linha in arq:
        infos = linha.split(";")
        c = Consulta()
        c.crm = infos[0]
        c.cpf = infos[1]
        c.data = infos[2]
        c.hora = infos[3]
        c.diagnostico = infos[4]
        c.medicamento = infos[5]
        consultas.append(c)
    arq.close()
    return consultas



#-----------------------------------------------------------------------------------------------------------------------

def main():
    arquivo_medicos = "dados_medicos.txt"
    arquivo_pacientes = "dados_pacientes.txt"
    arquivo_consultas = "dados_consultas.txt"
    medicos = ler_arquivo_medicos(arquivo_medicos)
    pacientes = ler_arquivo_pacientes(arquivo_pacientes)
    consultas = ler_arquivo_consultas(arquivo_consultas)
    medicos = []
    pacientes = []
    consultas = []
    j = ""
    while j != "5":
        j = menu()
        if j == "1":
            menu_medico(medicos)

        elif j == "2":
            menu_paciente(pacientes)

        elif j == "3":
            menu_consulta(consultas,medicos,pacientes)

        elif j == "4":
            menu_relatorio(consultas,medicos,pacientes)

        elif j == "5":
            escreve_arquivo_medicos(medicos, arquivo_medicos)
            escreve_arquivo_pacientes(pacientes, arquivo_pacientes)
            escreve_arquivo_consultas(consultas,arquivo_consultas)
            print("Obrigada por usar nosso sistema!")

        else:
            print("Opção Inválida. Tente novamente.")


main()
