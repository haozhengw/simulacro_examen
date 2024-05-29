import random

class JuegoAhorcado:
    ESTADOS = [
        r"""
         +--+
         |  |
            |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
            |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
         |  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|  |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
            |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        /   |
            |
        =====""",
        r"""
         +--+
         |  |
         O  |
        /|\ |
        / \ |
            |
        ====="""
    ]

    SALVADO = [
        r"""
         +--+
            |
            |
        \O/ |
         |  |
        / \ |
        ====="""
    ]

    CATEGORIA = 'FRUTAS'
    PALABRAS = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA'.split()

    def jugar(self):
        letras_incorrectas = []
        letras_correctas = []
        palabra_secreta = random.choice(self.PALABRAS)

        while True:
            self.dibujar(letras_incorrectas, letras_correctas, palabra_secreta)
            nueva_letra = self.dime_letra(letras_incorrectas + letras_correctas)

            if nueva_letra in palabra_secreta:
                letras_correctas.append(nueva_letra)
                if all(letra in letras_correctas for letra in palabra_secreta):
                    print(self.SALVADO[0])
                    print('¡Bien hecho! La palabra secreta es:', palabra_secreta)
                    print('¡Has ganado!')
                    break
            else:
                letras_incorrectas.append(nueva_letra)
                if len(letras_incorrectas) == len(self.ESTADOS) - 1:
                    self.dibujar(letras_incorrectas, letras_correctas, palabra_secreta)
                    print('¡Demasiados intentos!')
                    print('La palabra era "{}"'.format(palabra_secreta))
                    break

    def dibujar(self, letras_incorrectas, letras_correctas, palabra_secreta):
        print(self.ESTADOS[len(letras_incorrectas)])
        print('La categoría es:', self.CATEGORIA)
        print()

        print('Letras incorrectas:', ' '.join(letras_incorrectas) if letras_incorrectas else 'No hay letras incorrectas.')
        print()

        estado_palabra = ['_' if letra not in letras_correctas else letra for letra in palabra_secreta]
        print(' '.join(estado_palabra))

    def dime_letra(self, letras_adivinadas):
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in letras_adivinadas:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')
            else:
                return adivina

if __name__ == '__main__':
    juego = JuegoAhorcado()
    juego.jugar()
