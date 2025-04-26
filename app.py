import gradio as gr
from ollama import chat

def response(message, history):

    output = chat(model="qwen2.5:0.5b", messages=
                  [
                      {"role": "user", "content": message}
                  ])
    return output["message"]["content"]

gr.ChatInterface(fn=response).launch()