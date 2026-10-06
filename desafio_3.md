# Desafío III

## Enunciado
¿En qué tipo de datos podrías expresar la información de la estructura terciaria proteica?

## Respuesta
Dado que la estructura terciaria corresponde a la conformación tridimensional (3D) de los átomos en el espacio, puede expresarse mediante:

1. **Lista o arreglo de tuplas/vectores de números flotantes (`list` / `array` de tuplas `(float, float, float)`):** Coordenadas espaciales $(x, y, z)$ de cada átomo o del carbono alfa ($C_\alpha$) de cada aminoácido. Por ejemplo: `[(12.35, 4.21, -8.10), (14.02, 5.80, -6.50), ...]`.
2. **Diccionarios u objetos / clases (`dict` / `class`):** Una estructura jerárquica donde cada átomo o residuo se asocia a su identificador, tipo de átomo, residuo y sus coordenadas 3D (similar al formato de un archivo PDB).
3. **Matriz numérica 2D (matriz de distancias / matriz de contactos):** Una matriz donde cada posición $(i, j)$ almacena la distancia euclídea (número decimal) entre el aminoácido $i$ y el aminoácido $j$, capturando el plegamiento espacial relativo.
