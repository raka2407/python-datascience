from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pandas import json_normalize

url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/13134e2c-ba8a-49dd-9c53-b92ad967bd28"
iam_apikey_s2t = "SFv8rVkUpx66H-h8gqc9UIFUV0XWE2AOwbLmzflghEFq"

# Create Speech to Text Adapter Objects using endpoint URL and API Key
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)

#Download the audio file using the command below 
# wget -O PolynomialRegressionandPipelines.mp3  https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3

filename = 'PolynomialRegressionandPipelines.mp3'

# Read the file in binary mode (rb) and send to the service using s2t object created above

with open(filename, 'rb') as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')  # response is a dictionary including translation

json_normalize(response.result['results'],"alternatives")
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
print(recognized_text)
