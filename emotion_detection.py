from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

'''
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)
    return response.text

# Example usage
if __name__ == "__main__":
    text = "I love this new technology."
    result = emotion_detector(text)
    print(result)


'''
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)
    return response.json()  # Return JSON response

@app.route('/analyze-emotion', methods=['POST'])
def analyze_emotion():
    data = request.json
    text = data.get('text')
    
    if text:
        result = emotion_detector(text)
        return jsonify(result)
    else:
        return jsonify({"error": "No text provided for analysis."})

if __name__ == "__main__":
    app.run(debug=True)
