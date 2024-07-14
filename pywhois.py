import whois
print("*************************")
print("instagram: @rafael_cyber1")
print("*************************")
dominio = input("Dominio: ")
consulta_whois = whois.whois(dominio)
print(consulta_whois.text)
