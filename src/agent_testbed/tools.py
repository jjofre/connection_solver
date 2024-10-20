from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "extract words from the image and return as a json structure"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/png;base64,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QAACEAieQHHwjwjPE9avX5+QmVo+zjkoKytTy5Z9r7bbbhtVVORd5/7uu+9V3bp1VaNGGyfkwdwk5824J1/95Dk5De5rnoCX+nXWbXJ4p1+63CfHSRXOmU624VOlh1thEfjrr7/Ud9/9oLbZZitVXJy6+Tdy4ZQVL6X0Es+EcaaX7XOccbHnn0CqOk3OVao6NvFS+Zn4Joy5l2um8OLvjJNNWImbyrilkSpOlN1StxoRLHHfvqeqGTNeqFKyhg03VI0bb6b226+TGjCgn2rVavcqYUQI77nnATVhwgNq/vyFau3atapevXqqZcvd1EUXDVMHHLBflTji8NVX36hLLrlSvfHGXPXjjz/pMNttt63q3r2Luvji4WrDDTfUbg899Jg666xh2u72Z/Toq9XAgf3cguEfIgKtW++jlixZ6pojkcPPP39f+ZHVdHGSH/rDD4tV7dq10z4jXfhkd+4Li8Add4xXEyc+asnXAt1+lZTUUfvs00H9+9+XqV133cUujFOOzjprsLrsspG2XybLwIGnq6efnqyDiHzNm/eu2myzTROifPDBR+rgg3sluMmNKK9bb72l2mWX5urUU09R3bod4qoYVEkEh7wQyLZtM5msjryI7G622WaqefOdVZ8+x6jevY+15SVZxpYsma/f1ea5zqtT1p3uyXbTZia7x/Xe+1BZRAn9/vsfatGir9T99z+kevY8Wr355lsJJZWRxaOPPlFdcMFI9emnn+kGVwKsWrVKvfXWO+rYY09SV1zxn4Q4cjNlynRLEe2qnn12mq0wivs33yxRd989QfstXPiFOGEg4ImAm6x6SoRAsSLw559/qn79BqkRIy5Tn3wyz26/ysrWqFmzXlUHHthDvfLK7GoxWb16tXruuRftNNatW6fbP9vBxSKd8K+/XqKef36m7sxcddVolxh4FzKB6sqLyO6yZd9puT399HPVkCHnFTKOgst7bEYanTXTpctB6qijDlcivO+++75u4H799TetCJ5++jnqnXdes4PfeOOtavbsinuZXj777NPVTjvtqBvcBx54WA+FS5hDDjlIdeq0j47388+/qHPPHa6kwRbTufO+6sQTj1O//fa7uvPOe7SSKo3ksGEj1KRJj6oddyy1Gva+Oqz8ef31uWrBgoX6vrS0maVg7qvt8qdFi51tO5bCIHDssUcqkQkx0tl4/PGn7Iwf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"
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "```json\n{\n  \"words\": [\n    \"PONY\",\n    \"ROLL\",\n    \"COMB\",\n    \"BOOK\",\n    \"ROOT\",\n    \"TREE\",\n    \"CLAP\",\n    \"TABLE\",\n    \"BUN\",\n    \"SALAD\",\n    \"DIG\",\n    \"RUMBLE\",\n    \"SIFT\",\n    \"TWIST\",\n    \"PEAL\",\n    \"BRAID\"\n  ]\n}\n```"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "extract words from image and return as json structure"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "\n{\"words\":[\"PONY\",\"ROLL\",\"COMB\",\"BOOK\",\"ROOT\",\"TREE\",\"CLAP\",\"TABLE\",\"BUN\",\"SALAD\",\"DIG\",\"RUMBLE\",\"SIFT\",\"TWIST\",\"PEAL\",\"BRAID\"]}"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "json_object"
  }
)

import json
from langchain.llms import OpenAI

# Initialize the OpenAI LLM with your API key
openai_api_key = "your-openai-api-key"
llm = OpenAI(api_key=openai_api_key, model="gpt-4o")

# JSON structure from the active file
data = [
    {
        "type": "text",
        "text": "extract words from the image and return as a json structure"
    },
    {
        "type": "image_url",
        "image_url": {
            "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAo0AAAGACAYAAADI21gOAAABW2lDQ1BJQ0MgUHJvZmlsZQAAKJFjYGBiSSwoyGFhYGDIzSspCnJ3UoiIjFJgf8HAxcDHwMOgxqCVmFxc4BgQ4ANUwgCjUcG3awyMIPqyLsisdan52zOW8Ca8FJS4077483dM9SiAKyW1OBlI/wFireSCohIGBkYNIDugvKQAxK4AskWKgI4CsntA7HQIewGInQRhbwGrCQlyBrJPANkCyRmJKUD2DSBbJwlJPB2JnZtTmgx1A8j1PKl5ocFAmg+IZRg8GAIYFBiMGIwZUhmKgGGDXa0JWK0zQz5DAUMlUF0mQzpDBkMJUKcjUKSAIQeoW4HBkyGPIZlBj0EHbKIBEJuAwhg97BBiGfYMDGY"
        }
    }
]

# Extract the base64 image data from the JSON structure
image_data = data[1]["image_url"]["url"]

# Create the prompt for the LLM
prompt = f"Extract words from the image and return as a JSON structure. Image data: {image_data}"

# Invoke the LLM
response = llm(prompt)

# Print the response
print(response)