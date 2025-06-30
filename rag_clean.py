def rag_implementation(Path,Model):
    

    model = Model #Model name to use for RAG
    #Loading the PDF file
    from langchain_community.document_loaders import UnstructuredPDFLoader


    path = Path #Path to your PDF file
    # ==== PDF Ingestion ====
    # This will load the PDF file and convert it into a list of documents.

    loader = UnstructuredPDFLoader(file_path = path)
    data = loader.load()
    print("done loading....")
    # Preview first page
    content = data[0].page_content
    print(content[:100])

    # ==== End of PDF Ingestion ====

    # ==== Extract Text from PDF Files and Split into Small Chunks ====
    from langchain_ollama import OllamaEmbeddings
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.vectorstores import Chroma

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300) #Chunk overlap means how much releance of the document in used by LLM to answer
    chunks = text_splitter.split_documents(data)
    print("done splitting....")

    # print(f"Number of chunks: {len(chunks)}")
    # print(f"Example chunk: {chunks[0]}")


    # ===== Add to vector database ===
    import ollama

    ollama.pull("nomic-embed-text")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model="nomic-embed-text"),
        collection_name="simple-rag",
    )
    print("done adding to vector database....")


    ## === Retrieval ===
    from langchain.prompts import ChatPromptTemplate, PromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    from langchain_ollama import ChatOllama

    from langchain_core.runnables import RunnablePassthrough
    from langchain.retrievers.multi_query import MultiQueryRetriever


    # set up our model to use
    llm = ChatOllama(model=model)

    # a simple technique to generate multiple questions from a single question and then retrieve documents
    # based on those questions, getting the best of both worlds.
    QUERY_PROMPT = PromptTemplate(
        input_variables=["question"],
        template="""You are an AI language model assistant. Your task is to generate five
        different versions of the given user question to retrieve relevant documents from
        a vector database. By generating multiple perspectives on the user question, your
        goal is to help the user overcome some of the limitations of the distance-based
        similarity search. Provide these alternative questions separated by newlines.
        Original question: {question}""",
    )

    retriever = MultiQueryRetriever.from_llm(
        vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
    )

    # RAG prompt
    template = """Answer the question based ONLY on the following context:
    {context}
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"context":retriever, "question":RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    while(1):
        query = input("Enter your message (type 'exit' to quit):  ")
        
        if query == "exit" :
            break

        res = chain.invoke(input = (query))
        print(res)

