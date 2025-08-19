"""
Main processor module that orchestrates the entire workflow.
"""

import os
from api_client import APIClient
from file_handler import FileHandler
from retry_handler import RetryHandler
from config import OUTPUT_COLUMNS


class TextProcessor:
    """Main processor class that handles the complete workflow."""
    
    def __init__(self):
        """Initialize the text processor."""
        self.api_client = APIClient()
        self.file_handler = FileHandler()
        self.retry_handler = RetryHandler()
    
    def get_new_token(self):
        """Callback function to get new token from user."""
        return input("Please enter a new token: ")
    
    def process_single_file(self, file_path, filename, subdir):
        """
        Process a single text file.
        
        Args:
            file_path (str): Path to the file
            filename (str): Name of the file
            subdir (str): Subdirectory name
            
        Returns:
            list or None: [filename, question, answer] if successful, None otherwise
        """
        question = self.file_handler.read_text_file(file_path)
        
        def api_call():
            return self.api_client.get_completion(question)
        
        answer = self.retry_handler.execute_with_retry(
            api_call,
            token_callback=self.get_new_token,
            api_client=self.api_client
        )
        
        if answer is not None:
            print(f"Processed {filename} in {subdir}")
            return [filename, question, answer]
        else:
            print(f"Failed to process {filename} in {subdir}")
            return None
    
    def process_subdirectory(self, base_folder, subdir):
        """
        Process all text files in a subdirectory.
        
        Args:
            base_folder (str): Base folder path
            subdir (str): Subdirectory name
            
        Returns:
            list: List of processed data
        """
        subdir_path = os.path.join(base_folder, subdir)
        data = []
        
        text_files = self.file_handler.get_text_files_sorted(subdir_path)
        
        for filename in text_files:
            file_path = os.path.join(subdir_path, filename)
            result = self.process_single_file(file_path, filename, subdir)
            
            if result:
                data.append(result)
        
        return data
    
    def save_results(self, base_folder, subdir, data):
        """
        Save processing results to Excel file.
        
        Args:
            base_folder (str): Base folder path
            subdir (str): Subdirectory name
            data (list): Data to save
        """
        output_file = os.path.join(base_folder, f"responses_{subdir}.xlsx")
        
        if self.file_handler.save_to_excel(data, output_file, OUTPUT_COLUMNS):
            print(f"Responses saved to {output_file}")
        else:
            print(f"No data to save for {subdir}")
    
    def process_all_subdirectories(self, base_folder):
        """
        Process all subdirectories in the base folder.
        
        Args:
            base_folder (str): Path to the base folder
        """
        subdirectories = self.file_handler.get_subdirectories(base_folder)
        
        for subdir in subdirectories:
            print(f"Processing subdirectory: {subdir}")
            data = self.process_subdirectory(base_folder, subdir)
            self.save_results(base_folder, subdir, data)
