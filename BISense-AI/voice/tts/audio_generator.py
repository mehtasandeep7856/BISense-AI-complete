from voice.tts.tts_service import synthesize
def generate_audio(text,output_path,language='en'): return synthesize(text,output_path,language)
