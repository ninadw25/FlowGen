import streamlit as st
import tempfile
import shutil
from mermaid_generator import mermaid_code
from utils import save_mermaid_to_file, generate_png_from_mmd, clean_mermaid_code,transform_mermaid_text
from styling import add_bg_from_local, get_custom_css

# Create temporary directories
temp_mmd_dir = tempfile.mkdtemp(prefix="mermaid_mmd_")
temp_png_dir = tempfile.mkdtemp(prefix="mermaid_png_")


# between |  | do not use any " " or ' ' 
# And no brackets to be used also

def main():
    # Set page configuration
    st.set_page_config(
        page_title="FlowGen: Code to Flowchart",
        page_icon=":chart_with_upwards_trend:",
        layout="centered",
    )

    # Add background image with reduced opacity
    add_bg_from_local('background_image.jpg')  

    # Add custom CSS
    st.markdown(get_custom_css(), unsafe_allow_html=True)

    # Page Header
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 2.5em; color: #fff;">FlowGen: Code to Flowchart</h1>
        <p style="text-align: center; color: #d1d5db; font-size: 1.2em;">
            Convert your code into clean and visually appealing flowcharts instantly.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Text area for user input
    user_code = st.text_area("", height=200, placeholder="Enter you code in any Programming Language")

    if st.button("Generate Flowchart"):
        if user_code:
            #  STEP 1 : Generate Mermaid code
            raw_mermaid_diagram = mermaid_code(user_code)

            #  STEP 2 :  Clean the Mermaid code
            mermaid_diagram = clean_mermaid_code(raw_mermaid_diagram)
            
            # Display the Mermaid code
            st.subheader("Generated Mermaid Code:")
            st.code(mermaid_diagram, language="mermaid")

            # Save Mermaid code to file
            mmd_filepath = save_mermaid_to_file(mermaid_diagram, temp_mmd_dir)
            st.text(f"Mermaid code saved to: {mmd_filepath}")

            # Generate PNG from Mermaid code
            png_filepath = generate_png_from_mmd(mmd_filepath, temp_png_dir)
            if png_filepath:
                # Display the generated PNG with maximum possible width
                st.subheader("Flowchart:")
                # Ultra-wide display
                col1, col2, col3 = st.columns([0.01, 9.98, 0.01])  # Even more aggressive width
                with col2:
                    st.image(png_filepath, use_column_width=True)
            else:
                st.error("Failed to generate the flowchart image.")
        else:
            st.warning("Please enter user code to Generate.")

    # Footer
    st.markdown(
        """
        <div class="footer">
            Made by <b style="color: #5a67d8;">Ninad Wakode</b> for educational and self learning purpose.
        </div>
        """,
        unsafe_allow_html=True,
    )

# print(f"Temporary Mermaid directory: {temp_mmd_dir}")

if __name__ == "__main__":
    main()

    # Cleanup temporary directories on exit
    shutil.rmtree(temp_mmd_dir, ignore_errors=True)
    shutil.rmtree(temp_png_dir, ignore_errors=True)