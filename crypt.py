from cryptography import fernet

while 1:
    print("""
what do you want to do?
1) encrypt
2) decrypt
""")
    i = input("default [1]: ")
    if i == '':
        c = 1
    else:
        try:
            c = int(i)
        except ValueError:
            continue

    if c == 1:
        key = fernet.Fernet.generate_key()
        print(f"save this *key*: {key.decode()}")
        msg = input("enter message: ").encode()
        print("how many times do you want to encrypt it?\ni recommend no more than 3 times")
        i = input("default [1]: ")
        if i == '':
            c = 1
        else:
            c = int(i)
        
        result = fernet.Fernet(key).encrypt(msg)

        while c > 1:
            result = fernet.Fernet(key).encrypt(result)
            c -= 1
        
        print()
        print(f"result: {result.decode()}")
    elif c == 2:
        key = input("enter key: ").encode()
        msg = input("enter message: ").encode()
        try:
            result = fernet.Fernet(key).decrypt(msg)
        except:
            print("\n\nsomething is wrong \n\n")
            continue
        
        while 1:
            try:
                result = fernet.Fernet(key).decrypt(result)
            except:
                break
        
        print()
        print(f"result: {result.decode()}")
    
    print()
    i = input('anything else? [N/y]: ').lower()
    if i == 'n' or i == '':
        break
    else:
        continue