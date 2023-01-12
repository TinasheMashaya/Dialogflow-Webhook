# from flask import Flask
from flask import Flask, request
import openai

# Replace YOUR_API_KEY with your OpenAI API key
openai.api_key = "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"
# Set the model and prompt
model_engine = "text-davinci-003"
server = Flask(__name__)

@server.route("/status")
def hello():
    return "This is the bot server"

@server.route("/chat",methods=['POST'])
def bot():
    req = request.get_json(silent=True, force=True)
    query_result = req.get('queryResult').get("queryText")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=query_result,
        max_tokens=800,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    
    print(query_result)
    response = completion.choices[0].text
    print(response)
    
    return {
        "fulfillmentText": response,
        "displayText": '15',
        "source": "webhookdata"
    }

if __name__ == "__main__":
   server.run(debug=True ,port=8282)