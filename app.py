### ARIA – AI-Responsive Interactive Assistant

from flask import Flask, request, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from web_search_tool import web_search
import warnings
warnings.filterwarnings("ignore", message="Failed to load image Python extension")


app = Flask(__name__)

# Load model and tokenizer
checkpoint = "HuggingFaceTB/SmolLM2-360M-Instruct"
device = "cuda" if torch.cuda.is_available() else "cpu"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_query = request.form["query"]
        mode = request.form.get("mode", "web")  # Default to web search mode

        # Different prompts based on mode
        if mode == "web":
            try:
                context = web_search(user_query)
            except Exception as e:
                context = "No additional context could be retrieved."
                print("Web search failed:", e)

            system_prompt = (
                "You are a voice assistant that answers in a polite and professional tone. "
                "Use the following context to help answer the question:\n"
                f"{context}\n"
                "If the context is insufficient, still try to give the best possible answer."
            )
        elif mode == "reasoning":
            system_prompt = (
                "You are a voice assistant specialized in logical reasoning and problem-solving. "
                "Break down the problem systematically and explain your thought process step by step. "
                "Consider different angles and approaches to arrive at a well-reasoned conclusion."
            )
            context = ""
        else:  # creative mode
            system_prompt = (
                "You are a voice assistant with a flair for creative and imaginative responses. "
                "Think outside the box and provide unique, innovative perspectives while maintaining "
                "relevance to the query. Feel free to use metaphors, analogies, and vivid descriptions."
            )
            context = ""

        # System prompt setup with context included
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]

        input_text = tokenizer.apply_chat_template(messages, tokenize=False)
        inputs = tokenizer.encode(input_text,
                                return_tensors="pt",
                                padding=True,
                                truncation=True).to(device)
        
        outputs = model.generate(
            inputs,
            max_new_tokens=128
        )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract only the assistant's reply
        if "assistant" in response:
            response = response.split("assistant")[-1].strip(": ").strip()
        else:
            response = "Sorry, couldn't understand your query. Can you ask again?"

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

