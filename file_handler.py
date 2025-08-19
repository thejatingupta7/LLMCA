"""
File operations module for handling file I/O operations.
"""

import os
import pandas as pd


class FileHandler:
    """Handles file operations including reading and writing."""
    
    @staticmethod
    def read_text_file(file_path):
        """
        Read content from a text file.
        
        Args:
            file_path (str): Path to the text file
            
        Returns:
            str: File content
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    
    @staticmethod
    def get_subdirectories(base_folder):
        """
        Get list of subdirectories in the base folder.
        
        Args:
            base_folder (str): Path to the base folder
            
        Returns:
            list: List of subdirectory names
        """
        return [subdir for subdir in os.listdir(base_folder) 
                if os.path.isdir(os.path.join(base_folder, subdir))]
    
    @staticmethod
    def get_text_files_sorted(directory):
        """
        Get sorted list of .txt files in a directory.
        
        Args:
            directory (str): Path to the directory
            
        Returns:
            list: Sorted list of .txt filenames
        """
        files = [f for f in os.listdir(directory) if f.endswith(".txt")]
        return sorted(files, key=lambda x: int(x.split('.')[0]))
    
    @staticmethod
    def save_to_excel(data, output_file, columns):
        """
        Save data to Excel file.
        
        Args:
            data (list): List of data rows
            output_file (str): Output file path
            columns (list): Column names for the DataFrame
        """
        if data:
            df = pd.DataFrame(data, columns=columns)
            df.to_excel(output_file, index=False)
            return True
        return False
