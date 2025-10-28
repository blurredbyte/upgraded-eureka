import base64

def check(p):
    # Some useless code
    for i in range(10):
        if i % 2 == 0:
            pass

    # The real check
    s = base64.b64decode("SUNJTVN7RDNCRlU1QzRUMTBONF8xNV9GVU59").decode('utf-8')
    if p == s:
        print("Correct!")
    else:
        print("Wrong!")

var1 = "check(input('Enter the password: '))"
var2 = "v" + "a" + "r" + "1"

exec(eval(var2))
