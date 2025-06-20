from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

def load_model(model_name="microsoft/DialoGPT-small"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return generator
