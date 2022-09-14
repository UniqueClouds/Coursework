import pickle
import argparse
from tqdm import tqdm

def get_ground_truth(gt_path):
    gt_dict = pickle.load(open(gt_path, 'rb'))
    return gt_dict

parser = argparse.ArgumentParser()
parser.description='please enter two parameters a and b ...'
parser.add_argument("-so", "--submission_search_path", help="this is the submission search file path", type=str, default="./submissions/output.csv")
parser.add_argument("-st", "--submission_time_path", help="this is the submission time file path", type=str, default="./submissions/total_time.pkl")
parser.add_argument("-l", "--target_path", help="this is the target path", type=str, default="./test_b/labels_500.pkl")
parser.add_argument("-q", "--query_number", help="this is the query_number", type=int, default=0)
args = parser.parse_args()

submission_path = args.submission_path
target_path = args.target_path
query_number = args.query_number

result_reader = open(submission_path) 
labels = pickle.load(open(target_path, 'rb'))

indices = {"P": [],
           "R": [],
           "F": []}

for data_line in tqdm(result_reader):
    data_line = list(map(int, data_line.rstrip("\n").split(",")))
    # print(data_line)
    ind, topks = data_line[0], data_line[1:]
    targets = labels[ind]
    
    hit = 0
    for jnd in topks:
        if jnd in targets:
            hit += 1
    precision = hit / len(topks)
    recall = hit / len(targets)
    try:
        f1 = 2 * precision * recall / (precision + recall)
    except:
        f1 = 0.0
        
    indices['P'].append(precision)
    indices['R'].append(recall)
    indices['F'].append(f1)
    
print("Precision: ", sum(indices['P']) / query_number)
print("Recall: ", sum(indices['R']) / query_number)
print("F1: ", sum(indices['F']) / query_number)