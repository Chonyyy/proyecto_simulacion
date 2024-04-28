# Introducción

En el mundo actual, la propagación de enfermedades se ha convertido en un desafío global que requiere una atención urgente. La importancia de detener esta propagación no solo radica en la protección de la salud de las personas, sino también en la preservación de la estabilidad social y económica de las comunidades. En este trabajo, exploraremos las diferentes estrategias y medidas que se pueden implementar para prevenir y controlar la propagación de enfermedades, destacando la necesidad de una acción coordinada a nivel local.

# Simulación

La simulación se centra en modelar la propagación de una enfermedad ficticia en un entorno simulado, utilizando una combinación de agentes, conocimiento interno y reglas de progresión de la enfermedad. Se tienen dos tipos de agentes, unos que representan a individuos dentro de la simulación, con características como ubicación, estado de salud y uso de mascarillas, y otro que representa una institución rectora en la ciudad. La simulación permite la interacción entre agentes y el entorno, modelando comportamientos complejos y dinámicos.

También cuenta con la implementación de medidas de salud pública, como el uso de mascarillas obligatorio en distintos lugares, implementación de cuarentenas, aislamientos o toques de queda, promoción de distanciamiento social, entre otros, a través de la interacción entre agentes y la actualización dinámica de su conocimiento interno.

## Arquitectura

La arquitectura InterRRaP (Interactive Rational Planning) se centra en la interacción entre agentes en un entorno simulado, proporcionando una estructura clara y modular para el desarrollo de sistemas de agentes autónomos y cooperativos. Esta arquitectura se compone de varias capas, cada una con responsabilidades específicas, que trabajan juntas para permitir a los agentes actuar de manera eficiente y dirigida hacia objetivos en un entorno dinámico:

- **Interfaz del Mundo**: Actúa como un intermediario entre los agentes y el entorno simulado, facilitando la interacción entre ellos. Esta interfaz no solo permite a los agentes percibir y actuar sobre su entorno, sino que también actualiza el estado del entorno en respuesta a las acciones de los agentes. A este componente se le corresponde un mapa mental que representa el conocimiento del terreno del agente, el cual se actualiza en cada paso del agente con las percepciones.

- **Componente de Comportamiento**: Gestiona el conocimiento reactivo del agente, procesa la información del entorno y toma decisiones sobre qué acciones específicas realiza el agente.

- **Componente de Planificación**: Se encarga de la planificación a corto plazo, tomando decisiones basadas en el conocimiento interno del agente y su percepción del entorno, los comportamientos rutinarios también se manejan en esta capa.

- **Componente Cooperativo**: Traza planes y objetivos cooperativos, facilita la cooperación entre agentes, permitiendo que los agentes interactúen entre sí, compartan información y tomen decisiones colectivas.

## Por qué usar InteRRaP

La arquitectura de agentes InteRRaP es particularmente ajustada para simulaciones de control de epidemias debido a varias razones fundamentales. La arquitectura de agentes permite representar a cada individuo humano de una población como una entidad distinta o agente, atribuyéndole rasgos y comportamientos específicos. Esto es crucial en la simulación de epidemias, ya que permite modelar la interacción entre individuos, la transmisión de enfermedades y la progresión de la enfermedad dentro de los agentes, proporcionando una representación detallada y granular de la dinámica de la epidemia. Permite implementar intervenciones y modificaciones de comportamientos de manera flexible y eficiente.

## Base de conocimiento

El conocimiento es uno de los principales aspectos de la arquitectura de agente. En la implementación se utiliza una base de conocimientos herárquica que contiene tres capas que corresponden a cada uno de los componentes mencionados anteriormente, lo que permite una representación formal y lógica del conocimiento del agente.

La base de conocimientos incluye información relevante sobre el estado de salud del agente, su ubicación, si usa mascarilla, y otros aspectos cruciales para la toma de decisiones del agente. Esta se actualiza dinámicamente a medida que el agente interactúa con el entorno y con otros agentes. Por ejemplo, si un agente se mueve a una nueva ubicación, nueva información previamente no accesible se incorpora a su base de conocimientos, permitiendo al agente actualizar su comprensión del entorno y tomar decisiones informadas.

## Agentes ciudadanos

Estos agentes representan a ciudadanos dentro de la simulación. Cada agente tiene características como su ubicación, estado de salud, y si usa mascarilla. Los agentes interactúan con el entorno y entre sí, tomando decisiones basadas en una combinación de su conocimiento interno y la percepción del entorno, lo que permite modelar comportamientos complejos y dinámicos. Estas pueden incluir moverse a diferentes ubicaciones, trabajar, usar o quitar mascarilla, entre otras acciones.

## Agente Institución

Este agente juega un papel crucial en la simulación, actuando como un punto focal para la coordinación y la toma de decisiones colectivas entre los agentes en el entorno simulado.

### Características y Propósito

Canelo es diseñado para actuar como un líder o coordinador dentro de la simulación. Su propósito principal es tomar decisiones basadas en la información colectiva de todos los agentes y transmitir estas decisiones a los demás agentes para guiar sus acciones. Esto incluye decisiones sobre la implementación de medidas de salud pública, como el uso de mascarillas, la cuarentena, y la adopción de prácticas de distanciamiento social.

### Funcionamiento

El funcionamiento de Canelo se basa en su capacidad para procesar y analizar la información colectiva de los agentes utilizando un *Sistema experto*. Canelo utiliza una Interfaz del Mundo personalizada para obtener información actualizada sobre el entorno y el estado de otros agentes. Con esta información, Canelo puede tomar decisiones informadas sobre las medidas que deben implementarse para controlar la propagación de la enfermedad.

### Comunicación y Coordinación

Una de las características clave de Canelo es su capacidad para comunicarse y coordinar con los otros agentes. Utiliza la **Capa de Cooperativa** para transmitir sus decisiones a los demás agentes, facilitando la coordinación de acciones para alcanzar objetivos comunes.

# Entorno

El Entorno es una representación abstracta del espacio en el que los agentes se mueven y interactúan. Este entorno simulado es esencial para modelar la dinámica de la enfermedad y las interacciones entre agentes en un contexto urbano. El entorno se modela utilizando un Grafo. Cada nodo representa una ubicación específica dentro del entorno simulado, como un hospital, un lugar público, un espacio de trabajo, una cuadra o una parada de autobús. Las aristas representan las conexiones entre estos nodos, indicando las rutas posibles que los agentes pueden tomar para moverse entre diferentes ubicaciones. A cada nodo también se le calcula una probabilidad de contacto base que depende de la capacidad del nodo y la cantidad de agentes que hayan en este.

# Modelado de la Progresión del Virus

En la simulación, la epidemia es modelada utilizando un agente reactivo que tiene en su base de conocimientos implementada en Prolog, las reglas e información necesaria acerca del progreso de la enfermedad en un ciudadano.

## Cómo se propaga la enfermedad

En cada iteración de la simulación se calculan los contactos (cuando decimos contacto, nos referimos solamente a aquellos que propagan la enfermedad) que tienen agentes que se encuentran en un mismo lugar (nodo). Cada nodo tiene una probabilidad de contacto base y usar distintas medidas higiénicas puede reducir esta probabilidad de contacto. Si un agente tiene contacto con otro infectado, la enfermedad se propaga con una probabilidad.

## Progresión de la Enfermedad

La progresión de la enfermedad describe cómo un agente infectado puede pasar de una etapa de infección a otra, desde asintomático hasta terminal. Este proceso se modela a través de una serie de reglas que describen las condiciones bajo las cuales un agente puede progresar de una etapa a otra.

### Factores de Riesgo

Existen varios factores que pueden aumentar el riesgo de infección y de progresión de la enfermedad, como pudiera ser la edad del ciudadano o la densidad poblacional de un nodo, la cantidad de agentes en este de acuerdo a la capacidad. La capacidad de un nodo no determina el máximo de agentes que pueden estar en este, pero a partir de este punto se tiene la máxima probabilidad de contacto.

# IA

## Búsqueda

El uso del algoritmo A* para hallar el camino más corto entre dos puntos es una elección estratégica en este contexto, especialmente cuando se busca minimizar la exposición de los agentes a enfermedades infecciosas. Aquí se argumenta más a favor de esta estrategia:

1. **Eficiencia y Precisión**: A* es conocido por su eficiencia y precisión en la búsqueda de caminos más cortos. Utiliza una función heurística para guiar la búsqueda, lo que permite que el algoritmo se ejecute más rápido que otros métodos como Dijkstra, sin comprometer la precisión en la búsqueda del camino más corto. Esta eficiencia es crucial en entornos donde se requiere una respuesta rápida, como en la movilidad de agentes en la epidemia.

2. **Adaptabilidad a Entornos Complejos**: A* puede adaptarse a entornos complejos, como nodos infectados o con muchos agentes, donde la topología del espacio y las restricciones de movimiento pueden ser significativas. Esto es especialmente relevante en el contexto de la simulación de control de epidemias, donde los agentes deben navegar por entornos que pueden incluir áreas de alto riesgo de infección.

3. **Minimización de la Exposición a Enfermedades**: Aunque A* se utiliza principalmente para encontrar el camino más corto, su eficiencia y precisión pueden ser adaptadas para minimizar la exposición a enfermedades infecciosas. Por ejemplo, se pueden modificar los parámetros del algoritmo para priorizar caminos que minimicen la exposición a áreas de alto riesgo de infección, como las salas de pacientes infectados. Esto se logra ajustando la función heurística para que tenga en cuenta no solo la distancia al objetivo sino también la probabilidad de exposición a la enfermedad en diferentes partes del entorno.

4. **Flexibilidad para Adaptarse a Cambios**: A* es un algoritmo flexible que puede adaptarse a cambios en el entorno o en las condiciones de la epidemia. Por ejemplo, si la propagación de la enfermedad cambia o si se implementan nuevas estrategias de control, el algoritmo puede ser reajustado para reflejar estos cambios.

## Interfaz de Usuario y Procesamiento del Lenguaje Natural

Para mejorar la interacción con la simulación, desarrollamos una interfaz de usuario que permite a estos interactuar con la simulación mediante comandos de lenguaje natural. Utilizamos técnicas de procesamiento del lenguaje natural (NLP) para interpretar los comandos del usuario y mapearlos a acciones en la simulación.

### Sistema Experto

Se implementa un sistema experto utilizando Prolog para guiar las decisiones del agente institucional (Canelo) en la implementación de medidas para contener la enfermedad. El sistema experto se basa en reglas lógicas que reflejan las recomendaciones de salud pública y epidemiología.

### Funcionamiento

El sistema experto se basa en una serie de reglas que establecen condiciones y acciones a seguir. Por ejemplo, una regla podría ser:

'''
si la tasa de infección es alta y la capacidad hospitalaria es baja, entonces se debe implementar una cuarentena.
'''

El sistema experto evalúa estas reglas con respecto al estado actual de la simulación y las decisiones previas tomadas, generando recomendaciones para el agente institucional. Para realizar este sistema experto utilizamos el algoritmo genético sobre una serie de parámetros que este agente utiliza para tomar desiciones.

El algoritmo genético PyGAD es una biblioteca de Python diseñada para optimizar una amplia gama de problemas mediante técnicas de algoritmos genéticos. A continuación, se presenta un resumen técnico de cómo funciona PyGAD y por qué sería el mejor para una simulación de control de epidemias donde la función de fitness se enfoca en minimizar la cantidad de agentes infectados.

### Cómo funciona PyGAD

1. **Definición de la función de fitness**: PyGAD requiere que se defina una función de fitness que evalúe la calidad de una solución dada. En el contexto de esta simulación, esta función de fitness calcula la cantidad de agentes infectados en una simulación dada, y el objetivo es minimizar este número.

2. **Inicialización de la población**: PyGAD genera una población inicial de soluciones (agentes) con valores aleatorios dentro de un rango definido. Cada solución representa un conjunto de parámetros o estrategias que podrían ser utilizadas en la simulación de control de epidemias.

3. **Selección de padres**: A partir de la población inicial, PyGAD selecciona soluciones para la reproducción basándose en su fitness. Las soluciones con mejor fitness tienen más probabilidades de ser seleccionadas.

4. **Crossover y mutación**: Las soluciones seleccionadas se cruzan para generar nuevas soluciones, combinando partes de las soluciones padres. Luego, se aplica una mutación a estas nuevas soluciones para introducir variaciones y explorar nuevas áreas del espacio de soluciones.

5. **Evaluación de la nueva población**: Las nuevas soluciones se evalúan utilizando la función de fitness definida, y se seleccionan las mejores soluciones para formar la nueva población.

6. **Repetición**: Este proceso de selección, crossover, mutación y evaluación se repite durante un número definido de generaciones, permitiendo que la población evolucione hacia soluciones de mayor fitness.

### Por qué PyGAD es el mejor para una simulación de control de epidemias

- **Flexibilidad**: PyGAD es altamente flexible y puede ser utilizado para optimizar una amplia gama de problemas, lo que lo hace adecuado para simulaciones de control de epidemias que pueden requerir la optimización de múltiples parámetros o estrategias.

- **Capacidad para manejar complejidad**: La capacidad de PyGAD para explorar el espacio de soluciones mediante la mutación y el crossover permite manejar la complejidad inherente a los sistemas de control de epidemias, donde la interacción entre múltiples factores puede afectar la propagación de la enfermedad.

- **Adaptabilidad**: PyGAD puede adaptarse a cambios en el entorno de la epidemia o en las políticas de control mediante la reevaluación de la función de fitness y la evolución de la población hacia soluciones más efectivas.

- **Eficiencia**: A través de la selección de padres basada en la fitness, PyGAD puede converger rápidamente hacia soluciones óptimas, lo que es crucial en el contexto de una epidemia donde el tiempo es un factor crítico.

## Resultados Experimentales

### Para 20 agentes en un rango de 10 dias estos fueron los resultados

| Día | Susceptible | Asintomático | Sintomático | Crítico | Terminal | Muerto | Recuperado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 12 | 7 | 0 | 0 | 0 | 0 | 1 |
| 1 | 1 | 0 | 2 | 1 | 0 | 3 | 13 |
| 2 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 3 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 4 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 5 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 6 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 7 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 8 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 9 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |
| 10 | 1 | 0 | 0 | 0 | 0 | 4 | 15 |

### Para 50 agentes en un rango de 10 dias estos fueron los resultados

| Día | Susceptible | Asintomático | Sintomático | Crítico | Terminal | Muerto | Recuperado |
|-----|-------------|--------------|-------------|---------|----------|-------|------------|
| 0   | 35          | 4            | 1           | 0       | 0        | 0     | 10         |
| 1   | 19          | 1            | 3           | 1       | 1        | 1     | 24         |
| 2   | 13          | 0            | 1           | 0       | 1        | 4     | 31         |
| 3   | 12          | 0            | 1           | 0       | 0        | 5     | 32         |
| 4   | 8           | 0            | 1           | 2       | 0        | 5     | 34         |
| 5   | 8           | 0            | 0           | 1       | 0        | 6     | 35         |
| 6   | 8           | 0            | 0           | 0       | 0        | 7     | 35         |
| 7   | 8           | 0            | 0           | 0       | 0        | 7     | 35         |
| 8   | 8           | 0            | 0           | 0       | 0        | 7     | 35         |
| 9   | 8           | 0            | 0           | 0       | 0        | 7     | 35         |
| 10 | 8           | 0            | 0           | 0       | 0        | 7     | 35         |

### Para 100 agentes en un rango de 15 dias estos fueron los resultados

| Día | Susceptible | Asintomático | Sintomático | Crítico | Terminal | Muerto | Recuperado |
|-----|-------------|--------------|-------------|---------|----------|-------|------------|
| 0   | 87          | 8            | 2           | 0       | 0        | 0     | 3          |
| 1   | 10          | 1            | 4           | 0       | 2        | 1     | 82         |
| 2   | 4           | 0            | 2           | 3       | 1        | 5     | 85         |
| 3   | 2           | 0            | 1           | 1       | 0        | 8     | 88         |
| 4   | 2           | 0            | 0           | 1       | 0        | 9     | 88         |
| 5   | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 6   | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 7   | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 8   | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 9   | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 10 | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 11 | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 12 | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 13 | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 14 | 2           | 0            | 0           | 0       | 0        | 10    | 88         |
| 15 | 2           | 0            | 0           | 0       | 0        | 10    | 88         |

### Para 150 agentes en un rango de 15 dias estos fueron los resultados

| Día | Susceptible | Asintomático | Sintomático | Crítico | Terminal | Muerto | Recuperado |
|-----|-------------|--------------|-------------|---------|----------|-------|------------|
| 0   | 108         | 15           | 0           | 0       | 0        | 0     | 27         |
| 1   | 0           | 4            | 7           | 4       | 2        | 4     | 129        |
| 2   | 0           | 0            | 1           | 3       | 1        | 12    | 133        |
| 3   | 0           | 0            | 0           | 2       | 1        | 13    | 134        |
| 4   | 0           | 0            | 2           | 1       | 0        | 13    | 134        |
| 5   | 0           | 0            | 1           | 1       | 0        | 13    | 135        |
| 6   | 0           | 0            | 0           | 1       | 0        | 14    | 135        |
| 7   | 0           | 0            | 0           | 1       | 0        | 14    | 135        |
| 8   | 0           | 0            | 0           | 0       | 0        | 14    | 136        |
| 9   | 0           | 0            | 0           | 0       | 0        | 14    | 136        |
| 10 | 0           | 0            | 0           | 0       | 0        | 14    | 136        |
| 11 | 0           | 0            | 0           | 0       | 0        | 14    | 136        |
| 12 | 0           | 0            | 0           | 0       | 0        | 14    | 136        |
| 13 | 0           | 0            | 0           | 0       | 0        | 14    | 136        |
| 14 | 0           | 0            | 0           | 0       | 0        | 14    | 136        |

### Para 200 agentes en un rango de 15 dias estos fueron los resultados

| Día | Susceptible | Asintomático | Sintomático | Crítico | Terminal | Muerto | Recuperado |
|-----|-------------|--------------|-------------|---------|----------|-------|------------|
| 0   | 156         | 29           | 4           | 0       | 0        | 0     | 11         |
| 1   | 0           | 2            | 11          | 3       | 2        | 11    | 171        |
| 2   | 0           | 1            | 3           | 2       | 0        | 17    | 177        |
| 3   | 0           | 1            | 3           | 0       | 1        | 17    | 178        |
| 4   | 0           | 0            | 0           | 2       | 0        | 18    | 180        |
| 5   | 0           | 0            | 0           | 1       | 1        | 18    | 180        |
| 6   | 0           | 0            | 1           | 0       | 0        | 19    | 180        |
| 7   | 0           | 0            | 1           | 0       | 0        | 19    | 180        |
| 8   | 0           | 0            | 0           | 1       | 0        | 19    | 180        |
| 9   | 0           | 0            | 0           | 1       | 0        | 19    | 180        |
| 10 | 0           | 0            | 0           | 0       | 0        | 20    | 180        |
| 11 | 0           | 0            | 0           | 0       | 0        | 20    | 180        |
| 12 | 0           | 0            | 0           | 0       | 0        | 20    | 180        |
| 13 | 0           | 0            | 0           | 0       | 0        | 20    | 180        |
| 14 | 0           | 0            | 0           | 0       | 0        | 20    | 180        |

### Para 250 agentes en un rango de 15 dias estos fueron los resultados

| Día | Susceptible | Asintomático | Sintomático | Crítico | Terminal | Muerto | Recuperado |
|-----|-------------|--------------|-------------|---------|----------|-------|------------|
| 0   | 221         | 10           | 3           | 0       | 0        | 0     | 16         |
| 1   | 0           | 0            | 9           | 1       | 0        | 13    | 227        |
| 2   | 0           | 0            | 5           | 2       | 0        | 14    | 229        |
| 3   | 0           | 0            | 0           | 1       | 1        | 15    | 233        |
| 4   | 0           | 0            | 0           | 2       | 0        | 15    | 233        |
| 5   | 0           | 0            | 0           | 1       | 0        | 16    | 233        |
| 6   | 0           | 0            | 1           | 0       | 0        | 16    | 233        |
| 7   | 0           | 0            | 0           | 0       | 0        | 16    | 234        |
| 8   | 0           | 0            | 0           | 0       | 0        | 16    | 234        |
| 9   | 0           | 0            | 0           | 0       | 0        | 16    | 234        |
| 10 | 0           | 0            | 0           | 0       | 0        | 16    | 234        |
| 11 | 0           | 0            | 0           | 0       | 0        | 16    | 234        |
| 12 | 0           | 0            | 0           | 0       | 0        | 16    | 234        |
| 13 | 0           | 0            | 0           | 0       | 0        | 16    | 234        |
| 14 | 0           | 0            | 0           | 0       | 0        | 16    | 234        |

Los resultados experimentales presentados en la simulación muestran una serie de patrones y tendencias que son relevantes para entender la dinámica de la propagación de enfermedades en diferentes contextos y poblaciones. A continuación, se ofrece una opinión basada en la interpretación de estos datos:

1. **Escalabilidad y Efectividad de las Intervenciones**: A medida que el número de agentes aumenta, se observa una tendencia general hacia una mayor efectividad de las intervenciones en la reducción de la propagación de la enfermedad. Esto sugiere que las estrategias de control de epidemias pueden ser más efectivas en poblaciones más grandes, lo cual es crucial para la gestión de brotes de enfermedades en contextos reales.

2. **Impacto de la Inicialización de la Enfermedad**: Los resultados muestran que el número inicial de agentes infectados (sintomáticos o asintomáticos) tiene un impacto significativo en la evolución de la epidemia. En los casos con menos agentes (20 y 50), el impacto inicial es más pronunciado, mientras que en los casos con más agentes (100, 150, 200, 250), la epidemia parece alcanzar un estado estacionario más rápidamente, posiblemente debido a la mayor capacidad de la población para difundir la enfermedad.

3. **Duración de la Epidemia**: La duración de la epidemia parece estar influenciada por el número de agentes y la efectividad de las intervenciones. Esta epidemia en particular tiene una duracion de pocos dias por su letalidad, la epidemia alcanza un estado estacionario rápidamente.

4. **Recuperación y Mortalidad**: A medida que el número de agentes aumenta, la proporción de agentes recuperados y la tasa de mortalidad parecen disminuir. Esto podría indicar que las intervenciones son más efectivas en poblaciones más grandes, permitiendo una recuperación más rápida y una menor tasa de mortalidad.

# Conclusiones

k

# Recomendaciones y futuros cambios

Se recomienda realizar un estudio más profundo de Prolog para comprender mejor el funcionamiento de este lenguaje de programación. Originalmente, se utilizó Prolog para la base de conocimientos de los agentes, sin embargo, debido a su limitada capacidad de memoria, se optó por una base de conocimientos implementada en Python. A pesar de esto, se decidió mantener Prolog para la simulación de la propagación de la epidemia. Sin embargo, es importante tener en cuenta que existen limitaciones en cuanto a la cantidad de agentes que pueden ser manejados, ya que no se puede superar el límite de 300 agentes.

# Bibliografía

[1] https://towardsdatascience.com/introducing-geneal-a-genetic-algorithm-python-library-db69abfc212c  
[2] https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009149  
[3] https://github.com/diogomatoschaves/geneal  
[4] https://jmvidal.cse.sc.edu/library/muller93a.pdf  