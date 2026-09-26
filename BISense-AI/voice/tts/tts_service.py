from gtts import gTTS
def synthesize(text,output_path,language='en'): gTTS(text=text,lang=language).save(output_path); return output_path
