import time
import numpy as np

def searchfunction(query_embeddings, gallery_embeddings):
    """
    Args:
        query_embeddings: (N, 512) 所有待查询的图片的embedding
        gallery_embeddings: (M, 512) 大规模向量库的所有图片的embedding
    Returns:
        所有待查询的图片的最相似的K=10个图片向量的index, 例如[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    K = 10
    search_result = []
    for query_embedding in query_embeddings:
        dist_jnds = []
        for jnd, gallery_embedding in enumerate(gallery_embeddings):
            dist = np.linalg.norm(query_embedding - gallery_embedding)
            dist_jnds.append((dist, jnd))
        topk_rank_list = list(map(lambda x:x[1], sorted(dist_jnds, key=lambda x: x[0])[:K]))
        search_result.append(topk_rank_list)
    return search_result