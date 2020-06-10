import jieba
import jieba.analyse
import random
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")
src= input("input your sentence here")
src_list=src.split('，')
src_temp = src.strip()
re = jieba.analyse.extract_tags(sentence=src_temp,topK=1,allowPOS=('ns','n'))
n1= str(re[0])
f=open("3.txt","r")
words3=f.read().splitlines()
f.close
words_3=words3[random.randrange(0,len(words3))]
src_list.insert(1,"我是说"+n1+words_3)
src_temp="，".join(src_list)
f=open("1.txt","r")
words1=f.read().splitlines()
f.close
words_1=words1[random.randrange(0,len(words1))]
f=open("2.txt","r")
words2=f.read().splitlines()
f.close
words_2=words2[random.randrange(0,len(words2))]

print(words_1+src_temp+words_2)

