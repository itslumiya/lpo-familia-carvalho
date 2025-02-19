# pip install aima3
from aima3.logic import expr,FolKB, fol_fc_ask

clauses = []

clauses.append(expr("Ascendente(Pietro,Joao)"))
clauses.append(expr("Ascendente(Pietro,Clara)"))
clauses.append(expr("Ascendente(Pietro,Francisco)"))
clauses.append(expr("Ascendente(Pietro,Valeria)"))
clauses.append(expr("Ascendente(Pietro,Ana)"))

clauses.append(expr("Ascendente(Antonita,Joao)"))
clauses.append(expr("Ascendente(Antonita,Clara)"))
clauses.append(expr("Ascendente(Antonita,Francisco)"))
clauses.append(expr("Ascendente(Antonita,Valeria)"))
clauses.append(expr("Ascendente(Antonita,Ana)"))

clauses.append(expr("Ascendente(Ana,Helena)"))
clauses.append(expr("Ascendente(Ana,Joana)"))

clauses.append(expr("Ascendente(Joao,Mario)"))

clauses.append(expr("Ascendente(Helena,Carlos)"))
clauses.append(expr("Ascendente(Mario,Carlos)"))

clauses.append(expr("Ascendente(Clara,Pietro2)"))
clauses.append(expr("Ascendente(Enzo,Pietro2)"))

clauses.append(expr("Ascendente(Jacynto,Francisca)"))
clauses.append(expr("Ascendente(Jacynto,Antonia)"))
clauses.append(expr("Ascendente(Claudia,Francisca)"))
clauses.append(expr("Ascendente(Claudia,Antonia)"))

clauses.append(expr("Ascendente(Luzia,Jacynto)"))
clauses.append(expr("Ascendente(Pablo,Jacynto)"))

clauses.append(expr("Sexo(Pietro1,Masculino)"))
clauses.append(expr("Sexo(Antonita,Feminino)"))
clauses.append(expr("Sexo(João,Masculino)"))
clauses.append(expr("Sexo(Clara,Feminino)"))
clauses.append(expr("Sexo(Francisco,Masculino)"))
clauses.append(expr("Sexo(Valeria,Feminino)"))
clauses.append(expr("Sexo(Ana,Feminino)"))
clauses.append(expr("Sexo(Helena,Feminino)"))
clauses.append(expr("Sexo(Joana,Feminino)"))
clauses.append(expr("Sexo(Mário,Masculino)"))
clauses.append(expr("Sexo(Fabiana,Feminino)"))
clauses.append(expr("Sexo(Pietro2,Masculino)"))
clauses.append(expr("Sexo(Enzo,Masculino)"))
clauses.append(expr("Sexo(Francisca,Feminino)"))
clauses.append(expr("Sexo(Antonia,Feminino)"))
clauses.append(expr("Sexo(Jacynto,Masculino)"))
clauses.append(expr("Sexo(Claudia,Feminino)"))
clauses.append(expr("Sexo(Pablo,Masculino)"))
clauses.append(expr("Sexo(Luzia,Feminino)"))


clauses.append(expr("Ascendente(x,y) ==> Pessoa(x)"))
clauses.append(expr("Ascendente(x,y) ==> Pessoa(y)"))

clauses.append(expr("Ascendente(x,y) ==> Descendente(y,x)"))
clauses.append(expr("Descendente(x,y) ==> Ascendente(y,x)"))

clauses.append(expr("Ascendente(x,y) & Sexo(x,Masculino) ==> Pai(x,y) "))
clauses.append(expr("Ascendente(x,y) & Sexo(x,Feminino) ==> Mae(x,y) "))

clauses.append(expr("Ascendente(x,y) & Ascendente(x,z) & Sexo(y,Masculino) ==> Irmao(y,z)"))
clauses.append(expr("Ascendente(x,y) & Ascendente(x,z) & Sexo(z,Masculino) ==> Irmao(z,y)"))

clauses.append(expr("Ascendente(x,y) & Ascendente(x,z) & Sexo(y,Feminino) ==> Irma(y,z)"))
clauses.append(expr("Ascendente(x,y) & Ascendente(x,z) & Sexo(z,Feminino) ==> Irma(z,y)"))

clauses.append(expr("Ascendente(x,y) & Ascendente(y,z) & Sexo(x,Masculino) ==> Avozinho(x,z)"))
clauses.append(expr("Ascendente(x,y) & Ascendente(y,z) & Sexo(x,Feminino) ==> Avozinha(x,z)"))

clauses.append(expr("Ascendente(x,y) & Irmao(x,z) ==> Tio(z,y)"))
clauses.append(expr("Ascendente(x,y) & Irma(x,z) ==> Tia(z,y)"))

clauses.append(expr("Tio(x,y) & Ascendente(x,z) & Sexo(z,Masculino) ==> Primo(z,y)"))
clauses.append(expr("Tio(x,y) & Ascendente(x,z) & Sexo(z,Feminino) ==> Prima(z,y)"))

Genealogia = FolKB(clauses)

perguntas = ["Sexo(x,Masculino)",
             "Sexo(x,Feminino)",
             "Irmao(x,Ana)",
             "Irma(x,Joao)",
             "Descendente(x,Maria)",
             "Descendente(Joao,x)",
             "Pessoa(x)",
             "Mae(x,y)",
             "Pai(x,y)"]



for i in perguntas:
    resposta = fol_fc_ask(Genealogia, expr(i))
    print("%s -> %s" %(i, (list(resposta))))


