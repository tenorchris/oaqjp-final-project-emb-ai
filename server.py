''' Executing this function initiates the application of the emotion detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_route():
    #Retrieve text
    text_to_analyze = request.args.get('textToAnalyze')
    #Run emotion detection
    response = emotion_detector(text_to_analyze)
    #Extract values
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant = response.get('dominant_emotion')
    #Format exactly as required
    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
        
    ''' This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector_route()
        function. The output returned shows emotion and it's score.
    '''

@app.route("/")
def render_index_page():
    return render_template('index.html')
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
