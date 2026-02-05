from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='.')
CORS(app)

# Perplexity API configuration - Use environment variable for security
PERPLEXITY_API_KEY = os.environ.get('PERPLEXITY_API_KEY', '')
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

@app.route('/')
def home():
    """Serve the main HTML file"""
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests with Perplexity API"""
    try:
        data = request.json
        user_message = data.get('message', '')
        api_key = data.get('api_key', PERPLEXITY_API_KEY)
        
        if not user_message:
            return jsonify({
                "error": "Message is required",
                "status": "error"
            }), 400
        
        if not api_key:
            return jsonify({
                "error": "API key missing. Please add PERPLEXITY_API_KEY in Render environment variables.",
                "status": "error"
            }), 400
        
        # Perplexity API call
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": [
                {
                    "role": "system",
                    "content": "You are an expert AI coding assistant. Help with programming, debugging, tutorials, exam preparation (NTPC, Group D), and technical questions. Respond in Hindi and English mix when appropriate."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }
        
        response = requests.post(PERPLEXITY_API_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({
                "response": result['choices'][0]['message']['content'],
                "status": "success",
                "model": result.get('model', 'unknown')
            })
        else:
            error_msg = f"Perplexity API error: {response.status_code}"
            if response.text:
                error_msg += f" - {response.text}"
            return jsonify({
                "error": error_msg,
                "status": "error"
            }), 500
            
    except requests.exceptions.Timeout:
        return jsonify({
            "error": "Request timeout. Please try again.",
            "status": "error"
        }), 504
    except Exception as e:
        return jsonify({
            "error": f"Server error: {str(e)}",
            "status": "error"
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "message": "AI Assistant API is running!",
        "version": "1.0",
        "api_configured": bool(PERPLEXITY_API_KEY)
    })

@app.route('/api/status', methods=['GET'])
def status():
    """Check API configuration status"""
    return jsonify({
        "api_key_configured": bool(PERPLEXITY_API_KEY),
        "status": "connected" if PERPLEXITY_API_KEY else "not_configured"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)