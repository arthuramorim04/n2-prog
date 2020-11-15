import psycopg2

from connection import Connect


def inputName():
    nome = input("Nome: ")
    return nome


def inputCPF():
    cpf = input("CPF: ")
    return cpf


def inputEmail():
    email = input("E-mail: ")
    return email


def valid_cpf(cpf_val):
    if cpf_val.isdigit() == True and len(cpf_val) == 11:
        return 1

    else:
        return 0


def nameValidator(nome_val):
    if len(nome_val) <= 150:
        return 1

    else:
        return 0


def validate_email(email_val):
    if len(email_val) <= 400:
        return 1
    else:
        return 0


def mainMenu():
    opcao = int(input(("1- Inserir\n"
                       "2- Buscar\n"
                       "3- Alterar\n"
                       "4- Excluir\n"
                       "0- Sair\n\n"
                       )))
    operations(opcao)


def operations(opcao):
    if opcao == 1:

        cpf = inputCPF()
        cpf_valido = valid_cpf(cpf)

        if cpf_valido == 1:

            nome = inputName()
            nome_valido = nameValidator(nome)

            email = inputEmail()
            email_valido = validate_email(email)

            if nome_valido == 1 and email_valido == 1:
                conn = Connection().getConnection()
                cur = conn.cursor()
                cur.execute(
                    "insert into pessoa (nome, cpf, email, logado) values ('{0}','{1}','{2}','3')".format(nome, cpf,
                                                                                                          email))

                conn.commit()
                conn.close()

                mainMenu()

            else:
                mainMenu()

        else:
            mainMenu()


    elif opcao == 2:

        acao_select = int(input(
            "O que gostaria de fazer?\n3- Ver tudo\n2- Consultar por CPF\n3- Consultar por email\n4- Sair\n\nDIGITE: "))

        if acao_select == 1:
            conn = Connection().getConnection()
            cur = conn.cursor()
            cur.execute("select * from pessoa where logado = '3'")

            rows = cur.fetchall()

            for row in rows:
                print(row[0], str(row[1]), row[2], row[3])
                conn.close()
                mainMenu()


        elif acao_select == 2:

            cpf = inputCPF()
            cpf_valido = valid_cpf(cpf)

            if cpf_valido == 1:
                conn = Connection().getConnection()
                cur = conn.cursor()
                cur.execute("select * from pessoa where logado = '3' and cpf = '{0}'".format(cpf))
                rows = cur.fetchall()

            for row in rows:
                print(row[0], str(row[1]), row[2], row[3])

                conn.close()
                mainMenu()

            else:
                mainMenu()


        elif acao_select == 3:

            email = inputEmail()
            email_valido = validate_email(email)

            if email_valido == 1:
                conn = Connection().getConnection()
                cur = conn.cursor()
                cur.execute("select * "
                            "from pessoa "
                            "where logado = '3' "
                            "and email = '{0}'".format(email))

                rows = cur.fetchall()

            for row in rows:
                print(row[0], str(row[1]), row[2], row[3])

                conn.close()
                mainMenu()

            else:
                print("Email não encontrado.")
                mainMenu()


        elif acao_select == 4:
            print("Opção finalizada.")
            mainMenu()


        else:
            print("Opção inválida.")
            mainMenu()



    elif opcao == 3:

        acao_select = int(input("\n1- Atualizar nome\n2- Atualizar email\n3- Sair\n\n"))

        if acao_select == 1:

            cpf = inputCPF()
            cpf_valido = valid_cpf(cpf)

            nome = inputName()
            nome_valido = nameValidator(nome)

            if nome_valido == 1:
                conn = Connection().getConnection()

                cur = conn.cursor()
                cur.execute("update pessoa "
                            "set nome = '{0}' "
                            "where cpf = '{1}'".format(nome, cpf))
                conn.commit()
                conn.close()

            else:
                print("Nome inválido. Tente novamente.")


        elif acao_select == 2:

            cpf = inputCPF()
            cpf_valido = valid_cpf(cpf)

            email = inputEmail()
            email_valido = validate_email(email)

            if email_valido == 1:

                conn = Connection().getConnection()

                cur = conn.cursor()
                cur.execute("Update pessoa"
                            " set email = '{0}'"
                            .format(email))
                conn.commit()
                conn.close()

            else:
                print("Email inválido.")
                mainMenu()


        elif acao_select == 3:
            mainMenu()

        else:
            print("Opção inválida.")
            mainMenu()


    elif opcao == 4:

        cpf = inputCPF()
        cpf_valido = valid_cpf(cpf)

        if cpf_valido == 1:

            conn = Connect().getConnection()

            cur = conn.cursor()
            cur.execute("update pessoa"
                        " set logado = 0"
                        " where cpf = '{0}'"
                        .format(cpf))
            conn.commit()

            conn.close()
            mainMenu()

        else:
            print("CPF inválido. => ", cpf)


    elif opcao == 0:
        print("Exit.")
        exit()


    else:
        print("Opção invalida")
        mainMenu()