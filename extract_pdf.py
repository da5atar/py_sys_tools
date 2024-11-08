#!/usr/bin/env python3

"""
This module provides functionality to extract content from PDF files,
including text, tables, and images, and save them in various formats.
"""

import os
import pathlib
import pymupdf4llm

def main():
    """
    Main function to execute the PDF extraction based on user input.
    """
    # Default output directory (configurable)
    default_output_dir = "output"

    # Ask user for output directory or use default
    output_dir = input(
        f"Enter output directory (default: '{default_output_dir}'): "
    ) or default_output_dir
    output_path = pathlib.Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Display options to the user
    print("\nSelect an operation:")
    print("1. Extract PDF to Markdown")
    print("2. Extract Tables")
    print("3. Extract Images")
    choice = input("Enter your choice (1/2/3): ")

    # Validate choice
    if choice not in {'1', '2', '3'}:
        print("Invalid choice. Exiting.")
        return

    # Get input PDF path from the user
    pdf_path = input("Enter the path to the PDF file: ").strip()

    # Validate PDF path
    if not os.path.isfile(pdf_path):
        print(f"File '{pdf_path}' not found. Exiting.")
        return

    # Perform the selected operation
    if choice == '1':
        extract_markdown(pdf_path, output_path)
    elif choice == '2':
        extract_tables(pdf_path, output_path)
    elif choice == '3':
        extract_images(pdf_path, output_path)

def extract_markdown(pdf_path, output_path):
    """
    Extracts text from the PDF and saves it as a Markdown file.

    Parameters:
    - pdf_path: Path to the input PDF file.
    - output_path: Directory where the output will be saved.
    """
    # Extract text to Markdown
    md_text = pymupdf4llm.to_markdown(pdf_path)
    # Save Markdown text to file
    output_file = output_path / "output.md"
    output_file.write_text(md_text, encoding='utf-8')
    print(f"\nMarkdown extracted and saved to '{output_file}'.")

def extract_tables(pdf_path, output_path):
    """
    Extracts tables from the PDF and saves them in Markdown format.

    Parameters:
    - pdf_path: Path to the input PDF file.
    - output_path: Directory where the output will be saved.
    """
    # Extract tables to Markdown
    md_text_tables = pymupdf4llm.to_markdown(doc=pdf_path)
    # Save tables to Markdown file
    output_file = output_path / "tables.md"
    output_file.write_text(md_text_tables, encoding='utf-8')
    print(f"\nTables extracted and saved to '{output_file}'.")

def extract_images(pdf_path, output_path):
    """
    Extracts images from the PDF and saves them along with a Markdown file
    containing image references.

    Parameters:
    - pdf_path: Path to the input PDF file.
    - output_path: Directory where the output will be saved.
    """
    # Create a subdirectory for images
    images_dir = output_path / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    # Extract images and save Markdown with image references
    md_text_images = pymupdf4llm.to_markdown(
        doc=pdf_path,
        write_images=True,
        image_path=str(images_dir),
        image_format="png",
        dpi=300
    )
    # Save Markdown text to file
    output_file = output_path / "images.md"
    output_file.write_text(md_text_images, encoding='utf-8')
    print(f"\nImages extracted to '{images_dir}'.")
    print(f"Markdown with image references saved to '{output_file}'.")

if __name__ == "__main__":
    main()
