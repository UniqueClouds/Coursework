import math
import pickle
import argparse
from tqdm import tqdm

def get_ground_truth(gt_path):
    gt_dict = pickle.load(open(gt_path, 'rb'))
    return gt_dict

def time_score(t):
    T = 0.26128693103790285 / math.log(1/0.2020)
    return math.exp(-t/T)

def score_time_f1(f1, t):
    t_score = time_score(t)
    score = t_score * 0.5 + f1 * 0.5
    return score

parser = argparse.ArgumentParser()
parser.description='please enter two parameters a and b ...'
parser.add_argument("-so", "--submission_search_path", help="this is the submission search file path", type=str, default="./submissions/output.csv")
parser.add_argument("-st", "--submission_time_path", help="this is the submission time file path", type=str, default="./submissions/total_time.pkl")
parser.add_argument("-l", "--target_path", help="this is the target path", type=str, default="./test_a/labels_500.pkl")
parser.add_argument("-q", "--query_number", help="this is the query_number", type=int, default=500)
args = parser.parse_args()

submission_path = args.submission_search_path
target_path = args.target_path
query_number = args.query_number

result_reader = open(submission_path)
labels = pickle.load(open(target_path, 'rb'))

indices = {"P": []}

for data_line in tqdm(result_reader):
    data_line = list(map(int, data_line.rstrip("\n").split(",")))
    ind, topks = data_line[0], data_line[1:]
    targets = labels[ind]
    
    hit = 0
    for jnd in topks:
        if jnd in targets:
            hit += 1
    precision = hit / len(topks)
        
    indices['P'].append(precision)
    
print("Precision: ", sum(indices['P']) / query_number)

total_time = pickle.load(open(args.submission_time_path, 'rb'))
average_time = sum(total_time) / len(total_time)
print("Average time: ", average_time)

score = score_time_f1(sum(indices['P']) / query_number, average_time)
print("Score: ", score)