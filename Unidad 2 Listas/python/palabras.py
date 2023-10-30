# Función para invertir las palabras en una frase
def invertir_frase(frase):
    palabras = frase.split()  # Dividir la frase en palabras
    palabras_invertidas = palabras[::-1]  # Invertir la lista de palabras
    frase_invertida = " ".join(palabras_invertidas)  # Unir las palabras invertidas en una sola frase
    return frase_invertida

# Función principal
def main():
    frase = input("Ingrese una frase: ")
    frase_invertida = invertir_frase(frase)
    print("Frase invertida:", frase_invertida)

if __name__ == "__main__":
    main()
