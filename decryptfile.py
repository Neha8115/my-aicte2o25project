message = ""
n = 0
m = 0
z = 0

pas = input("hello")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:",decrypted)
else:
    print("YOU ARE NOT auth")
