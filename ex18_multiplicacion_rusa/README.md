
# Ejercicio 18 — Multiplicación rusa (GitHub Classroom + IA)

## Contexto (por qué importa)
Algoritmo histórico que combina duplicación y bisección, útil para razonar sobre invariantes.

## Enunciado del problema
Lee dos enteros **no negativos** `a` y `b`.
- Si `b` inicia en 0, imprime `0` (sin pasos).
- Si no, imprime cada paso `a b` por línea (empezando en los valores iniciales) hasta que `b` sea 1.  
- El **resultado** es la suma de `a` en las filas donde `b` fue **impar**. Imprímelo en una **última línea**.

---

## Repositorio y archivos

```
.
├── src/
│   └── exercise.py        # escribe tu solución aquí
├── tests/
│   └── test_exercise.py   # pruebas del autograder
└── README.md              # este documento
```

El archivo `src/exercise.py` contiene el siguiente esqueleto:

```python
def main():
    # escribe tu código abajo de esta línea
    ...

if __name__ == '__main__':
    main()
```

Coloca **todo tu código** dentro de `main()` (debajo del comentario).

---

## Requisitos técnicos (lo que evalúa el autograder)

1. Respeta el contrato de **entrada/salida** (sin mensajes extra).  
2. Usa al menos un **ciclo** (`for` o `while`) si el problema lo requiere.  
3. No imprimas texto adicional, ni espacios en blanco al final de línea.  

> El autograder evalúa únicamente el comportamiento observable (I/O).  
> La rúbrica humana también valora tu **proceso** y **claridad algorítmica**.

---

## Guía de trabajo (pensamiento computacional primero)

Antes de escribir código, completa estas micro‑tareas en tu archivo `exercise.py` como comentarios **encima de tu solución**:

1) **IPO rápido (Entrada–Proceso–Salida):**  
   - **Entrada:**  
   - **Proceso (algoritmo, 2–4 pasos):**  
   - **Salida:**  

2) **Invariante del ciclo (1 oración):**  
   Explica qué propiedad se mantiene verdadera en cada iteración (por ejemplo: “al iniciar cada iteración con `i`, ya procesé hasta `i-1`”).

> Estos comentarios son **obligatorios** y serán revisados por el/la profesor(a).

---

## Uso responsable de IA (ChatGPT / Copilot)

Se permite usar IA como apoyo, **pero debes evidenciar tu aporte**. En la parte superior de `exercise.py`, pega como comentarios:

- **Prompt(s) que usaste** (máx. 3 líneas).  
- **Qué aceptaste o modificaste** de la sugerencia (2–4 líneas).  
- **Verificación manual**: explica cómo probaste tu programa sin IA (1–2 líneas).

Ejemplo:
```python
# PROMPT: "Explícame el algoritmo X con while y cómo leer las entradas sin imprimir textos extra."
# CAMBIOS: Ajusté la lectura con int(input()) y quité prints de depuración.
# VERIFICACIÓN: Probé casos pequeños y límites.
```

> No se califica si usas o no IA, sino tu **criterio** y **proceso**.

---

## Pruebas locales

Ejecuta en tu terminal, desde la raíz del repo:

```bash
python -m pytest --tb=short -v
```

Asegúrate de pasar **todas** las pruebas antes de hacer *commit*.

---

## Entrega (Git workflow)

1. Verifica que tu programa pasa `pytest`.  
2. *Commit* con un mensaje significativo (ej. `feat: implementa algoritmo iterativo`).  
3. *Push* a tu repositorio de GitHub Classroom.

---

## Rúbrica (humana) — 10 pts

| Criterio | Descripción | Pts |
|---|---|---:|
| **Correctitud I/O** | Cumple con el formato y pasa el autograder. | 4 |
| **Claridad algorítmica** | IPO y algoritmo en 2–4 pasos claros y consistentes. | 2 |
| **Razonamiento sobre ciclos** | Invariante del ciclo pertinente. | 2 |
| **Uso responsable de IA** | Prompts + cambios + verificación claros. | 2 |

---

## Reflexión corta (como comentarios al final de `exercise.py`)

Responde en 3–5 líneas cada una:

1. ¿Qué parte del problema te pareció más “mecánica” y cuál más de razonamiento?  
2. Si usaste IA, ¿qué limitación detectaste y cómo la solucionaste?  
3. ¿Cómo validarías este programa en un sistema mayor?

---

<details>
<summary><strong>Notas para el profesorado</strong> (ocultar para estudiantes)</summary>

- Este README busca priorizar **pensamiento computacional** y evidencia de proceso.  
- Los comentarios obligatorios (IPO, invariante, prompts) ayudan a mitigar la “resolución pasiva con IA”.  
- Se sugiere revisar aleatoriamente repos para corroborar calidad de prompts y congruencia con el código.  
</details>
