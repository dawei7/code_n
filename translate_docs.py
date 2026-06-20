import os
import glob
import re
import time
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='de')

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    placeholders = []
    
    # Extract Code Blocks
    def replacer_code(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'```.*?```', replacer_code, text, flags=re.DOTALL)
    
    # Extract inline code
    def replacer_inline_code(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'`[^`]+`', replacer_inline_code, text)
    
    # Extract Math
    def replacer_math(match):
        placeholders.append(match.group(0))
        return f'[[[PH_{len(placeholders)-1}]]]'
    text = re.sub(r'\$\$[^\$]+\$\$', replacer_math, text, flags=re.DOTALL)
    text = re.sub(r'\$[^\$]+\$', replacer_math, text)
    
    # Translate
    # Chunk by double newline
    chunks = text.split('\n\n')
    translated_chunks = []
    
    current_chunk = ""
    for chunk in chunks:
        if len(current_chunk) + len(chunk) < 4500:
            if current_chunk:
                current_chunk += '\n\n' + chunk
            else:
                current_chunk = chunk
        else:
            if current_chunk.strip():
                try:
                    translated_chunks.append(translator.translate(current_chunk.strip()))
                except Exception as e:
                    print(f"Error translating chunk: {e}")
                    translated_chunks.append(current_chunk.strip())
            current_chunk = chunk
            time.sleep(0.1) # basic rate limit

    if current_chunk.strip():
        try:
            translated_chunks.append(translator.translate(current_chunk.strip()))
        except Exception as e:
            print(f"Error translating chunk: {e}")
            translated_chunks.append(current_chunk.strip())

    translated_text = '\n\n'.join(translated_chunks)

    # Restore placeholders
    # Fix spaces inserted by Google Translate
    translated_text = re.sub(r'\[\s*\[\s*\[\s*PH_(\d+)\s*\]\s*\]\s*\]', r'[[[PH_\1]]]', translated_text)
    
    for i, ph in enumerate(placeholders):
        translated_text = translated_text.replace(f'[[[PH_{i}]]]', ph)
        
    return translated_text


md_files = [f for f in glob.glob('docs/**/*.md', recursive=True) if not f.endswith('_de.md') and 'README' not in f and '_template' not in f]

count = 0
for file in md_files:
    target_file = file[:-3] + '_de.md'
    if not os.path.exists(target_file):
        try:
            translated = process_file(file)
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated)
            count += 1
            print(f"[{count}] Translated: {file}")
        except Exception as e:
            print(f"Failed to process {file}: {e}")
            
print(f"Successfully processed {count} files.")
