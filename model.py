from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from typing import Optional
from config import settings
import preprocessing
import logging

logger = logging.getLogger(__name__)

class SummaryModel:
    """
    Wrapper for loading a pretrained summarization model and generating summaries.
    """
    def __init__(self, model_name: str = settings.MODEL_NAME) -> None:
        self.tokenizer = None
        self.model = None
        self.model_name = model_name
        self._load_model_and_tokenizer()

    def _load_model_and_tokenizer(self) -> None:
        """Load the tokenizer and model from HuggingFace."""
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)
        except Exception as e:
            logging.error(f"Failed to load model or tokenizer: {e}")
            raise

    def _preprocess(self, text: str) -> str:
        """Apply preprocessing steps to the input text."""
        text = preprocessing.remove_url(text)
        text = preprocessing.remove_emoji(text)
        text = preprocessing.remove_extra_whitespace(text)
        return text

    def generate_summary(self, text: str) ->Optional[str]:
        """
        Generate a summary for the given text.
        """
        try:
            logger.info("Generating summary for text of length %d characters", len(text))
            preprocessed_text = self._preprocess(text)
            inputs = self.tokenizer.encode(
            preprocessed_text,
            return_tensors="pt",
            max_length=512,
            padding='longest',
            truncation=True
            )
            outputs = self.model.generate(
            inputs,
            max_length=512,
            min_length=80,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True
            )
            summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            logger.info("Generated summary of length %d characters", len(summary))
            return summary
        except Exception as e:
            logger.error("Error generating summary: %s", e)
            raise

# Singleton instance
nases_model = SummaryModel()