# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils 
import argparse

argp = argparse.ArgumentParser()
argp.add_argument('--eval_corpus_path', default=None)
args = argp.parse_args()

correct = 0
total = 0
with open(args.eval_corpus_path, encoding='utf-8') as fin:
    lines = [x.strip().split('\t') for x in fin]
    total = len(lines)
preds = ["London"] * total
utils.evaluate_places(args.eval_corpus_path, preds)
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))