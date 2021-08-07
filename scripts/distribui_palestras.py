import pandas as pd

def trata_entrada():
	entrada = pd.read_excel("entrada-revisada.xlsx")
	entrada = entrada[entrada[entrada.columns[1]]=="Português"].copy()
	entrada[entrada.columns[3]]=entrada[entrada.columns[3]].apply(lambda x : x.strip())
	entrada = entrada[entrada[entrada.columns[22]]=="Palestra"].copy()
	entrada = entrada.drop(columns=entrada.columns.values[32:])
	entrada = entrada.drop(columns=entrada.columns.values[4:23])
	entrada = entrada.drop(columns=entrada.columns.values[5:8])
	entrada = entrada.drop(columns=entrada.columns.values[0:2])
	entrada = entrada.sort_values(by=[entrada.columns[1]], ignore_index=True)
	entrada = entrada.reset_index()
	return entrada

def distribui_palestras():
	""" Para cada posição na lista de entrada, ele atribuirá 3 palestras.
	% len(entrada) é utilizado para atribuir as palestras circularmente."""
	entrada = trata_entrada()
	entrada["avaliador1"] = entrada.apply(lambda x: entrada[entrada.columns[1]].iloc[(x.name+(9*1))%len(entrada)], axis=1)
	entrada["avaliador2"] = entrada.apply(lambda x: entrada[entrada.columns[1]].iloc[(x.name+(9*2))%len(entrada)], axis=1)
	entrada["avaliador3"] = entrada.apply(lambda x: entrada[entrada.columns[1]].iloc[(x.name+(9*3))%len(entrada)], axis=1)
	entrada["email1"] = entrada.apply(lambda x: entrada[entrada.columns[2]].iloc[(x.name+(9*1))%len(entrada)], axis=1)
	entrada["email2"] = entrada.apply(lambda x: entrada[entrada.columns[2]].iloc[(x.name+(9*2))%len(entrada)], axis=1)
	entrada["email3"] = entrada.apply(lambda x: entrada[entrada.columns[2]].iloc[(x.name+(9*3))%len(entrada)], axis=1)
	aux1=entrada.copy().drop(columns=["email2","email3","avaliador2","avaliador3"]).rename(columns={"email1":"email","avaliador1":"avaliador"})
	aux2=entrada.copy().drop(columns=["email1","email3","avaliador1","avaliador3"]).rename(columns={"email2":"email","avaliador2":"avaliador"})
	aux3=entrada.copy().drop(columns=["email1","email2","avaliador1","avaliador2"]).rename(columns={"email3":"email","avaliador3":"avaliador"})
	saida = pd.concat([aux1, aux2, aux3],ignore_index=True)
	saida.to_excel("teste-saida.xlsx")
	return saida
print(distribui_palestras())
