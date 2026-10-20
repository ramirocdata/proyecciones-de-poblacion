# Proyecciones de Población

Materiales del curso de posgrado **Proyecciones de Población**: programa, guías por sesión, plantillas de Excel con el procedimiento paso a paso y extensiones opcionales en Python.

## Enfoque

Cada método se trabaja primero en **Excel**, de modo que el proceso de cálculo quede visible columna por columna. Python aparece después como forma de automatizar y escalar el mismo procedimiento.

Convención de colores en las plantillas:

| Color | Significado |
|---|---|
| Texto azul / fondo amarillo claro | Dato de entrada o supuesto (se puede cambiar) |
| Texto negro | Fórmula (no sobrescribir) |
| Fondo verde claro | Resultado clave |

## Estructura

```
proyecciones-poblacion/
├── README.md              ← este archivo
├── programa.md            ← programa completo (16 semanas)
├── bibliografia.md
├── sesiones/              ← una carpeta por semana con objetivos, taller y lectura
│   ├── 01-introduccion/
│   ├── ...
│   └── 16-proyectos-finales/
├── excel/                 ← plantillas de trabajo
│   ├── 04_crecimiento.xlsx
│   ├── 06_tabla_de_vida.xlsx
│   └── 11_cohortes_componentes.xlsx
├── python/                ← extensiones opcionales
├── datos/                 ← fuentes y guía de descarga
└── evaluacion/            ← guía y rúbrica del proyecto final
```

## Cómo usar este repositorio

**Estudiantes:** descarguen el repositorio (botón verde *Code → Download ZIP*) o clónenlo. Abran la plantilla de la sesión, guarden una copia con su nombre y trabajen sobre ella.

**Datos:** las plantillas traen una **población ficticia** con fines didácticos. En los talleres se reemplaza por datos del DANE (ver `datos/README.md`).

## Licencia

Contenidos bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es); código bajo licencia MIT. Ver `LICENSE.md`.
