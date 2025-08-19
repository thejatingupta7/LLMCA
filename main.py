"""
Main entry point for the text processing application.

This script orchestrates the entire workflow by importing and using
modular components for processing text files with AI completions.
"""

from processor import TextProcessor
from config import BASE_FOLDER


def main():
    """Main function that runs the entire text processing workflow."""
    print("Starting text file processing...")
    print(f"Base folder: {BASE_FOLDER}")
    
    # Initialize the processor
    processor = TextProcessor()
    
    # Process all subdirectories
    processor.process_all_subdirectories(BASE_FOLDER)
    
    print("All exams processed successfully!")


if __name__ == "__main__":
    main()