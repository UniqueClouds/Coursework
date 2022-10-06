# 2022 Data Mining Big Jobs

## Problem Description

With the development of storage and communication technology, large-scale image data retrieval has become an urgent problem to be solved. In practical applications, image data is often converted into high-dimensional vectors by an image encoder, so the retrieval task of large-scale image data is transformed into the indexing problem of high-dimensional vectors. This project focuses on the **search of high-dimensional vectors** (Embedding dimension of this project is 512) and does not consider the image encoding part, so students only need to complete the retrieval task of the query vector provided by us in the large-scale vector library.

<!-- <center>![problem defination](https://github.com/lzzppp/Coursework/blob/main/irproject.png)<center> -->
<div  align="center">
    <img src="https://github.com/lzzppp/Coursework/blob/main/irproject.png" height=457 width=419 alt="图片名称" align=center />
</div>

## Data and File Format

├── submissions  
│   ├── output.csv   
├── test\_b  
│   ├── gallery\_emb.npy  
│   ├── labels\_5000.pkl  
│   └── query\_emb.npy  
├── test\_a    
│   ├── gallery\_emb.npy  
│   ├── labels\_500.pkl  
│   └── query\_emb.npy  
├── evaluation.py    
├── run.sh  
├── search.py  
└── Readme.md

- test\_a (query: 500; gallery:500,000) and test\_b (query: 5000; gallery:5,000,000) have the same file structure. We will initially provide a smaller dataset test\_a for students to debug the search algorithm (query\_emb.npy is the query embeddings; gallery\_emb.npy is the embeddings to be queried; label\_500.pkl is the 10 indexes that belong to the same group in gallery_emb.npy for each query embedding.), and give the running code sample **search.py** and test code **evaluation.py**.  
- You only need to submit **the modified search.py** code to 12221073@zju.edu.cn, and we will comprehensively measure **the query time** and **P@10** indicators to give the score of this project.

test_a data download link: https://pan.baidu.com/s/1jKLpwpE1vVodaDTsq2WL7A?pwd=tgi7 code: tgi7

## Evaluation indicators
Efficiency: We count the average time per query, the faster the better.

Effectiveness: For the top-10 search for each query given by the algorithm, we will calculate the precision (P@10). The higher the precision, the better.

<div  align="center">
    <img src="https://github.com/lzzppp/Coursework/blob/main/precision.png" height=180 width=419 alt="图片名称" align=center />
</div>

Final Rank: We will rank submissions based on the efficiency and effectiveness of the search algorithm submitted.

## Runing Demo

    python search.py -q ./test_a/query_emb.npy -g ./test_a/gallery_emb.npy -o ./submissions/output.csv 

> -q : The path of all query embeddings 
> 
> -g : The path of all gallery embeddings
> 
> -so : The path that stores the search result of all queries
> 
> -st : The path that stores the total time of all queries



