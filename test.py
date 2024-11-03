# import marqo

# mq = marqo.Client(url='http://localhost:8882')


# mq.index("my-first-index").add_documents([
#     {
#         "Title": "The Travels of Marco Polo",
#         "Description": "A 13th-century travelogue describing Polo's travels"
#     }, 
#     {
#         "Title": "Extravehicular Mobility Unit (EMU)",
#         "Description": "The EMU is a spacesuit that provides environmental protection, "
#                        "mobility, life support, and communications for astronauts",
#         "_id": "article_591"
#     }],
#     # tensor_fields=["Description"]
# )

# results = mq.index("my-first-index").search(
#     q="What is the best outfit to wear on the moon?"
# )


import json
import os
from marqo import Client

# Initialize the Marqo client
client = Client(url="http://localhost:8882")  # Replace with your Marqo instance URL

# Define the index name
INDEX = "nepali_legal_documents"

# conf = {
#     "model":"BAAI/bge-m3",
#     "treatUrlsAndPointersAsImages":False,
#     "normalizeEmbeddings":True
# }

settings = {
    # "treatUrlsAndPointersAsImages": True,
    "model": "bge-m3",
    "modelProperties": {
        "name": "BAAI/bge-m3",
        "dimensions": 1024,
        "type": "hf",
    },
    # "type": "structured",
    "normalizeEmbeddings": True,
    # "all_fields": [{"name": "my_custom_vector", "type": "custom_vector"}],
    # "tensor_fields": ["my_custom_vector"],
}


# client.create_index(
#     INDEX,
#     index_settings={
#         'index_defaults': {
#             'model': 'custom',
#             'treat_urls_and_pointers_as_images': False,
#             'normalize_embeddings': True,
#         }
#     }
# )

# client.index(INDEX).update_settings(
#     index_settings={
#         'index_defaults': {
#             'model': 'custom',
#             'treat_urls_and_pointers_as_images': False,
#             'normalize_embeddings': True,
#         }
#     }
# )



# Create the index with the model and settings directly
# response = client.create_index(
#     index_name=f"{INDEX}",
#     settings_dict=settings,
# )

# Load the documents from the JSON file
# with open('output_split_1.json', 'r') as f:
#     documents = json.load(f)  # Load the entire JSON as a list of dictionaries

# load txt files in list from output_folder
documents = []
files = os.walk('output_folder/')

for f in files:
    for file in f[2]:
        if file.endswith('.txt'):
            file_path = f[0] + '/' + file
            with open(file_path, 'r') as file_handle:
                content = file_handle.read().replace('\n', ' ')  # Remove newlines
                documents.append(
                    dict(
                        c=content,
                        t=file
                    )
                )

# Add all documents to the Marqo index at once
print(client.index(INDEX).add_documents(
    documents=documents,
    # mappings={"my_custom_vector": {"type": "custom_vector"}},
    # use_existing_tensors=True,
    # client_batch_size=50,
    tensor_fields=["c", "t"],
    ))

print("All documents have been added to the Marqo index.")
