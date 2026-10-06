"""
Desafío VIII: Representación de Sequence Logo a partir de una lista de secuencias alineadas usando logomaker.
"""

import logomaker
import matplotlib.pyplot as plt

# Lista de secuencias provistas en el desafío
secuencias = [
    "MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRAQCKTHPHFVIPYRCLVGEFVSDALLAPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV",
    "MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVGEFVSDALLVPDKCKFLHQERMDVCETHLHWHTV"
]

def generar_logo(lista_secuencias: list[str], output_imagen: str = "logo_secuencias.png"):
    """
    Genera y guarda una representación Sequence Logo a partir de secuencias alineadas.
    """
    # 1. Crear matriz de frecuencias / información a partir del alineamiento
    matriz_logo = logomaker.alignment_to_matrix(lista_secuencias)

    # 2. Configurar la figura (ancho adecuado para la longitud de las secuencias)
    fig, ax = plt.subplots(figsize=(22, 4))

    # 3. Dibujar el Sequence Logo
    logo = logomaker.Logo(matriz_logo, ax=ax)

    # 4. Estilos y etiquetas
    ax.set_title("Sequence Logo - Desafío VIII", fontsize=14, pad=10)
    ax.set_xlabel("Posición del aminoácido", fontsize=12)
    ax.set_ylabel("Información (bits)", fontsize=12)

    # 5. Guardar la imagen
    plt.tight_layout()
    plt.savefig(output_imagen, dpi=300)
    print(f"Logo guardado exitosamente en '{output_imagen}'.")

    # Mostrar la figura (opcional, en entornos interactivos)
    plt.show()

if __name__ == "__main__":
    generar_logo(secuencias)
