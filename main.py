import netrc

def oqish():
    try:
        netrc_file = netrc.netrc()
        login, parol, host = netrc_file.authenticators('example.com')
        return login, parol
    except Exception as e:
        return None, None

def yozish(login, parol):
    try:
        netrc_file = netrc.netrc()
        netrc_file.authenticators('example.com', login, parol)
        netrc_file.write()
    except Exception as e:
        return False
    return True

def main():
    login, parol = oqish()
    if login and parol:
        print(f"Login: {login}, Parol: {parol}")
    else:
        login = input("Login: ")
        parol = input("Parol: ")
        if yozish(login, parol):
            print("Parol saqlandi")
        else:
            print("Parol saqlanmadi")

if __name__ == "__main__":
    main()
