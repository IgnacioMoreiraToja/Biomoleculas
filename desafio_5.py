"""
Desafío V: Predicción básica de estructura secundaria a partir de la secuencia de aminoácidos.
- H: Hélice alfa (Alpha helix)
- B: Hoja beta plegada (Beta sheet)
- L: Bucle o loop (Coil/Loop)
"""

# Diccionario con las tendencias conformacionales de los 20 aminoácidos estándar:
PREFERENCIAS_ESTRUCTURA = {
    # Propensión a formar hélice alfa (H)
    'A': 'H', 'E': 'H', 'L': 'H', 'M': 'H', 'Q': 'H', 'K': 'H', 'R': 'H', 'H': 'H',
    # Propensión a formar hoja beta plegada (B)
    'V': 'B', 'I': 'B', 'Y': 'B', 'C': 'B', 'W': 'B', 'F': 'B', 'T': 'B',
    # Propensión a formar bucles o giros (L)
    'G': 'L', 'P': 'L', 'S': 'L', 'D': 'L', 'N': 'L'
}

def predecir_estructura_secundaria(secuencia: str) -> str:
    """
    Recibe una secuencia de aminoácidos (código de una letra) y predice
    la estructura secundaria de cada residuo devolviendo una cadena
    con 'H', 'B' o 'L' en cada posición.
    """
    secuencia_limpia = secuencia.strip().upper()
    prediccion = [PREFERENCIAS_ESTRUCTURA.get(aa, 'L') for aa in secuencia_limpia]
    return "".join(prediccion)

if __name__ == "__main__":
    # Secuencia de prueba
    secuencia_ejemplo = "MLPGLALLLLAAWTMRALEVPTDGNAPLLVEPQIAMFCGRLN"
    resultado = predecir_estructura_secundaria(secuencia_ejemplo)

    print("Secuencia de aminoácidos:")
    print(secuencia_ejemplo)
    print("\nPredicción de estructura secundaria (H: Hélice, B: Hoja Beta, L: Loop):")
    print(resultado)
