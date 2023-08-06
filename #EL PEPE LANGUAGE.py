#EL PEPE LANGUAGE
print(f"""
EL PEPE LANG (2023) Copyright @MrZeussim.
CURRENT FILE: {__file__}
      """)

ERRORCODES = {
    100: f"ERR100: ERROR DE VALOR \n({__file__})",
    200: f"ERR200: ERROR DE SINTAXIS \n({__file__})",
    300: f"ERR300: ERROR DE DIVISIÓN ENTRE CERO \n({__file__})",
    400: f"ERR400: ERROR DE COMANDO NO ENCONTRADO \n({__file__})"
}

def on_print(arguments):
    print(f"{arguments}")

def on_suma(digits):
    initNum = 0
    for i in digits:
        try:
            num = float(i)
            initNum += num
        except:
            print(ERRORCODES[100])
            return
    print(initNum)
    return initNum
    
def on_resta(digits):
    initNum = 0
    subCount = 0
    for i in digits:
        subCount += 1
        try:
            if subCount == 1:
                initNum += float(i)
            else:
                num = float(i)
                initNum -= num
        except:
            print(ERRORCODES[100])
            return
    print(initNum)
    return initNum
    
def on_mul(digits):
    initNum = 1
    for i in digits:
        try:
            
            num = float(i)
            initNum *= num
        except:
            print(ERRORCODES[100])
            return
    print(initNum)
    return initNum
    
def on_div(digits):
    initNum = 0
    subCount = 0
    for i in digits:
        subCount += 1
        try:
            if subCount == 1:
                initNum += float(i)
            else:
                try:
                    num = float(i)
                    initNum /= num
                except ZeroDivisionError:
                    print(ERRORCODES[300])
                    return

        except:
            print(ERRORCODES[100])
            return
    print(initNum)
    return initNum
    
while True:
    inputType = input("\n>>> ")
    #command-(arguments);
    if inputType.startswith("#") is True and inputType.endswith(");") is True:
        splited = inputType.split("-", maxsplit=1)
        if splited[0] == "#imprimir":
            """FORMAT: #imprimir-("argumento");"""
            if splited[1].startswith("(\"") is True and splited[1].endswith("\");") is True:
                textToPrint = splited[1].replace("(\"", "").replace("\");", "")
                on_print(textToPrint)
            else:
                print(f"{ERRORCODES[200]}- El formato correcto es #imprimir-(\"argumento\");")
        elif splited[0] == "#sumar":
            """FORMAT: #sumar-(num + num);"""
            if splited[1].startswith("(") is True and splited[1].endswith(");") is True:
                textToSum = splited[1].replace("(", "").replace(");", "").split("+")
                on_suma(textToSum)
            else:
                print(f"{ERRORCODES[200]}- El formato correcto es #sumar-(x + y + z);")
        elif splited[0] == "#restar":
            """FORMAT: #sumar-(num - num);"""
            if splited[1].startswith("(") is True and splited[1].endswith(");") is True:
                textToRest = splited[1].replace("(", "").replace(");", "").split("-")
                on_resta(textToRest)
            else:
                print(f"{ERRORCODES[200]}- El formato correcto es #restar-(x - y - z);")
        elif splited[0] == "#mul":
            """FORMAT: #multipli-(num * num);"""
            if splited[1].startswith("(") is True and splited[1].endswith(");") is True:
                textToMul = splited[1].replace("(", "").replace(");", "").split("*")
                on_mul(textToMul)
            else:
                print(f"{ERRORCODES[200]}- El formato correcto es #mul-(x * y * z);")
        elif splited[0] == "#div":
            """FORMAT: #sumar-(num / num);"""
            if splited[1].startswith("(") is True and splited[1].endswith(");") is True:
                textToDiv = splited[1].replace("(", "").replace(");", "").split("/")
                on_div(textToDiv)
            else:
                print(f"{ERRORCODES[200]}- El formato correcto es #div-(x / y / z);")
        else:
            print(f"{ERRORCODES[400]}-COMANDO NO ENCONTRADO.")
    else:
        print(f"{ERRORCODES[200]}- El formato correcto es #COMMAND-(ARGUMENT);")
