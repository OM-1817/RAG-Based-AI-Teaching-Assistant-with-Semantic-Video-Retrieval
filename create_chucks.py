import whisper
import json
import os

model = whisper.load_model("large-v2")

audios=os.listdir("audios")
for audio in audios:
    number=audio.split("_")[0]
    title=audio.split("_")[1][:-4]
    print(number,title)

    result=model.transcribe(audio=f"audios/{audio}",language="hi",task="translate",word_timestamps=False)
    
    
    
    chucks=[]
    for segment in result["segments"]:
        chucks.append({"number":number,"title":title,"start":segment["start"],"end":segment["end"],"text":segment["text"]})
        
    chucks_with_metadata={"chucks":chucks,"text":result["text"]}
    
    with open(f"json/{audio}.json","w") as f:
        json.dump(chucks_with_metadata,f)
