"""
API client module for handling OpenAI API interactions.
"""

from openai import OpenAI
from config import TOKEN, ENDPOINT, MODEL_NAME, TEMPERATURE, MAX_TOKENS
from prompts import DEFAULT_PROMPT


class APIClient:
    """Handles API interactions with OpenAI."""
    
    def __init__(self, token=None):
        """Initialize the API client."""
        self.token = token or TOKEN
        self.endpoint = ENDPOINT
        self.model_name = MODEL_NAME
        self.client = OpenAI(base_url=self.endpoint, api_key=self.token)
    
    def update_token(self, new_token):
        """Update the API token and reinitialize client."""
        self.token = new_token
        self.client = OpenAI(base_url=self.endpoint, api_key=self.token)
    
    def get_completion(self, question, system_prompt=None):
        """
        Get completion from the API.
        
        Args:
            question (str): The user question
            system_prompt (str): System prompt to use (defaults to DEFAULT_PROMPT)
            
        Returns:
            str: The API response content
        """
        if system_prompt is None:
            system_prompt = DEFAULT_PROMPT
            
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": question,
                }
            ],
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )
        
        return response.choices[0].message.content
