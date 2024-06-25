def division(a,b):
    if b != 0:
        return a/b
    else:
        print("como vas a dividir por zero, zapallo?")
        raise Exception("No corras mas, muchacha ojos de papel")

    print("ola k ase?")


if __name__ == "__main__":
    division(1,0)

