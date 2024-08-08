from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

app = Flask(__name__)

# Load the GPT-2 model and tokenizer
model_name = 'gpt2'  # Ensure the correct model name
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultation', methods=['POST'])
def consultation():
    data = request.json
    user_input = data.get('input_text')
    
    # Generate a response
    response = generator(user_input, max_length=50, num_return_sequences=1)
    return jsonify({'response': response[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
