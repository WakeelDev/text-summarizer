import os
from transformers import T5Tokenizer, T5ForConditionalGeneration

# ✅ Use relative path so it works on both local & Streamlit Cloud
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "t5-small")

# Load tokenizer and model
tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = T5ForConditionalGeneration.from_pretrained(MODEL_PATH)

def summarize_text(text, max_length=150, min_length=40):
    """
    Summarize the given text using T5-small with optimized decoding.
    """
    # Add T5 prefix for summarization
    input_text = "summarize: " + text

    inputs = tokenizer.encode(
        input_text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    # Generate summary with tuned parameters
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,       # encourage conciseness
        num_beams=4,              # better exploration
        repetition_penalty=2.5,   # reduce copy-paste behavior
        early_stopping=True
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is transforming industries by enabling machines 
    to perform tasks that typically require human intelligence. These tasks include 
    problem-solving, speech recognition, decision-making, and language translation.
    """
    print("\nOriginal Text:\n", sample_text)
    print("\nGenerated Summary:\n", summarize_text(sample_text))
