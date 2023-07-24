import torch
from transformers import StoppingCriteria


class StopOnTokens(StoppingCriteria):
    def __init__(self, stop_token_ids):
        """
        Initializes the StopOnTokens instance.

        Args:
         stop_token_ids (list): A list of token IDs that trigger stopping if the
         last token in the input sequence matches any of these IDs.
        """
        self.stop_token_ids = stop_token_ids

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        """
        Determines if the input sequence should be stopped based on the stop_token_ids.

        Args:
            input_ids (torch.LongTensor): The input sequence represented as a LongTensor.
            scores (torch.FloatTensor): The scores associated with the input sequence.
            **kwargs: Additional keyword arguments.

        Returns:
            bool: True if the last token in the input sequence matches any stop_token_id,
            False otherwise.
        """

        for stop_id in self.stop_token_ids:
            if input_ids[0][-1] == stop_id:
                # input_ids = input_ids[:, :-1]
                return True
        return False
