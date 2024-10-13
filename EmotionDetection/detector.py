import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=Input_json, headers=Headers)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        emotions = data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        # Formatting the output
        formatted_response = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        
        # Print formatted output
        print("Emotion Scores:")
        for emotion, score in formatted_response.items():
            if emotion != 'dominant_emotion':
                print(f"{emotion.title()}: {score}")
        print("\nDominant Emotion:", formatted_response['dominant_emotion'].title())
        
        return formatted_response  # Optionally return the data if needed elsewhere
    else:
        # Handle other status codes with an appropriate error response
        print(f'Error: Status code {response.status_code}: {response.reason}')
        return None