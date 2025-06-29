from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

creds = Credentials(
    api_key="T6tSFsQAqh2dN_EMQRYVuT6GLwmix6mczkjU8r79cKJA",
    url="https://us-south.ml.cloud.ibm.com"
)

model = ModelInference(
    model_id="ibm/granite-3-2b-instruct",
    credentials=creds,
    project_id="e16e059a-1a6a-4a41-a747-6f52cd47bb71"
)

params = {
    "decoding_method": "greedy",
    "max_new_tokens": 1024
}
