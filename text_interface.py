import streamlit as st
import gpt4all as gpt
from gpt4all import GPT4All
# from simulation.main import function, factorial, contar_palabras, filtrar_lista, calcular_media, es_primo, maximo_lista, suma
import io
import sys
from simulation.epi_sim import Simulation

s = Simulation()
s.initialize_simulation()
s.simulate()


model = GPT4All("/home/chony/LLM/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q4_K_S.gguf")

st.title("EpiDoc")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "user",
        "content": """
                   Bienvenido a Epidoc,su app para simular el comportamiento de epidemias. Se muestra una entrada de texto donde puede proporcionar la siguiente informacion sobre como quiere que se desarrolle la epidemia:

- **Días de simulación**: Un número entero que indica la cantidad de días que durará la simulación (por ejemplo, 31).
- **Tamaño de la cuadrícula**: Un número entero que representa las dimensiones de la cuadrícula de la simulación (por ejemplo, 10).
- **Capacidad por bloque**: Un número entero que señala la capacidad máxima de cada bloque (por ejemplo, 100).
- **Cantidad de casas**: Un número entero que indica el total de casas en la simulación (por ejemplo, 10).
- **Capacidad de cada casa**: Un número entero que determina cuántas entidades pueden ocupar cada casa (por ejemplo, 5).
- **Cantidad de hospitales**: Un número entero que señala el número de hospitales disponibles (por ejemplo, 4).
- **Capacidad de cada hospital**: Un número entero que define la capacidad de cada hospital (por ejemplo, 50).
- **Horario de los hospitales**: Un par de números enteros que representan las horas de operación (por ejemplo, (8, 20)).
- **Cantidad de áreas recreativas**: Un número entero que indica el número de áreas recreativas (por ejemplo, 4).
- **Capacidad de cada área recreativa**: Un número entero que determina la capacidad de cada área recreativa (por ejemplo, 20).
- **Horario de las áreas recreativas**: Un par de números enteros que representan las horas de operación (por ejemplo, (8, 20)).
- **Cantidad de lugares de trabajo**: Un número entero que indica el número de lugares de trabajo (por ejemplo, 4).
- **Capacidad de cada lugar de trabajo**: Un número entero que determina la capacidad de cada lugar de trabajo (por ejemplo, 10).
- **Horario de los lugares de trabajo**: Un par de números enteros que representan las horas de operación (por ejemplo, (8, 20)).
- **Cantidad de agentes**: Un número entero que define el número total de agentes en la simulación (por ejemplo, 20).

No tiene que proporcionar todos los datos pero se agradece. Si tiene alguna pregunta o necesita asistencia, no dude en contactarnos. ¡Gracias por utilizar nuestra aplicación!
"""
    })
    st.session_state.messages.append({
        "role": "user",
        "content": """Quiero que mi chatbot responda únicamente con llamados a las siguientes funciones de Python, sin ningún texto ni comentario adicional:
                    - function(nombre_funcion, *args, **kwargs): llama a la función con el nombre especificado y los argumentos proporcionados.
                    - factorial(n): calcula el factorial de un número entero n.
                    - contar_palabras(frase): cuenta el número de palabras en una frase.
                    - filtrar_lista(funcion_filtro, lista): filtra una lista utilizando una función de filtro.
                    - calcular_media(numeros): calcula la media aritmética de una lista de números.

                    Por favor, asegúrate de que tus respuestas sean únicamente llamados a estas funciones.$
                    """
    })
    st.session_state.messages.append({
        "role": "user",
        "content": """El simbolo $ al final de mis prompts significa que ya terminde de escribir no me sigas autocompletando"""
    })
    st.session_state.messages.append({
        "role": "user",
        "content": "cual es el factorial de 5 ?$"
    })
    st.session_state.messages.append({
        "role": "assistent",
        "content": "factorial(5)"
    })
    st.session_state.messages.append({
        "role": "user",
        "content": "cuantas palabras tiene la oracion: hola mundo$"
    })
    st.session_state.messages.append({
        "role": "assistent",
        "content": "contar_palabras([hola, mundo])"
    })
    st.session_state.messages.append({
        "role": "user",
        "content": "calcula la media de 5 numeros primos cualesquiera$"
    })
    st.session_state.messages.append({
        "role": "assistent",
        "content": "calcular_media([3,3,3,5,7])"
    })
    st.session_state.messages.append({
        "role": "user",
        "content": "5 es un numero primo?$"
    })
    st.session_state.messages.append({
        "role": "assistent",
        "content": "es_primo(5)"
    })
    st.session_state.messages.append({
        "role": "user",
        "content": "cual es el maximo de esta lista [2,3]$"
    })
    st.session_state.messages.append({
        "role": "assistent",
        "content": "maximo_lista([2,3])"
    })
    st.session_state.messages.append({
        "role": "user",
        "content": "suma 2 y 3$"
    })
    st.session_state.messages.append({
        "role": "assistent",
        "content": "suma(2,3)"
    })
    
# Convertir el historial en una cadena de texto
historial_texto = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])

print(historial_texto)


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# Assigning and determining the messages that the user will enter from the prompt
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Pasar el historial y el mensaje del usuario al modelo
    # Suponiendo que 'model' es tu modelo de lenguaje y que tiene un método 'generate'
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
        
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        response = model.generate(historial_texto + "\n" + "user: " + prompt + "$")
        content = message_placeholder.markdown(response)
        
        res = response.replace("assistant:", "", 1)
        res = res.replace(" ", "")
        
        print(res)
        result = eval(res)
        print(result)

        
        # Finalmente, agregamos al asistente y al usuario al historial.
        st.session_state.messages.append({"role": "assistent", "content": response})
    
    

