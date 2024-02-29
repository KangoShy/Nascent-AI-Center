import sys

import chromadb

if __name__ == '__main__':
    # sys.path.append("D:/anaconda3/envs/AICenter/lib/site-packages")
    # setup Chroma in-memory, for easy prototyping. Can add persistence easily!

    client = chromadb.Client()

    # Create collection. get_collection, get_or_create_collection, delete_collection also available!
    collection = client.create_collection("all-my-documents")

    # Add docs to the collection. Can also update and delete. Row-based API coming soon!
    # 若在add方法没有传入embedding参数，则会使用Chroma默认的all-MiniLM-L6-v2 方式进行embedding
    collection.add(
        documents=["我喜欢吃面条", "我喜欢游泳", "我喜欢画画", "我叫张三", "我今年刚满18岁"],
        # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own
        # embeddings as well
        metadatas=[{"source": "doc1"}, {"source": "doc2"}, {"source": "doc3"},
                   {"source": "doc4"}, {"source": "doc6"}],  # filter on these!
        ids=["id1", "id2", "id3", "id4", "id6"],  # unique for each doc
    )

    results = collection.query(
        query_texts=["你的爱好是什么？"],
        n_results=3
    )

    for coll in client.list_collections():
        print(coll)

    print(results)

# if __name__ == '__main__':
#     for x in str(sys.path).split(","):
#         print(x)
