Prompt_Template = """You are an intelligent assistant. You are given a document and a question. 
Answer the question based **only on the document content**. 
If the document does not contain the information needed to answer the question, respond with:
**"The document does not contain information relevant to your question."**

Document:{document_text}

Question:{user_question}

Answer:
"""