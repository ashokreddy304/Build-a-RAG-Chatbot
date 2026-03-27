from openai import OpenAI

text_chunks = ["The sky is blue.", "The grass is green."]

client = OpenAI()  # uses the environment variable OPENAI_API_KEY

embeddings_list = []

for text_chunk in text_chunks:
    response = client.embeddings.create(input=[text_chunk], model="text-embedding-3-small")
    embedding = response.data[0].embedding
    embeddings_list.append(embedding)

print(len(embeddings_list[0]))