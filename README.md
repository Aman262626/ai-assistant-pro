# 🚀 AI Assistant Pro - Perplexity Powered

**Complete full-stack AI chatbot** with Flask backend and modern 3D UI.

![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![Perplexity](https://img.shields.io/badge/AI-Perplexity-20b8c6)

## 🌐 Live Demo

**Website**: [https://ai-assistant-pro-cusz.onrender.com](https://ai-assistant-pro-cusz.onrender.com)

## ✨ Features

### 🤖 AI Capabilities
- **Perplexity API Integration** - Latest Llama 3.1 Sonar model
- **Online Search** - Real-time web search capabilities
- **Code Assistance** - Debug, explain, and write code
- **Exam Preparation** - NTPC, Group D study help
- **Hindi + English** - Bilingual support

### 🎨 Modern UI
- **3D Effects** - Smooth animations and glassmorphism
- **Dark Theme** - Eye-friendly dark interface
- **Responsive Design** - Works on all devices
- **Quick Shortcuts** - One-click prompts for common tasks

### ⚡ Quick Actions
- 🐍 REST API Tutorial
- 🐛 Debug Code
- ⚛️ Full Stack Development
- 📚 Learn DSA
- 🎯 Exam Prep

## 🚀 Deployment on Render

### Prerequisites
- GitHub account
- Render account ([render.com](https://render.com))
- Perplexity API key ([perplexity.ai](https://www.perplexity.ai))

### Step 1: Get Perplexity API Key

1. Visit [Perplexity AI](https://www.perplexity.ai)
2. Sign up / Login
3. Go to API section
4. Generate new API key
5. Copy the key (starts with `pplx-`)

### Step 2: Deploy on Render

1. **Login to Render**
   - Go to [render.com](https://render.com)
   - Sign in with GitHub

2. **Create New Web Service**
   - Click **"New +"** button
   - Select **"Web Service"**
   - Connect this repository: `Aman262626/ai-assistant-pro`

3. **Configure Settings**
   ```
   Name: ai-assistant-api (or any unique name)
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   Plan: Free
   ```

4. **Add Environment Variable**
   - Go to **Environment** tab
   - Click **"Add Environment Variable"**
   - Add:
     ```
     Key: PERPLEXITY_API_KEY
     Value: pplx-your-actual-api-key-here
     ```

5. **Deploy**
   - Click **"Create Web Service"**
   - Wait 3-5 minutes for deployment
   - Your site will be live at: `https://your-app-name.onrender.com`

### Step 3: Test Your Deployment

1. Open your Render URL
2. You should see **"✓ Connected & Ready"** status
3. Type a message and click Send
4. AI should respond within seconds!

## 📁 Project Structure

```
ai-assistant-pro/
├── app.py              # Flask backend with Perplexity API
├── index.html          # Frontend UI (auto-configured)
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔧 API Endpoints

### `GET /`
Serves the main HTML interface

### `POST /api/chat`
Send messages to AI

**Request:**
```json
{
  "message": "Python me REST API kaise banaye?"
}
```

**Response:**
```json
{
  "response": "AI response here...",
  "status": "success",
  "model": "llama-3.1-sonar-small-128k-online"
}
```

### `GET /health`
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "message": "AI Assistant API is running!",
  "api_configured": true
}
```

### `GET /api/status`
Check API configuration

**Response:**
```json
{
  "api_key_configured": true,
  "status": "connected"
}
```

## 🧪 Local Development

### 1. Clone Repository
```bash
git clone https://github.com/Aman262626/ai-assistant-pro.git
cd ai-assistant-pro
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variable
```bash
# On Windows (CMD):
set PERPLEXITY_API_KEY=pplx-your-key-here

# On Windows (PowerShell):
$env:PERPLEXITY_API_KEY="pplx-your-key-here"

# On Mac/Linux:
export PERPLEXITY_API_KEY="pplx-your-key-here"
```

### 5. Run Application
```bash
python app.py
```

### 6. Open Browser
```
http://localhost:5000
```

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Gunicorn** - Production WSGI server
- **Requests** - HTTP library

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with animations
- **JavaScript** - Interactive functionality
- **Fetch API** - Async communication

### AI
- **Perplexity API** - AI model provider
- **Llama 3.1 Sonar** - Language model
- **Online Search** - Real-time web access

### Deployment
- **Render** - Cloud hosting platform
- **GitHub** - Version control
- **Environment Variables** - Secure config

## 📝 Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|----------|
| `PERPLEXITY_API_KEY` | Your Perplexity API key | Yes | None |
| `PORT` | Server port (auto-set by Render) | No | 5000 |

## 🔒 Security Features

✅ **API Key Protection** - Keys stored in environment variables  
✅ **CORS Configured** - Prevents unauthorized access  
✅ **Input Validation** - Sanitizes user input  
✅ **Error Handling** - Graceful error messages  
✅ **No Hardcoded Secrets** - All sensitive data in env vars  

## ⚠️ Important Notes

### Free Tier Limitations (Render)
- Service sleeps after **15 minutes** of inactivity
- First request may take **30-50 seconds** (cold start)
- **750 hours/month** free (sufficient for 1 website)
- Automatic wake-up on incoming requests

### API Usage
- Perplexity API has rate limits
- Monitor your usage in Perplexity dashboard
- Free tier available for testing

### Best Practices
- Never commit `.env` files
- Rotate API keys regularly
- Monitor error logs in Render dashboard
- Keep dependencies updated

## 🐛 Troubleshooting

### Problem: "API key missing" error
**Solution:**  
Check that `PERPLEXITY_API_KEY` is set correctly in Render Environment Variables.

### Problem: Slow first response
**Solution:**  
This is normal for Render free tier. Service wakes up from sleep mode (takes 30-50 seconds).

### Problem: "Connection error"
**Solution:**  
1. Check if backend is deployed and running
2. Visit `/health` endpoint to verify: `https://your-app.onrender.com/health`
3. Check Render logs for errors

### Problem: Deployment failed
**Solution:**  
1. Check Render build logs
2. Verify `requirements.txt` has correct package versions
3. Ensure Python 3.9+ is specified

## 📱 Browser Support

✅ Chrome 90+  
✅ Firefox 88+  
✅ Safari 14+  
✅ Edge 90+  
✅ Mobile browsers (iOS Safari, Chrome Mobile)  

## 🎯 Use Cases

- **Coding Help** - Debug code, explain concepts, write functions
- **Learning** - Tutorials on Python, JavaScript, DSA, etc.
- **Exam Prep** - NTPC, Group D, RRB preparation
- **Project Ideas** - Get suggestions for projects
- **Quick Answers** - Technical questions answered instantly

## 📄 License

MIT License - Free to use, modify, and distribute!

## 👤 Author

**Aman**  
GitHub: [@Aman262626](https://github.com/Aman262626)  
Location: Gorakhpur, Uttar Pradesh, India  

## 🙏 Acknowledgments

- [Perplexity AI](https://www.perplexity.ai) - AI API provider
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Render](https://render.com) - Hosting platform
- Community contributors

## 🚀 Future Enhancements

- [ ] Image generation (DALL-E integration)
- [ ] Voice input/output
- [ ] File upload analysis
- [ ] Chat history with database
- [ ] User authentication
- [ ] Multi-language UI
- [ ] Real-time streaming responses
- [ ] Code execution sandbox

## 📞 Support

For issues or questions:
1. Open an issue on [GitHub](https://github.com/Aman262626/ai-assistant-pro/issues)
2. Check existing issues first
3. Provide detailed error messages
4. Include screenshots if applicable

---

**⭐ Star this repo if you find it helpful!**

**Happy Coding! 🎉**