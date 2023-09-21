import openai
import os

openai.api_key='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';
openai.api_base='https://api.openai.com/v1'

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    message = [{"role":"user","content":"hello."}]
)

print(completion.choices[0].message)