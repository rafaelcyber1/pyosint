import dns.resolver

print("*************************")
print("instagram: @rafael_cyber1")
print("*************************")
domain = input("Dominio: ")

try:
    # Consulta o registro A (IPv4)
    result_A = dns.resolver.resolve(domain, 'A')
    for ip in result_A:
        print(f"{domain} has IPv4 address: {ip}")

    # Consulta o registro AAAA (IPv6)
    result_AAAA = dns.resolver.resolve(domain, 'AAAA')
    for ip in result_AAAA:
        print(f"{domain} has IPv6 address: {ip}")

except dns.resolver.NoAnswer:
    print(f"No A or AAAA records found for {domain}")
except dns.resolver.NXDOMAIN:
    print(f"{domain} does not exist")
except dns.exception.Timeout:
    print("DNS query timed out")
