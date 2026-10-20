# Extensiones en Python (opcionales)

Cada script reproduce una plantilla de `excel/` para mostrar cómo se automatiza el mismo procedimiento. La regla del curso es: **primero se entiende en Excel, luego se automatiza en Python**. Los resultados deben coincidir con los de la plantilla.

| Script | Plantilla equivalente | Sesión |
|---|---|---|
| `cohortes_componentes.py` | `excel/11_cohortes_componentes.xlsx` | 11 |

## Requisitos

```bash
pip install pandas
```

## Ejecución

Desde la raíz del repositorio:

```bash
python python/cohortes_componentes.py
```

Lee `datos/ficticio_base.csv` (los mismos datos ficticios de la plantilla) e imprime la TGF, los nacimientos por periodo y la población proyectada 2020–2040.

## Por agregar

- `crecimiento.py` (sesión 4)
- `tabla_de_vida.py` (sesión 6)
- `leslie.py` con numpy (sesión 13)
