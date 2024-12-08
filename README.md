# Multi-Language-Translator

## Overview
The **Multi Language Translator** is a web-based application that translates English text into a wide range of languages. It uses the powerful **facebook/nllb-200-distilled-600M** model for translation, ensuring accurate and contextually relevant translations. The application leverages Gradio for a user-friendly interface, making it easy for users to input text and select their desired target language.

## Features
- **Multi-Language Support:** Translate English text into multiple languages using the FLORES-200 language codes.
- **Dropdown Language Selection:** Choose your desired target language from a sorted list of available languages.
- **User-Friendly Interface:** A clean and simple Gradio-based interface for seamless interaction.
- **Efficient Translation:** Utilizes a high-performance transformer model for fast and accurate translations.

## How It Works
1. **Input Text:** Enter the English text you want to translate in the textbox provided.
2. **Select Target Language:** Choose the target language from the dropdown menu.
3. **Get Translated Text:** Click the "Submit" button to generate the translation.

The application fetches the FLORES-200 language code for the selected language and performs the translation using the `facebook/nllb-200-distilled-600M` model.

## Installation

To use this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/multi-language-translator.git
   cd multi-language-translator
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Prepare the language data: Ensure the file language.json is in the root directory. This file should contain language names and their corresponding FLORES-200 codes.

Run the application:

bash
Copy code
python app.py
Access the app: Open your browser and go to http://localhost:7860.

# Dependencies
Gradio: For building the interactive user interface.
Transformers: For using the pre-trained NLLB-200 model for translation.
Torch: For optimized execution of the model.
JSON: For handling language data mappings.
# File Structure
bash
Copy code
multi-language-translator/
│
├── app.py                # Main application code
├── language.json         # JSON file containing languages and FLORES-200 codes
├── requirements.txt      # List of required Python packages
└── README.md             # Project documentation
Language Data
The language.json file contains the list of supported languages along with their corresponding FLORES-200 codes. The app uses this data to map user-selected languages to the model's target language format.

Example language.json Structure:
json
Copy code
[
  {
    "Language": "French (Latin script)",
    "FLORES-200 code": "fra_Latn"
  },
  {
    "Language": "Spanish (Latin script)",
    "FLORES-200 code": "spa_Latn"
  }
]
# Usage
Input Text: Type or paste the text you wish to translate in English.
Choose Target Language: Select a language from the dropdown menu (e.g., French, Spanish).
Translate: Click the "Submit" button, and the translated text will appear in the output textbox.
# Future Enhancements
Add support for text-to-speech functionality in multiple languages.
Enable translation between non-English source languages.
Provide real-time language detection for source text.
# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgements
Hugging Face for providing the pre-trained NLLB-200 model.
Gradio for the intuitive web interface framework.
Meta AI Research for the NLLB-200 model development and open-source contributions.
