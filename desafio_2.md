# Desafío II

## Enunciado
Proponé una forma de expresar la información contenida en la estructura primaria de las proteínas usando tipos de datos de los lenguajes de programación que conocés.

## Respuesta
La estructura primaria (la secuencia lineal de aminoácidos) puede expresarse principalmente mediante:

1. **Cadena de texto (`string` / `str`):** Cada residuo de aminoácido se representa con su código de una sola letra (por ejemplo: `"MLPGLALLLLAAWTMRALEV"`). Es la forma más compacta, eficiente y estándar en bioinformática (como en el formato FASTA).
2. **Lista o arreglo (`list` / `array`):** Una lista ordenada de caracteres o cadenas con el código de 3 letras (por ejemplo: `["Met", "Leu", "Pro", "Gly", ...]`). Permite acceder a cada aminoácido mediante su índice de posición y almacenar modificaciones o propiedades por posición.
