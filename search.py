
from marqo import Client

# Initialize the Marqo client
client = Client(url="http://localhost:8882")  # Replace with your Marqo instance URL

# Define the index name
INDEX = "nepali_legal_documents"

def search_db(query):
    return client.index(INDEX).search(query)

q= "what can you tell me about insuring mail packages"

# results = client.index(INDEX).search(
#     q,
#     # search_method="LEXICAL",
#     # ef_search=200,
#     # show_highlights=True,
#     # attributes_to_retrieve=["_id",]
#     # approximate=True
# )
# print(results['hits'][0].get('c'))


# print(results['hits'][0])

#############################################################
#       STEP 5: Make it chatty
#############################################################

# highlights, texts = extract_text_from_highlights(results, token_limit=150)
# docs = [Document(page_content=f"Source [{ind}]:" + t) for ind, t in enumerate(texts)]
# llm = OpenAI(temperature=0.9)
# chain_qa = LLMChain(llm=llm, prompt=qna_prompt())
# llm_results = chain_qa.invoke({"summaries": docs, "question": results['query']}, return_only_outputs=True)
# print(llm_results['text'])

# #############################################################
# #       STEP 6: Score the references
# #############################################################

# score_threshold = 0.20
# top_k = 3
# scores = predict_ce(llm_results['text'], texts)
# inds = get_sorted_inds(scores)
# scores = scores.cpu().numpy()
# scores = [np.round(s[0], 2) for s in scores]
# references = [(str(np.round(scores[i], 2)), texts[i]) for i in inds[:top_k] if scores[i] > score_threshold]
# df_ref = pd.DataFrame(references, columns=['score', 'sources'])
# print(df_ref)