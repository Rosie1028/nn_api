from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import preprocessing

class ResumenModel:
    def __init__(self) -> None:
        self.model = self._load_token_model()

    def _load_token_model(self):
        """Load and return tokenizer and model"""
        name = "ELiRF/NASES"
        return AutoTokenizer.from_pretrained(name), AutoModelForSeq2SeqLM.from_pretrained(name)
    
    def _codification(self, article: str):
        tokenizer, model = self.model
        article = preprocessing.strip_url(article)
        article = preprocessing.strip_emoji(article)
        article = preprocessing.remove_extra_whitespace(article)

        a = tokenizer.tokenize(article)
        print(a)

        inputs = tokenizer.encode(article, return_tensors="pt", max_length =512,padding='longest', truncation=True)
        print(inputs)
        return tokenizer, model, inputs
    
    def generate_summary(self, text: str) -> str:
        tokenizer, model, inputs = self._codification(text)
        
        outputs = model.generate(
            inputs,
            max_length = 512,
            min_length =80,
            length_penalty = 2.0,
            num_beams = 4,
            early_stopping = True
        )
        print(outputs)
        print(tokenizer.decode(outputs[0]))

        return tokenizer.decode(outputs[0])


nases_model = ResumenModel()