# LUNA Readme

### Prerequisites
    1. Download a vosk speech recognition model into `model/` from [alphacephei](https://alphacephei.com/vosk/models). The model also needs to be specified in config file under `speech-to-text-model` and must be exclusive from vosk.

### Instructions 
    1. Install dependencies `pip install --no-cache-dir -r requirements.txt`
    2. Setup `.env`
    3. Setup `config.json`
    3. Run `python src/service.py`

### Env vars
```
OPENAI_API_KEY=sk-proj-openaikey
```