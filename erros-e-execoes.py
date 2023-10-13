try:
    a = int(input("numerador:"))
    b = int(input("denominador:"))
    s = a / b

except ValueError:
    print("tivemos um problema :(")
except Exception as erro:
    print(f"o problema foi {erro.__class__}")
else:  # opcional
    print(s)
finally:  # opciona
    print("programa executado :)")