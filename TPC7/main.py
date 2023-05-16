#!/usr/bin/env python3
import argparse
from glob import glob
from gensim.models import Word2Vec
from gensim.utils import tokenize


parser = argparse.ArgumentParser(
    prog='Cria Modelo', epilog='Made for SPLN 2022/2023')

parser.add_argument("dir")
parser.add_argument('--out', '-o', default='./model')
parser.add_argument('--ephoc', '-e', default=5)
parser.add_argument('--dim', '-d', default=300)

args = parser.parse_args()
dir = args.dir
ephocs = args.ephoc
dim = args.dim
out = args.out

files = glob(f'{dir}/*.txt')

cont = []
for file in files:
    fd = open(file, 'r')
    for line in fd:
        cont.append(list(tokenize(line, lowercase=True)))


model = Word2Vec(cont, epochs=ephocs, vector_size=dim)
model.save(f'{out}.vec')
