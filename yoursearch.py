import time
import numpy as np

def searchfunction(query_embeddings, gallery_embeddings):
    K = 10
    all_result = []
    for query_embedding in query_embeddings:
        dist_jnds = []
        for jnd, gallery_embedding in enumerate(gallery_embeddings):
            dist = np.linalg.norm(query_embedding - gallery_embedding)
            dist_jnds.append((dist, jnd))
        topk_rank_list = list(map(lambda x:x[1], sorted(dist_jnds, key=lambda x: x[0])[:K]))
        all_result.append(topk_rank_list)
    return all_result