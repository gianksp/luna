# LUNA Readme

### Prerequisites
    1. Download a vosk speech recognition model into `model/` from [alphacephei](https://alphacephei.com/vosk/models)

### Instructions 
    1. Install dependencies `pip install --no-cache-dir -r requirements.txt`
    2. Setup `.env`
    3. Setup `config.json`
    3. Run `python src/service.py`

### Env vars
```
OPENAI_API_KEY=sk-proj-openaikey
VOSK_MODEL=vosk-model-small-en-us-0.15
```