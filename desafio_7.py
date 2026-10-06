"""
Desafío VII: Búsqueda del motivo de N-glicosilación (N{P}[ST]{P}) en UniProt.
Problema basado en Rosalind (Finding a Protein Motif).

Motivo: N{P}[ST]{P}
- N: Asparagina
- {P}: Cualquier aminoácido excepto Prolina
- [ST]: Serina o Treonina
- {P}: Cualquier aminoácido excepto Prolina
"""

import re
import requests

# Expresión regular con lookahead para detectar solapamientos
MOTIVO_N_GLICOSILACION = re.compile(r'(?=(N[^P][ST][^P]))')


def obtener_secuencia_uniprot(uniprot_id: str) -> str:
    """
    Descarga la secuencia de una proteína en formato FASTA desde UniProt.
    Maneja identificadores como 'B5ZC00' o 'P07204_TRPI_RAT'.
    """
    # Si contiene guión bajo, el accession id para la URL es la primera parte
    accession_id = uniprot_id.split('_')[0]
    url = f"https://rest.uniprot.org/uniprotkb/{accession_id}.fasta"
    
    response = requests.get(url)
    if response.status_code != 200:
        # Fallback a URL alternativa
        url_alt = f"http://www.uniprot.org/uniprot/{accession_id}.fasta"
        response = requests.get(url_alt)

    if response.status_code == 200:
        lineas = response.text.strip().splitlines()
        # Omitir la línea del encabezado FASTA (>sp|...)
        secuencia = "".join(lineas[1:])
        return secuencia
    return ""


def buscar_motivo_nglicosilacion(ids_proteinas: list[str]) -> dict[str, list[int]]:
    """
    Busca las posiciones (1-indexadas) del motivo de N-glicosilación
    para cada identificador de proteína provisto.
    """
    resultados = {}
    for pid in ids_proteinas:
        pid = pid.strip()
        if not pid:
            continue
        secuencia = obtener_secuencia_uniprot(pid)
        if secuencia:
            # Buscar ocurrencias del motivo (posiciones 1-indexadas)
            posiciones = [m.start() + 1 for m in MOTIVO_N_GLICOSILACION.finditer(secuencia)]
            if posiciones:
                resultados[pid] = posiciones
    return resultados


if __name__ == "__main__":
    # Lista de identificadores de ejemplo (máximo 15 según el enunciado)
    identificadores_ejemplo = [
        "A2Z669",
        "B5ZC00",
        "P07204_TRPI_RAT",
        "P20840_SAG1_YEAST"
    ]

    print("Buscando motivo de N-glicosilación en proteínas de UniProt...\n")
    hallazgos = buscar_motivo_nglicosilacion(identificadores_ejemplo)

    for pid, posiciones in hallazgos.items():
        print(pid)
        print(" ".join(map(str, posiciones)))
