from copyreg import pickle
import time
import argparse
import numpy as np
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.description='please enter two parameters a and b ...'
parser.add_argument("-q", "--query_emb_path", help="this is the query embeddings path", type=str, default="query_emb.npy")
parser.add_argument("-g", "--gallery_emb_path", help="this is the gallery embeddings path", type=str, default="gallery_emb.npy")
parser.add_argument("-o", "--output_path", help="this is the output file path", type=str, default="./submissions/output.csv")
args = parser.parse_args()

K = 10
csv_writer = open(args.output_path, 'w')
query_embeddings = np.load(args.query_emb_path)
gallery_embeddings = np.load(args.gallery_emb_path)

total_time = []
for ind, query_embedding in enumerate(tqdm(query_embeddings)):
    start_time = time.time()
    ''' ⭐ ⭐ ⭐ ⬇ ⬇ ⬇ search part; your can replace here with any method to search ⬇ ⬇ ⬇ ⭐ ⭐ ⭐ '''
    dist_jnds = []
    for jnd, gallery_embedding in enumerate(gallery_embeddings):
        dist = np.linalg.norm(query_embedding - gallery_embedding)
        dist_jnds.append((dist, jnd))
    topk_rank_list = list(map(lambda x:x[1], sorted(dist_jnds, key=lambda x: x[0])[:K]))
    ''' ⭐ ⭐ ⭐ ⬆ ⬆ ⬆ search part; your can replace here with any method to search ⬆ ⬆ ⬆ ⭐ ⭐ ⭐ '''
    end_time = time.time()
    total_time.append(end_time - start_time)
    csv_writer.write(str(ind) + "," + ",".join(list(map(str, topk_rank_list))) + "\n")
    
pickle.dump(total_time, open("./submissions/total_time.pkl", "wb"))