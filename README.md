# MapReduce

 1. Introduction:
The assignment tasked the development of a basic search engine utilizing MapReduce technology. It comprised preprocessing a significant dataset of Wikipedia articles, indexing the articles using MapReduce, and implementing a query processing system.

2. Preprocessing Phase:

    Objective: The preprocessing phase aimed to clean and organize the Wikipedia dataset to prepare it for indexing.
    Approach: Python's Pandas library facilitated reading the dataset, extracting relevant columns (ARTICLE_ID and SECTION_TEXT), and cleaning the text by removing special characters and converting it to lowercase.
    Implementation: Separate mapper and reducer scripts were developed to execute the preprocessing tasks in a distributed manner using Hadoop Streaming. The mapper cleaned the text segments and emitted key-value pairs, while the reducer concatenated the cleaned text segments for each ARTICLE_ID.

3. Indexing Phase:

    Objective: The indexing phase involved creating an inverted index of the preprocessed Wikipedia articles to enable efficient querying.
    Approach: The MapReduce paradigm was employed to distribute the indexing tasks across multiple nodes, facilitating parallel processing.
    Implementation: Word Enumeration and Document Count tasks were implemented using distinct mapper and reducer scripts. The mapper tokenized the text and emitted word-document pairs, while the reducer aggregated these pairs to generate the inverted index.

4. Query Processing:

    Objective: Query processing aimed to retrieve relevant articles based on user queries using the inverted index generated during the indexing phase.
    Approach: Queries were tokenized and vectorized using the TF/IDF Vector Space Model. The cosine similarity between the query vector and document vectors was calculated to rank the articles.
    Implementation: A query processing module was developed to tokenize queries, calculate TF/IDF weights, and compute cosine similarity scores. MapReduce was leveraged to parallelize the relevance analysis process.

5. Vector Space Model:

    Objective: The Vector Space Model represented documents and queries as vectors to measure their similarity efficiently.
    Approach: Each document and query were represented as sparse vectors, with each dimension corresponding to a term in the vocabulary.
    Implementation: Python scripts were crafted to convert text into vector representations, calculate TF/IDF weights, and compute cosine similarity scores using MapReduce.

6. Conclusion:
The assignment demonstrated the creation of a basic search engine utilizing MapReduce technology. By harnessing distributed processing and the MapReduce paradigm, the search engine efficiently indexed large datasets and retrieved relevant results for user queries. Potential future enhancements could include integrating additional relevance ranking algorithms and optimizing the system for further scalability and performance gains.
