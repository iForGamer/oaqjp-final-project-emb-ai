import requests
import json

def emotion_detector(text_to_analyze):
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL,json=myobj,headers=Headers)

    if response.status_code == 200:
        formated_response = response.json()
        emotions = formated_response['emotionPredictions'][0]['emotion']
        max_score = max(emotions.values())
        for i in emotions:
            if max_score == emotions[i]:
                emotions["dominant_emotion"]=i
                break
    elif response.status_code == 400:
        emotions = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
        }
    else:
        emotions = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None
        }
    return emotions
