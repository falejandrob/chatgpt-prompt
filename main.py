from openai import OpenAI
client = OpenAI()
prompt = input(f"tell me something about you want to talk")
#stringPrompt =f"Give me some informations about the following topic {prompt}"
stringPrompt =f"Dame algo de informacion sobre el siguiente tema:  {prompt}"
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )
#
# print(completion.choices[0].message)


#Realiza una solicitud a la API de GPT-3
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "user", "content": stringPrompt}
  ]
)



#Imprime la respuesta generada por GPT-3
#print(response.choices[0].message)

with open(prompt+".txt",'w') as archivo:
  archivo.write(str(response.choices[0].message.content))