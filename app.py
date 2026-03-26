import os
import gradio as gr
from google import genai
from google.genai import types

# 🔴 BOTÓN ROJO PARA MODO CLARO
os.environ["GRADIO_THEME"] = "light"

# 1. API Key segura
api_key = os.environ.get("GEMINI_API_KEY", "AIzaSyA7LjsUxnnCM-IsnTDcHrg0ZXKkxysH6iM")
client = genai.Client(api_key=api_key)

# 2. Instrucciones
system_instruction = """
Sei "Pazienza IA", un assistente tecnico progettato esclusivamente per gli anziani. 
La tua personalità è estremamente paziente, calorosa, rispettosa e incoraggiante. 
REGOLE RIGOROSE:
1. NON usare MAI gergo tecnico. 
2. Usa sempre analogie del mondo fisico.
3. NON dare mai più di un'istruzione alla volta. Aspetta che l'utente confermi.
4. Se l'utente si frustra, convalida i suoi sentimenti.
"""

chat = client.chats.create(
    model="gemini-3.1-pro-preview",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
    )
)

def responder(mensaje, historial):
    response = chat.send_message(mensaje)
    return response.text

# 3. 
css_final = """
/* Fondo general */
body, :root { background-color: #FFF9F2 !important; }

/*  Centrar y hacer más estrecha la aplicación */
#app-container {
    max-width: 800px !important; 
    margin: 0 auto !important; 
    padding-top: 20px;
}

/* Forzar fondo blanco */
.chatbot, .block {
    background-color: #FFFFFF !important; 
    border-radius: 20px !important;
}

/* Letras y globos */
body, *, .chatbot, .textbox, button { font-size: 22px !important; }
.message.user { background-color: #FFE5D9 !important; color: #5D4037 !important; border-radius: 20px 20px 5px 20px !important; padding: 15px !important; }
.message.bot { background-color: #EBF5FB !important; color: #154360 !important; border-radius: 20px 20px 20px 5px !important; padding: 15px !important; }

/* Limpiar basura visual */
footer, .svelte-1gfknrx { display: none !important; }
"""

# 4. Interfaz centrada
with gr.Blocks(css=css_final, theme=gr.themes.Soft(primary_hue="orange")) as demo:
    
    # Columna estrecha centrada
    with gr.Column(elem_id="app-container"):
        gr.HTML(
            """
            <div style='background-color: #FFF3E0; padding: 25px; border-radius: 25px; text-align: center; border: 2px solid #FFE0B2; margin-bottom: 15px;'>
                <h1 style='margin: 0; color: #D35400;'>👵 Pazienza IA 👴</h1>
                <p style='margin-top: 5px; color: #873600; font-size: 20px;'>Il tuo assistente tecnologico sereno e amichevole.</p>
            </div>
            """
        )
        gr.ChatInterface(fn=responder)

#  modo claro
js_claro = "function() { document.body.classList.remove('dark'); }"

if __name__ == "__main__":
    # Prueba local
    demo.launch(share=True, js=js_claro)
