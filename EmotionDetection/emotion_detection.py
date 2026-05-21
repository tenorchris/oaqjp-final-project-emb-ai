#Import the requests library to handle HTTP requests
import requests
#Import the json library to format the HTTP responses
import json

#Define a function to run emotion detection
def emotion_detector(text_to_analyze):
    #URL of the emotion detector analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    #Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #Send a POST request to the API with the text and headers
    response = requests.post(url,json=myobj,headers=header)
    #Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    #Extracting emotion scores from the response
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    #Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    #Return the response text from the API
    return {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
