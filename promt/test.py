# Importa los módulos necesarios
import openai
import os

# Carga las variables de entorno desde el archivo .env
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Configura tu clave de API de OpenAI desde la variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

# Función para obtener una completación de texto
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,  # Puedes ajustar la temperatura para controlar la aleatoriedad
    )
    return response.choices[0].message["content"]

# Ejemplo de prompt
prompt = "Traduce la siguiente frase al francés: 'Hola, ¿cómo estás?'"


# Llamada a la función con el prompt
response_text = get_completion(prompt)
print(response_text)
