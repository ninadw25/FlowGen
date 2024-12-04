import os
import subprocess
import streamlit as st
import re
from PIL import Image, ImageEnhance



def save_mermaid_to_file(mermaid_code, temp_dir):
    filename = f"flowchart_{os.urandom(4).hex()}.mmd"
    filepath = os.path.join(temp_dir, filename)
    with open(filepath, 'w') as f:
        f.write(mermaid_code)
    return filepath

# def generate_png_from_mmd(mmd_filepath, temp_png_dir):
#     mmdc_path = r"C:\Users\ninad\AppData\Roaming\npm\mmdc.cmd"

#     if mmdc_path is None:
#         st.error("Could not find mmdc command.")
#         return None

#     output_filename = os.path.basename(mmd_filepath).replace('.mmd', '.png')
#     output_filepath = os.path.join(temp_png_dir, output_filename)
#     command = [
#         mmdc_path,
#         '-i', mmd_filepath,
#         '-o', output_filepath,
#         '-t', 'dark',
#         '-b', 'transparent',
#         # '-p', 'A3',    # Use A0 paper size for more space
#     ]
#     try:
#         result = subprocess.run(command, check=True, capture_output=True, text=True)
#         return output_filepath
#     except subprocess.CalledProcessError as e:
#         st.error(f"Error generating image: {e.stderr}")
#         return None

import os
import subprocess
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

def generate_png_from_mmd(mmd_filepath, temp_png_dir):
    mmdc_path = r"C:\Users\ninad\AppData\Roaming\npm\mmdc.cmd"

    if mmdc_path is None:
        st.error("Could not find mmdc command.")
        return None

    output_filename = os.path.basename(mmd_filepath).replace('.mmd', '.png')
    output_filepath = os.path.join(temp_png_dir, output_filename)
    
    command = [
        mmdc_path,
        '-i', mmd_filepath,
        '-o', output_filepath,
        '-t', 'dark',
        '-b', 'transparent'
    ]
    
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        # Open the image with PIL
        img = Image.open(output_filepath)
        
        # Advanced image enhancement
        # 1. Resize with high-quality algorithm
        width, height = img.size
        new_width = width * 3  # Triple the width
        new_height = height * 3  # Triple the height
        img_resized = img.resize((new_width, new_height), Image.LANCZOS)
        
        # 2. Apply subtle sharpening filter
        img_sharp = img_resized.filter(ImageFilter.SHARPEN)
        
        # 3. Enhance contrast and color
        enhancer_contrast = ImageEnhance.Contrast(img_sharp)
        img_contrast = enhancer_contrast.enhance(1.3)
        
        enhancer_color = ImageEnhance.Color(img_contrast)
        img_color = enhancer_color.enhance(1.1)
        
        # 4. Final brightness adjustment
        enhancer_brightness = ImageEnhance.Brightness(img_color)
        img_final = enhancer_brightness.enhance(1.1)
        
        # Save the enhanced image
        enhanced_filepath = os.path.join(temp_png_dir, f"enhanced_{output_filename}")
        img_final.save(enhanced_filepath, quality=95)
        
        return enhanced_filepath
    
    except subprocess.CalledProcessError as e:
        st.error(f"Error generating image: {e.stderr}")
        return None

def clean_mermaid_code(raw_mermaid_code):
    cleaned_code = raw_mermaid_code.strip()
    
    if cleaned_code.startswith("```mermaid"):
        cleaned_code = cleaned_code.replace("```mermaid", "").strip()
        
    if cleaned_code.endswith("```"):
        cleaned_code = cleaned_code.replace("```", "").strip()
    return cleaned_code

def transform_mermaid_text(mermaid_code):
    """
    Transform Mermaid code by ensuring specific text sections are enclosed in quotes.
    
    Rules:
    1. Enclose text inside { } in quotes if not already quoted
    2. Enclose text inside [ ] in quotes if not already quoted
    3. Enclose text after | in quotes if not already quoted, excluding parenthetical text
    
    Args:
        mermaid_code (str): Original Mermaid code string
    
    Returns:
        str: Transformed Mermaid code
    """
    def process_section(line):
        # Process curly braces sections
        def quote_curly_braces(match):
            content = match.group(1)
            # If not already quoted, add quotes
            if not (content.startswith('"') and content.endswith('"')):
                return '{' + f'"{content}"' + '}'
            return match.group(0)
        
        line = re.sub(r'\{([^}]*)\}', quote_curly_braces, line)
        
        # Process square brackets sections
        def quote_square_brackets(match):
            content = match.group(1)
            # If not already quoted, add quotes
            if not (content.startswith('"') and content.endswith('"')):
                return '[' + f'"{content}"' + ']'
            return match.group(0)
        
        line = re.sub(r'\[([^\]]*)\]', quote_square_brackets, line)
        
        # Process pipe sections
        def quote_pipe_section(match):
            before_pipe = match.group(1)
            # If the section after pipe is not already quoted and does not contain parentheses
            if not re.match(r'.*".*', before_pipe) and '(' not in before_pipe:
                return f'|"{before_pipe}"'
            return match.group(0)
        
        line = re.sub(r'\|([^(]*)', quote_pipe_section, line)
        
        return line

    # Process each line
    transformed_lines = []
    for line in mermaid_code.split('\n'):
        transformed_line = process_section(line)
        transformed_lines.append(transformed_line)
    
    return '\n'.join(transformed_lines)






# def extract_mermaid_code(raw_mermaid_code):
#     lines = raw_mermaid_code.splitlines()
#     in_mermaid_block = False
#     cleaned_code = []
    
#     for line in lines:
#         if line.startswith("```mermaid"):
#             in_mermaid_block = True
#         elif line.startswith("```"):
#             in_mermaid_block = False
#         elif in_mermaid_block:
#             cleaned_code.append(line)
#     return "\n".join(cleaned_code)