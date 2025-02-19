# pip install aima3
from aima3.logic import expr,FolKB, fol_fc_ask

clauses = []

clauses.append(expr("Progenitor(Pietro,Joao)"))
clauses.append(expr("Progenitor(Pietro,Clara)"))
clauses.append(expr("Progenitor(Pietro,Francisco)"))
clauses.append(expr("Progenitor(Pietro,Valeria)"))
clauses.append(expr("Progenitor(Pietro,Ana)"))

clauses.append(expr("Progenitor(Antonita,Joao)"))
clauses.append(expr("Progenitor(Antonita,Clara)"))
clauses.append(expr("Progenitor(Antonita,Francisco)"))
clauses.append(expr("Progenitor(Antonita,Valeria)"))
clauses.append(expr("Progenitor(Antonita,Ana)"))

clauses.append(expr("Progenitor(Ana,Helena)"))
clauses.append(expr("Progenitor(Ana,Joana)"))

clauses.append(expr("Progenitor(Joao,Mario)"))

clauses.append(expr("Progenitor(Helena,Carlos)"))
clauses.append(expr("Progenitor(Mario,Carlos)"))

clauses.append(expr("Progenitor(Clara,Pietro2)"))
clauses.append(expr("Progenitor(Enzo,Pietro2)"))

clauses.append(expr("Progenitor(Jacynto,Francisca)"))
clauses.append(expr("Progenitor(Jacynto,Antonia)"))
clauses.append(expr("Progenitor(Claudia,Francisca)"))
clauses.append(expr("Progenitor(Claudia,Antonia)"))

clauses.append(expr("Progenitor(Luzia,Jacynto)"))
clauses.append(expr("Progenitor(Pablo,Jacynto)"))

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


clauses.append(expr("Progenitor(x,y) ==> Pessoa(x)"))
clauses.append(expr("Progenitor(x,y) ==> Pessoa(y)"))

clauses.append(expr("Acendente(x,y) ==> Descendente(y,x)"))
clauses.append(expr("Descendente(x,y) ==> Acendente(y,x)"))

clauses.append(expr("Acendente(x,y) & Sexo(x,Masculino) ==> Pai(x,y) "))
clauses.append(expr("Acendente(x,y) & Sexo(x,Feminino) ==> Mae(x,y) "))

clauses.append(expr("Acendente(x,y) & Acendente(x,z) & Sexo(y,Masculino) ==> Irmao(y,z)"))
clauses.append(expr("Acendente(x,y) & Acendente(x,z) & Sexo(z,Masculino) ==> Irmao(z,y)"))

clauses.append(expr("Acendente(x,y) & Acendente(x,z) & Sexo(y,Feminino) ==> Irma(y,z)"))
clauses.append(expr("Acendente(x,y) & Acendente(x,z) & Sexo(z,Feminino) ==> Irma(z,y)"))

clauses.append(expr("Acendente(x,y) & Acendente(y,z) & Sexo(y,Masculino) ==> Avozinho(x,z)"))
clauses.append(expr("Acendente(x,y) & Acendente(y,z) & Sexo(y,Feminino) ==> Avozinha(x,z)"))

clauses.append(expr("Acendente(x,y) & Irmao(x,z) ==> Tio(z,y)"))
clauses.append(expr("Acendente(x,y) & Irma(x,z) ==> Tia(z,y)"))

clauses.append(expr("Tio(x,y) & Acendente(x,z) & Sexo(z,Masculino) ==> Primo(z,y)"))
clauses.append(expr("Tia(x,y) & Acendente(x,z) & Sexo(z,Masculino) ==> Primo(z,y)"))

clauses.append(expr("Tio(x,y) & Acendente(x,z) & Sexo(z,Feminino) ==> Primo(z,y)"))
clauses.append(expr("Tia(x,y) & Acendente(x,z) & Sexo(z,Feminino) ==> Primo(z,y)"))

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


