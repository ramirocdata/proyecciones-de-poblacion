# Programa del curso: Proyecciones de Población

**Nivel:** posgrado (maestría / especialización)
**Duración:** 16 semanas · 3 horas semanales
**Herramienta principal:** Microsoft Excel (o LibreOffice Calc) · **Complementaria:** Python
**Docente:** Ramiro

---

## 1. Descripción

El curso introduce los fundamentos teóricos y los métodos aplicados para proyectar poblaciones a nivel nacional y subnacional. Se trabaja de lo simple a lo complejo: desde los modelos matemáticos de crecimiento hasta el método de componentes por cohortes y las proyecciones derivadas (hogares, población en edad escolar, poblaciones étnicas).

La apuesta pedagógica es que **cada cálculo sea visible**. Por eso la herramienta principal es Excel: cada columna es un paso del método, cada fórmula se puede inspeccionar y cada supuesto se puede modificar para ver su efecto. Python se introduce como complemento para mostrar cómo el mismo procedimiento se automatiza y escala.

## 2. Objetivos

Al finalizar el curso, la persona estudiante estará en capacidad de:

1. Distinguir entre proyección, pronóstico y prospectiva, y reconocer los supuestos que sostienen cada ejercicio.
2. Evaluar la calidad de la información por edad y sexo (censos, estadísticas vitales) y aplicar correcciones básicas.
3. Aplicar modelos matemáticos de crecimiento y juzgar su pertinencia según horizonte y escala.
4. Construir tablas de vida abreviadas y derivar relaciones de supervivencia.
5. Formular supuestos de fecundidad, mortalidad y migración a partir de evidencia.
6. Ejecutar una proyección por el método de componentes por cohortes, en Excel y en forma matricial (Leslie).
7. Producir proyecciones subnacionales y derivadas, y comunicar sus resultados y su incertidumbre.
8. Leer críticamente las proyecciones oficiales (DANE, CELADE, Naciones Unidas), incluidas sus implicaciones para poblaciones étnicas.

## 3. Metodología

Cada sesión combina:

- **Exposición conceptual** (≈ 45 min).
- **Taller en Excel** (≈ 90 min) con una plantilla de la carpeta `excel/`. Las celdas de entrada están en azul; las de fórmula, en negro. Se pide no pegar valores: el proceso debe quedar trazable.
- **Discusión de lectura** (≈ 30 min).
- **Extensión en Python** (opcional, fuera de clase) en la carpeta `python/`.

## 4. Contenido por sesiones

### Unidad 1. Fundamentos y datos

| Semana | Tema | Taller Excel |
|---|---|---|
| 1 | Qué es proyectar. Proyección, pronóstico y prospectiva. Ecuación compensadora. Fuentes en Colombia (CNPV 2018, EEVV, proyecciones DANE). | Ecuación compensadora con datos agregados |
| 2 | Estructura por edad y sexo. Pirámides, índices de masculinidad, dependencia y envejecimiento. | Pirámide e indicadores |
| 3 | Calidad de los datos. Índices de Whipple, Myers y Naciones Unidas. Suavizamiento por grupos de edad. | Evaluación de declaración de edad |

### Unidad 2. Métodos matemáticos

| Semana | Tema | Taller Excel |
|---|---|---|
| 4 | Crecimiento aritmético, geométrico y exponencial. Tiempo de duplicación. Interpolación y extrapolación. | `04_crecimiento.xlsx` |
| 5 | Curva logística y ajuste de tendencias. Límites de los métodos matemáticos. | Ajuste logístico |

### Unidad 3. Componentes demográficos

| Semana | Tema | Taller Excel |
|---|---|---|
| 6 | Mortalidad I: tasas específicas y tabla de vida abreviada. | `06_tabla_de_vida.xlsx` |
| 7 | Mortalidad II: relaciones de supervivencia. Supuestos de mortalidad futura. Introducción a Lee-Carter. | Relaciones de supervivencia |
| 8 | Fecundidad: tasas específicas, TGF, TBR, edad media. Supuestos de fecundidad futura. | Fecundidad y supuestos |
| 9 | Migración: saldos, tasas, patrón por edad (Rogers-Castro). Migración internacional reciente en Colombia. | Saldo migratorio por edad |
| 10 | **Taller integrador / evaluación parcial.** | — |

### Unidad 4. Método de componentes por cohortes

| Semana | Tema | Taller Excel |
|---|---|---|
| 11 | Proyección de población cerrada: supervivencia de cohortes, nacimientos, grupo abierto final. | `11_cohortes_componentes.xlsx` |
| 12 | Población abierta: incorporación de la migración. Escenarios (alto, medio, bajo). | Escenarios |
| 13 | Forma matricial: matriz de Leslie. Población estable. | Leslie con `MMULT` |

### Unidad 5. Aplicaciones

| Semana | Tema | Taller Excel |
|---|---|---|
| 14 | Proyecciones subnacionales: método de razones, participación y su consistencia con el total nacional. | Participación departamental |
| 15 | Proyecciones derivadas (hogares, edad escolar, fuerza de trabajo) y poblaciones étnicas. Incertidumbre y proyecciones probabilísticas (WPP). | Tasas de jefatura |
| 16 | **Presentación de proyectos finales.** | — |

## 5. Evaluación

| Componente | Peso |
|---|---|
| Talleres en Excel (mejores 8 de 10) | 35 % |
| Evaluación parcial (semana 10) | 20 % |
| Proyecto final: proyección de una unidad territorial o población específica | 35 % |
| Participación y discusión de lecturas | 10 % |

Ver `evaluacion/` para la guía y la rúbrica del proyecto final.

## 6. Bibliografía

Ver [`bibliografia.md`](bibliografia.md).
