# FlowGen: Code to Flowchart Converter

FlowGen is an interactive Streamlit application that converts code from any programming language into flowcharts using Mermaid MD language. This tool leverages the power of the Llama 3 Large Language Model (LLM) to translate code logic into clear, visual flowcharts, making it easier to understand complex codebases.

![FlowGen Workflow](./path_to_your_image/Working_of_FlowGen.png)

---

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- **Supports All Languages**: Converts code from any language into a flowchart.
- **Mermaid MD Integration**: Uses Mermaid for flowchart syntax, supporting easy rendering and export.
- **Image Export**: Generates a PNG image of the flowchart.
- **Error Cleaning**: Automatically cleans Mermaid code syntax errors for seamless visualization.

---

## How It Works
FlowGen's process involves multiple stages, as outlined below:

1. **Taking Input**  
   - The Streamlit frontend accepts code in any programming language from the user.

2. **LLM Model Processing**  
   - The code is sent to the Llama 3 Large Language Model (LLM) via API calls to convert the code logic into flowchart-friendly Mermaid code.

3. **Prompt Making**  
   - An appropriate prompt is crafted to ensure the LLM generates the correct Mermaid code for the flowchart.

4. **Mermaid Code Generation**  
   - FlowGen uses Mermaid MD, a library that provides syntax for various diagram types, to structure the flowchart.

5. **Cleaning Mermaid Code**  
   - Any syntax errors in the Mermaid code are automatically cleaned to ensure compatibility with the `mmdc` command.

6. **Diagram Generation**  
   - The cleaned Mermaid code is saved to a `.mmd` file and then processed by the `mmdc` command to generate a `.png` image.

7. **Displaying Output**  
   - The final flowchart is displayed in the Streamlit frontend within seconds.

---

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/flowgen.git
    cd flowgen
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure Mermaid CLI (`mmdc`) is installed globally:
    - Follow the instructions [here](https://mermaid-js.github.io/mermaid-cli/) to install `mmdc`.

4. Set the path to `mmdc` in the `generate_png_from_mmd` function of `app.py`:
    ```python
    mmdc_path = r"C:\path_to_your_mmdc\mmdc.cmd"
    ```

---

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Enter code in any programming language in the provided text area on the Streamlit interface.

3. Click on "Generate Flowchart" to visualize the flowchart of your code.

4. The generated flowchart in Mermaid format will be displayed, along with a `.png` image of the flowchart.

---

## Example

Here is an example of how the code works internally.

```python
def save_mermaid_to_file(mermaid_code):
    filename = f"flowchart_{os.urandom(4).hex()}.mmd"
    filepath = os.path.join(temp_mmd_dir, filename)
    with open(filepath, 'w') as f:
        f.write(mermaid_code)
    return filepath
