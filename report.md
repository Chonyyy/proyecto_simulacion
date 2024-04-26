# Simulación de epidemias

autores:
> - María de Lourdes Choy C411
> - Alejandro Yero Valdes C411

# Introducción

En el mundo actual, la propagación de enfermedades se ha convertido en un desafío global que requiere una atención urgente. La importancia de detener esta propagación no solo radica en la protección de la salud de las personas, sino también en la preservación de la estabilidad social y económica de las comunidades. En este trabajo, exploraremos las diferentes estrategias y medidas que se pueden implementar para prevenir y controlar la propagación de enfermedades, destacando la necesidad de una acción coordinada a nivel local.

# Simulación

Nuestra simulación se centra en modelar la propagación de una enfermedad ficticia en un entorno simulado, utilizando una combinación de agentes, conocimiento interno, y reglas de progresión de la enfermedad. Tenemos dos tipos de agentes, unos que representan a individuos dentro de la simulacion, con características como ubicación, estado de salud, y uso de mascarillas, y otro que representa una intitución rectora en la ciudad. La simulación permite la interacción entre agentes y el entorno, modelando comportamientos complejos y dinámicos. 

También cuenta con la implementación de medidas de salud pública, como pudiesen ser el uso de mascarillas obligatorio en distintos lugares, implementación de cuarentenas, aislamientos o toques de queda, promoción de distanciamoento social, entre otros, a través de la interacción entre agentes y la actualización dinámica de su conocimiento interno.

## Arquitectura

La arquitectura InterRRaP (Interactive Rational Planning) se centra en la interacción entre agentes en un entorno simulado, proporcionando una estructura clara y modular para el desarrollo de sistemas de agentes autónomos y cooperativos. Esta arquitectura se compone de varias capas, cada una con responsabilidades específicas, que trabajan juntas para permitir a los agentes actuar de manera eficiente y dirigida hacia objetivos en un entorno dinámico:

- **Interfaz del Mundo**: Actúa como un intermediario entre los agentes y el entorno simulado, facilitando la interacción entre ellos. Esta interfaz no solo permite a los agentes percibir y actuar sobre su entorno, sino que también actualiza el estado del entorno en respuesta a las acciones de los agentes. A este componente se le corresponde un mapa mental que representa el conocimiento del terreno del agente, el cual se actualiza en cada paso del agente con las percepciones.

- **Componente de Comportamiento**: Gestiona el conocimiento reactivo del agente, procesa la información del entorno y toma desiciones sobre que acciones específicas realiza el agente.  

- **Componente de Planificación**: Se encarga de la planificación a corto plazo, tomando decisiones basadas en el conocimiento interno del agente y su percepción del entorno, los comportamientos rutinarios tambien se manejan en esta capa.  

- **Componente Cooperativo**: Traza planes y objetivos cooperativos, facilita la cooperación entre agentes, permitiendo que los agentes interactúen entre sí, compartan información y tomen decisiones colectivas.  

## Base de conocimiento

El conocimiento es uno de los principales aspectos de nuestra arquitecura de agente. En nuestra implementación utilizamos Prolog para crear una base de conocimientos herárquica que contiene tres capas que corresponden a cada uno de los componentes mencionados anteriormente, lo que permite una representación formal y lógica del conocimiento del agente.

La base de conocimientos incluye información relevante sobre el estado de salud del agente, su ubicación, si usa mascarilla, y otros aspectos cruciales para la toma de decisiones del agente. Esta se actualiza dinámicamente a medida que el agente interactúa con el entorno y con otros agentes. Por ejemplo, si un agente se mueve a una nueva ubicación nueva información previamente no accesible se incorpora a su base de conocimientos, permitiendo al agente actualizar su comprensión del entorno y tomar decisiones informadas.

## Agentes ciudadanos

Estos agentes representan a ciudadanos dentro de la simulación. Cada agente tiene características como su ubicación, estado de salud, y si usa mascarilla. Los agentes interactúan con el entorno y entre sí, tomando desiciones basadas en una combinación de su conocimiento interno y la percepción del entorno, lo que permite modelar comportamientos complejos y dinámicos. Estas pueden incluir moverse a diferentes ubicaciones, trabajar, usar o quitar mascarilla, entre otras acciones.

## Agente Institución

Este agente juega un papel crucial en la simulación, actuando como un punto focal para la coordinación y la toma de decisiones colectivas entre los agentes en el entorno simulado.

### Características y Propósito

Canelo es diseñado para actuar como un líder o coordinador dentro de la simulación. Su propósito principal es tomar decisiones basadas en la información colectiva de todos los agentes y transmitir estas decisiones a los demás agentes para guiar sus acciones. Esto incluye decisiones sobre la implementación de medidas de salud pública, como el uso de mascarillas, la cuarentena, y la adopción de prácticas de distanciamiento social.

### Funcionamiento

El funcionamiento de Canelo se basa en su capacidad para procesar y analizar la información colectiva de los agentes utilizando un *Sistema experto en Prolog*. Canelo utiliza una Interfaz del Mundo personalizada para obtener información actualizada sobre el entorno y el estado de otros agentes. Con esta información, Canelo puede tomar decisiones informadas sobre las medidas que deben implementarse para controlar la propagación de la enfermedad.

### Comunicación y Coordinación

Una de las características clave de Canelo es su capacidad para comunicarse y coordinar con los otros agentes. Utiliza la **Capa de Cooperativa** para transmitir sus decisiones a los demás agentes, facilitando la coordinación de acciones para alcanzar objetivos comunes.

# Entorno

El Entorno es una representación abstracta del espacio en el que los agentes se mueven y interactúan. Este entorno simulado es esencial para modelar la dinámica de la enfermedad y las interacciones entre agentes en un contexto urbano. El entorno se modela utilizando un Grafo. Cada nodo representa una ubicación específica dentro del entorno simulado, como un hospital, un lugar público, un espacio de trabajo, una cuadra o una parada de autobus. Las aristas representan las conexiones entre estos nodos, indicando las rutas posibles que los agentes pueden tomar para moverse entre diferentes ubicaciones. A cada nodo tambien se le calcula una probabilidad de contacto base que depende de la capacidad del nodo y la cantidad de agentes que hayan en este.

# Modelado de la Progresión del Virus

En nuestra simulación, la epidemia es modelada utilizando un agente reactivo que tiene, que su base de conocimientos(también implementada en Prolog) las reglas e información necesaria acerca del progreso de la enfermedad en un ciudadano.

## Cómo se propaga la enfermedad

En cada iteración de la simulación se calculan los contactos(cuando decimos contacto, nos referimos solamente a aquellos que propagan la enfermedad) que tienen agentes que se encuentran en un mismo lugar(nodo). Cada nodo tiene una probabilidad de contacto base y usar distintas medidas higienicas puede reducir esta probabilidad de contacto. Si un agente tiene contacto con otro infectado, la enfermedad se propaga con una probabilidad.

## Progresión de la Enfermedad

La progresión de la enfermedad describe cómo un agente infectado puede pasar de una etapa de infección a otra, desde asintomomático hasta terminal. Este proceso se modela a través de una serie de reglas que describen las condiciones bajo las cuales un agente puede progresar de una etapa a otra.

### Factores de Riesgo

Existen varios factores que pueden aumentar el riesgo de infección y de progresión de la enfermedad, como pudiera ser la edad del ciudadano o la densidad poblacional de un nodo, la cantidad de agentes en este de acuerdo a la capacidad. La capacidad de un nodo no determina el maximo de agentes que pueden estar en este, pero a partir de este punto se tiene la máxima probabilidad de contacto.

# IA

## Búsqueda

Usamos A star para hallar el camino mas corto de un punto a otro y, cuando los agentes quieran evitar el contacto minimizar la exposicion de estos

## Interfaz de Usuario y Procesamiento del Lenguaje Natural

Para mejorar la interacción con la simulación, desarrollamos una interfaz de usuario que permite a estos interactuar con la simulación mediante comandos de lenguaje natural. Utilizamos técnicas de procesamiento del lenguaje natural (NLP) para interpretar los comandos del usuario y mapearlos a acciones en la simulación.

### Sistema Experto

En nuestra simulación, implementamos un sistema experto utilizando Prolog para guiar las decisiones del agente institucional (Canelo) en la implementación de medidas para contener la enfermedad. El sistema experto se basa en reglas lógicas que reflejan las recomendaciones de salud pública y epidemiología.

### Funcionamiento

El sistema experto se basa en una serie de reglas que establecen condiciones y acciones a seguir. Por ejemplo, una regla podría ser:

'''
si la tasa de infección es alta y la capacidad hospitalaria es baja, entonces se debe implementar una cuarentena.
'''

El sistema experto evalúa estas reglas con respecto al estado actual de la simulación y las decisiones previas tomadas, generando recomendaciones para el agente institucional. Para realizar este sistema experto utilizamos el algoritmo genético sobre una serie de parámetros que este agente utiliza para tomar desiciones.

## Búsqueda

En nuestra simulación, utilizamos el algoritmo A* implementado en clases prácticas para resolver dos problemas muy similares, haciendo un cambio de las funciones g(n) y h(n). Uno de estos fue encontrar el camino de longitud mínima, el cuál se utiliza por defecto por los agentes, y otro que intenta minimizar la exposición a la enfermedad priorizando moverse por nodos con menos densidad poblacional.

## Resultados Experimentales

ok

# Conclusiones

ok

# Bibliografía

[1] https://towardsdatascience.com/introducing-geneal-a-genetic-algorithm-python-library-db69abfc212c  
[2] https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009149  
[3] https://github.com/diogomatoschaves/geneal  
[4] https://jmvidal.cse.sc.edu/library/muller93a.pdf  