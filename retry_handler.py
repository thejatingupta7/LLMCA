"""
Retry logic module for handling API rate limits and failures.
"""

import time


class RetryHandler:
    """Handles retry logic for API calls."""
    
    def __init__(self, max_retries=5, initial_wait_time=61):
        """
        Initialize retry handler.
        
        Args:
            max_retries (int): Maximum number of retries
            initial_wait_time (int): Initial wait time in seconds
        """
        self.max_retries = max_retries
        self.initial_wait_time = initial_wait_time
    
    def execute_with_retry(self, func, *args, **kwargs):
        """
        Execute a function with retry logic.
        
        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments
            
        Returns:
            Result of the function or None if max retries exceeded
        """
        retries = 0
        wait_time = self.initial_wait_time
        
        while retries < self.max_retries:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_str = str(e)
                if self._is_rate_limit_error(error_str):
                    print(f"Rate limit exceeded. Waiting for {wait_time} seconds before retrying...")
                    time.sleep(wait_time)
                    retries += 1
                    wait_time *= 2  # Exponential backoff
                    
                    # Ask for new token if callback provided
                    if 'token_callback' in kwargs:
                        new_token = kwargs['token_callback']()
                        kwargs['api_client'].update_token(new_token)
                else:
                    raise e  # Reraise exception if it's not a rate limit issue
        
        print(f"Max retries exceeded. Skipping.")
        return None
    
    @staticmethod
    def _is_rate_limit_error(error_str):
        """Check if error is related to rate limiting."""
        return "RateLimitReached" in error_str or "429" in error_str
