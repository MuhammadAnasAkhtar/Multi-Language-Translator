import torch
import gradio as gr
import json

# Use a pipeline as a high-level helper
from transformers import pipeline

text_translator = pipeline("translation", model="facebook/nllb-200-distilled-600M",
                         torch_dtype=torch.bfloat16)

# Load the JSON data from the file
with open('language.json', 'r') as file:
    language_data = json.load(file)

# Get all available languages (excluding duplicates with different scripts)
available_languages = []
seen_languages = set()
for entry in language_data:
    base_language = entry['Language'].split('(')[0].strip()
    if base_language not in seen_languages:
        available_languages.append(base_language)
        seen_languages.add(base_language)

# Sort languages alphabetically
available_languages.sort()

def get_FLORES_code_from_language(language):
    # First try exact match
    for entry in language_data:
        if entry['Language'].lower() == language.lower():
            return entry['FLORES-200 code']
    
    # If no exact match, try matching the base language name
    for entry in language_data:
        if entry['Language'].lower().startswith(language.lower()):
            return entry['FLORES-200 code']
    return None

def translate_text(text, destination_language):
    dest_code = get_FLORES_code_from_language(destination_language)
    if dest_code is None:
        return f"Error: Could not find FLORES code for language {destination_language}"
    
    translation = text_translator(text,
                                src_lang="eng_Latn",
                                tgt_lang=dest_code)
    return translation[0]["translation_text"]

gr.close_all()

demo = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Input text to translate", lines=6),
        gr.Dropdown(choices=available_languages, label="Select Destination Language")
    ],
    outputs=[gr.Textbox(label="Translated text", lines=4)],
    title="Multi Language Translator",
    description="This application translates English text to multiple languages. Select your desired target language from the dropdown menu."
)

if __name__ == "__main__":
    demo.launch()
