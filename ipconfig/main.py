def ipClassFinder(ipAdress):
    ipPrefix=int(ipAdress.split(".")[0])
    if ipPrefix>=0 and ipPrefix<=127:
        print("Class A IP Adress")
    elif ipPrefix>=128 and ipPrefix<=191:
        print("Class B IP Adress")
    elif ipPrefix>=192 and ipPrefix<=223:
        print("Class C IP Adress")
    elif ipPrefix>=224 and ipPrefix<=239:
        print("Class D IP Adress")
    elif ipPrefix>=240 and ipPrefix<=255:
        print("Class E IP Adress")
    else:
        print("Invalid IP Adress")

ip=input("Enter an IP Adress: ")
ipClassFinder(ip)