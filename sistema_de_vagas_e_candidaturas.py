from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect (
    host = "localhost",
    user="root",
    passwd="",
    database="sistema_de_vagas_e_candidaturas"
)

stringEmailUsuario = ""
StringTipoLogin = ""

def encaminharLogin(tipoUsuario):
    if tipoUsuario == "empresas":
        empresa_ou_candidato.close()
        empresa_login.show()        
    else:
        empresa_ou_candidato.close()
        candidato_login.show()

def criarLogin(tipoLogin):
        email = candidato_login.emailCandidato.text()
        senha = candidato_login.senhaCandidato.text()
        cursor = banco.cursor()
        comandoSql1="SELECT email FROM login WHERE email = "
        comandoSql1= comandoSql1+"'"+str(email)+"'"
        #dados1 = (str(email))
        print(comandoSql1)
        cursor.execute(comandoSql1)
        dados_lidos1= cursor.fetchall()
        #print(dados_lidos1)

        if not dados_lidos1: 
            cursor2 = banco.cursor()
            comandoSql2="INSERT INTO login(tipo,email,senha) VALUES (%s,%s,%s)"
            dados2 = (tipoLogin,str(email),str(senha))
            stringEmailUsuario = str(email)
            StringTipoLogin = tipoLogin
            cursor2.execute(comandoSql2,dados2)
            banco.commit()
            candidato_login.close()
            menuCandidatos.show()

        else:
            candidato_login.mensagemCadastroOuEntrar.setText("Usuário já cadastrado, favor fazer login")
            #print(stringEmailUsuario,StringTipoLogin)

def criarLoginEmpresa(tipoLogin):
        email = empresa_login.emailEmpresa.text()
        senha = empresa_login.senhaEmpresa.text()
        cursor = banco.cursor()
        comandoSql1="SELECT email FROM login WHERE email = "
        comandoSql1= comandoSql1+"'"+str(email)+"'"
        #dados1 = (str(email))
        print(comandoSql1)
        cursor.execute(comandoSql1)
        dados_lidos1= cursor.fetchall()
        #print(dados_lidos1)

        if not dados_lidos1: 
            cursor2 = banco.cursor()
            comandoSql2="INSERT INTO login(tipo,email,senha) VALUES (%s,%s,%s)"
            dados2 = (tipoLogin,str(email),str(senha))
            stringEmailUsuario = str(email)
            StringTipoLogin = tipoLogin
            cursor2.execute(comandoSql2,dados2)
            banco.commit()
            empresa_login.close()
            menuEmpresas.show()

        else:
            candidato_login.mensagemCadastroOuEntrar.setText("Empresa já cadastrado, favor fazer login")
            #print(stringEmailUsuario,StringTipoLogin)

def fazerLogin():
        emailEntrar = candidato_login.emailCandidato.text()
        senhaEntrar = candidato_login.senhaCandidato.text()
        cursor = banco.cursor()
        comandoSql1="SELECT email,senha FROM login WHERE email = "
        comandoSql1= comandoSql1+"'"+str(emailEntrar)+"' and senha ='"+str(senhaEntrar)+"'"
        #dados1 = (str(email))
        #print(comandoSql1)
        cursor.execute(comandoSql1)
        dados_lidos1= cursor.fetchall()
        #print(dados_lidos1)

        if not dados_lidos1: 
            candidato_login.mensagemCadastroOuEntrar.setText("email ou senha incorreto, favor tentar login novamente")

        else:
            stringEmailUsuario = str(emailEntrar)
            StringTipoLogin = str(senhaEntrar)
            #print(stringEmailUsuario,StringTipoLogin)    
            candidato_login.close()
            menuCandidatos.show()

def fazerLoginEmpresa():
        emailEntrar = empresa_login.emailEmpresa.text()
        senhaEntrar = empresa_login.senhaEmpresa.text()
        cursor = banco.cursor()
        comandoSql1="SELECT email,senha FROM login WHERE email = "
        comandoSql1= comandoSql1+"'"+str(emailEntrar)+"' and senha ='"+str(senhaEntrar)+"'"
        #dados1 = (str(email))
        #print(comandoSql1)
        cursor.execute(comandoSql1)
        dados_lidos1= cursor.fetchall()
       # print(dados_lidos1)

        if not dados_lidos1: 
            candidato_login.mensagemCadastroOuEntrar.setText("email ou senha incorreto, favor tentar login novamente")

        else:
            stringEmailUsuario = str(emailEntrar)
            StringTipoLogin = str(senhaEntrar)
            empresa_login.close()
            menuEmpresas.show()   
            #print(stringEmailUsuario,StringTipoLogin)                                 
                   
def chamarCadastroUsuario():
    cadastrar_candidato.show()
    menuCandidatos.close()

def voltarMenuCandidato():
    cadastrar_candidato.close()
    menuCandidatos.show()

def cadastrarCandidato():
    #capturando dados digitados
    linha1 = cadastrar_candidato.nomeCandidato.text()
    linha2 = cadastrar_candidato.pretensaoSalarial.text()
    texto1 = cadastrar_candidato.experiencia.toPlainText()
    linha4 = cadastrar_candidato.ultimaEscolaridade.text()
    linha5 = cadastrar_candidato.emailCandidato.text()
    #with open('experiencia.txt','a') as f: f.write(linha3)

    #abrindo ponteiro de varredura
    cursor = banco.cursor()
    
    #%s representa os dados a serem inseridos
    comando_SQL= "INSERT INTO candidato(nome,pretensao,experiencia,escolaridade,emailCandidato) VALUES(%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(texto1),str(linha4),str(linha5))
    #execuntando comando SQL
    cursor.execute(comando_SQL,dados)
    #salvando operação no banco
    banco.commit()

    cadastrar_candidato.nomeCandidato.setText("")
    cadastrar_candidato.pretensaoSalarial.setText("")
    cadastrar_candidato.experiencia.setText("")
    cadastrar_candidato.ultimaEscolaridade.setText("")
    cadastrar_candidato.emailCandidato.setText("")

def mostrarVagasParaCandidato():
    menuCandidatos.close()
    muralVagas.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM vaga"
    cursor.execute(comando_SQL)
    #salvando registros da tabela na variável
    dados_lidos = cursor.fetchall()
    #atribuindo quantidade de registros por linha e coluna
    muralVagas.tableWidget.setRowCount(len(dados_lidos))
    muralVagas.tableWidget.setColumnCount(6)

    #varrendo dados
    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
            #atribuindo os dados ao item da tabela baseado na linha e na coluna
            muralVagas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def mostrarVagasParaEmpresa():
    menuEmpresas.close()
    MuralVagasCandidatoEmpresas.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM candidaturaVaga"
    cursor.execute(comando_SQL)
    #salvando registros da tabela na variável
    dados_lidos = cursor.fetchall()
    #atribuindo quantidade de registros por linha e coluna
    MuralVagasCandidatoEmpresas.tableWidget.setRowCount(len(dados_lidos))
    MuralVagasCandidatoEmpresas.tableWidget.setColumnCount(11)

    #varrendo dados
    for i in range(0, len(dados_lidos)):
        for j in range(0, 11):
            #atribuindo os dados ao item da tabela baseado na linha e na coluna
            MuralVagasCandidatoEmpresas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def fazerCandidatura():
    strCodigoVaga = str(muralVagas.codigoVaga.text())
    strEmailCandidato = str(muralVagas.emailCandidato.text())

    if (not strCodigoVaga) & (not strEmailCandidato):
        muralVagas.mensagemDePreenchimento.setText("Favor digitar os dados, o código ou o email está nulo")
    else:
        cursor = banco.cursor()
        comandoSqlConsultaVaga = "SELECT nome,faixa_salarial,requisitos,escolaridade_minima,email_empresa FROM vaga WHERE id="+strCodigoVaga
        cursor.execute(comandoSqlConsultaVaga)
        dados_vaga = cursor.fetchall()
        if not dados_vaga:
            muralVagas.mensagemDePreenchimento.setText("código incorreto, tente novamente")
        else:     
             nomeVaga= dados_vaga[0][0]
             faixaSalarial = dados_vaga[0][1]
             requisitos= dados_vaga[0][2]
             escolaridade_minima= dados_vaga[0][3]
             email_empresa = dados_vaga[0][4]

        comandoSqlConsultaCandidato = "SELECT nome,pretensao,experiencia,escolaridade,emailCandidato FROM candidato WHERE emailCandidato='"+strEmailCandidato+"'"
        cursor.execute(comandoSqlConsultaCandidato)
        dados_candidato= cursor.fetchall()
        if not dados_candidato:
            muralVagas.mensagemDePreenchimento.setText("email incorreto, tente novamente")
        else:   
            nomeCandidato = dados_candidato[0][0]
            pretensao = dados_candidato[0][1]
            experiencia = dados_candidato[0][2] 
            escolaridade = dados_candidato[0][3]
            email_candidato = dados_candidato[0][4]

        if (not not dados_vaga) & (not not dados_candidato):
            comandoSqlInserirCandidaturaVaga = "INSERT INTO candidaturavaga(nomeVaga,faixa_salarial,requisitos,escolaridade_minima,email_empresa,nomeCandidato,pretensao,experiencia,escolaridade,emailCandidato) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            dados_candidatoVaga= (str(nomeVaga),str(faixaSalarial),str(requisitos),str(escolaridade_minima),str(email_empresa),str(nomeCandidato),pretensao,str(experiencia),str(escolaridade),str(email_candidato))
            cursor.execute(comandoSqlInserirCandidaturaVaga,dados_candidatoVaga)
            banco.commit()

            muralVagas.codigoVaga.setText("")
            muralVagas.emailCandidato.setText("")
            muralVagas.mensagemDePreenchimento.setText("")

def voltarMural():
    muralVagas.close()
    menuCandidatos.show();
    muralVagas.mensagemDePreenchimento.setText("")

def deslogarCandidato():
    menuCandidatos.close();
    empresa_ou_candidato.show()

def deslogarEmpresa():
    menuEmpresas.close()
    empresa_ou_candidato.show()

def chamar_cadastro_de_vagas():
    menuEmpresas.close()
    cadastrar_empresas_ui.show()

def cadastrar_vagas():
    linha1 = cadastrar_empresas_ui.nomeVaga.text()
    texto1 = cadastrar_empresas_ui.requisitos.toPlainText()
    email_empresa = cadastrar_empresas_ui.emailEmpresaVaga.text()

    faixa_salarial = ""
    escolaridade= ""

    if cadastrar_empresas_ui.rb1000.isChecked():
        faixa_salarial = "até 1000"
        #print("faixa salarial ",faixa_salarial,"foi selecionada")
    elif cadastrar_empresas_ui.rb10002000.isChecked():
        faixa_salarial = "de 1000 até 2000"
        #print("faixa salarial ",faixa_salarial,"foi selecionada")        
    elif cadastrar_empresas_ui.rb20003000.isChecked():
        faixa_salarial= "de 2000 até 3000"
        #print("faixa salarial ",faixa_salarial,"foi selecionada")                
    elif cadastrar_empresas_ui.rbmaior3000.isChecked():
        faixa_salarial = "acima de 3000"
        #print("faixa salarial ",faixa_salarial,"foi selecionada")                        
    
    if cadastrar_empresas_ui.rbfundamental.isChecked():
        escolaridade ="Ensino fundamental"
        #print(escolaridade)
    elif cadastrar_empresas_ui.rbEnsinoMedio.isChecked():
        escolaridade ="Ensino médio"
        #print(escolaridade)
    elif cadastrar_empresas_ui.rvTecnologo.isChecked():   
        escolaridade="Tecnólogo"
        #print(escolaridade)
    elif cadastrar_empresas_ui.rbEnsinoSuperior.isChecked():
        escolaridade="Ensino Superior"
        #print(escolaridade)
    elif cadastrar_empresas_ui.rbPos.isChecked():
        escolaridade="Pós / MBA / Mestrado"
        #print(escolaridade)
    else:  
        escolaridade="Doutorado"  
        #print(escolaridade)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO vaga(nome,faixa_salarial,requisitos,escolaridade_minima,email_empresa) VALUES(%s,%s,%s,%s,%s)"
    dados = (str(linha1),faixa_salarial,str(texto1),escolaridade,str(email_empresa))
    cursor.execute(comando_SQL,dados)
    banco.commit()

    cadastrar_empresas_ui.nomeVaga.setText("")
    cadastrar_empresas_ui.requisitos.setText("")
    cadastrar_empresas_ui.emailEmpresaVaga.setText("")

def voltarMenuEmpesas():
    cadastrar_empresas_ui.close()
    menuEmpresas.show()

def voltarMenuEmpresasDoEditarVagas():
     MuralVagasCandidatoEmpresas.codigoVagaMuralComCandidatos.setText("")
     MuralVagasCandidatoEmpresas.close()
     menuEmpresas.show()

def excluirVaga():
    codigoVaga = MuralVagasCandidatoEmpresas.codigoVagaMuralComCandidatos.text()
    emailEmpresa = str(MuralVagasCandidatoEmpresas.emailEmpresaMuralVagasComCandidatos.text())

    cursor = banco.cursor()
    comandoSql= "DELETE FROM candidaturaVaga WHERE id="+codigoVaga
    cursor.execute(comandoSql)

    cursor = banco.cursor()
    comandoSql2= "DELETE FROM vaga WHERE email_empresa='"+emailEmpresa+"'"
    cursor.execute(comandoSql2)
    banco.commit()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM candidaturaVaga"
    cursor.execute(comando_SQL)
    #salvando registros da tabela na variável
    dados_lidos = cursor.fetchall()
    #atribuindo quantidade de registros por linha e coluna
    MuralVagasCandidatoEmpresas.tableWidget.setRowCount(len(dados_lidos))
    MuralVagasCandidatoEmpresas.tableWidget.setColumnCount(11)

    #varrendo dados
    for i in range(0, len(dados_lidos)):
        for j in range(0, 11):
            #atribuindo os dados ao item da tabela baseado na linha e na coluna
            MuralVagasCandidatoEmpresas.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    MuralVagasCandidatoEmpresas.codigoVagaMuralComCandidatos.setText("")
    MuralVagasCandidatoEmpresas.emailEmpresaMuralVagasComCandidatos.setText("")

def encerrar():
    empresa_ou_candidato.close()

app = QtWidgets.QApplication([])    
empresa_ou_candidato = uic.loadUi("EmpresaOuCandidato.ui")
empresa_login = uic.loadUi("loginInSignInEmpresa.ui")
empresa_login.pbEntrarEmpresa.clicked.connect(lambda:fazerLoginEmpresa())
empresa_login.pbCadastrarEmpresa.clicked.connect(lambda:criarLoginEmpresa("empresas"))
empresa_ou_candidato.pbEmpresas.clicked.connect(lambda:encaminharLogin("empresas"))
empresa_ou_candidato.pbCandidatos.clicked.connect(lambda:encaminharLogin("candidatos"))
empresa_ou_candidato.pbEncerrarPrograma.clicked.connect(lambda:encerrar())
candidato_login = uic.loadUi("loginInSignInCandidato.ui")
candidato_login.pbCadastrarCandidato.clicked.connect(lambda:criarLogin("candidato"))
candidato_login.pbEntarCandidatos.clicked.connect(lambda:fazerLogin())
menuCandidatos = uic.loadUi("menuCandidatos.ui")
menuCandidatos.pbCadastroMenuCandidato.clicked.connect(lambda:chamarCadastroUsuario())
menuCandidatos.pbConsultarVagas.clicked.connect(lambda:mostrarVagasParaCandidato())
menuCandidatos.pbSairMenu.clicked.connect(lambda:deslogarCandidato())
cadastrar_candidato = uic.loadUi("cadastroCandidato.ui")
cadastrar_candidato.botaoVoltarCandidato.clicked.connect(lambda:voltarMenuCandidato())
cadastrar_candidato.botaoCadastrarCandidato.clicked.connect(lambda:cadastrarCandidato())
muralVagas = uic.loadUi("MuralVagasCandidato.ui")
muralVagas.pbCandidatarMural.clicked.connect(lambda:fazerCandidatura())
muralVagas.pbVolarMuralVagas.clicked.connect(lambda:voltarMural())
menuEmpresas = uic.loadUi("menuEmpresas.ui")
menuEmpresas.pbCadastrarVagas.clicked.connect(lambda:chamar_cadastro_de_vagas())
menuEmpresas.pbEditarVagas.clicked.connect(lambda:mostrarVagasParaEmpresa())
menuEmpresas.pbDeslogarMenuEmpresas.clicked.connect(lambda:deslogarEmpresa())
cadastrar_empresas_ui = uic.loadUi("cadastroVagas.ui")    
cadastrar_empresas_ui.pbCriarVaga.clicked.connect(lambda:cadastrar_vagas())
cadastrar_empresas_ui.pbVoltar.clicked.connect(lambda:voltarMenuEmpesas())
MuralVagasCandidatoEmpresas = uic.loadUi("MuralVagasCandidatoEmpresas.ui")
MuralVagasCandidatoEmpresas.ExcluirVagaComCandidato.clicked.connect(lambda:excluirVaga())
MuralVagasCandidatoEmpresas.pbVolarMuralVagasComCandidatos.clicked.connect(lambda:voltarMenuEmpresasDoEditarVagas())


empresa_ou_candidato.show()
app.exec()

"""

create table candidato (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45),
    pretensao DOUBLE,
    experiencia VARCHAR(400),
    escolaridade VARCHAR(30),
    emailCandidato VARCHAR(100),
    PRIMARY KEY (id)
    );

    create table vaga(
     id INT NOT NULL AUTO_INCREMENT,
     nome VARCHAR(40),
     faixa_salarial VARCHAR(60),
     requisitos VARCHAR(400),
     escolaridade_minima VARCHAR(70),
     email_empresa VARCHAR(100),
     PRIMARY KEY (id)
 );
    create table login(
        id INT NOT NULL AUTO_INCREMENT,
        tipo VARCHAR(30),
        email VARCHAR(300),
        senha VARCHAR(300),
        PRIMARY KEY (id)
    );


    create table candidaturaVaga(
        id INT NOT NULL AUTO_INCREMENT,
        nomeVaga VARCHAR(40),
        faixa_salarial VARCHAR(60),
        requisitos VARCHAR(400),
        escolaridade_minima VARCHAR(70),
        email_empresa VARCHAR(100),
        nomeCandidato VARCHAR(45),
        pretensao DOUBLE,
        experiencia VARCHAR(400),
        escolaridade VARCHAR(30),
        emailCandidato VARCHAR(100),
        PRIMARY KEY (id)
    );

    
"""