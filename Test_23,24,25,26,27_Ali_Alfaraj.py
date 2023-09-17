#!/usr/bin/env python
# coding: utf-8

# In[1]:


#problem 23 what are the kmers making a given text
import pandas as pd
def Text_to_Kmers(Text,k):
    n= len(Text)
    Kmers=[]
    for i in range(n-k+1):
        Kmers.append(Text[i:i+k])
    return Kmers
answer=Text_to_Kmers('CAATCCAAC',5)
for i in answer:
    print(i)


# In[2]:


# Poblem 24 Kmers to Text

def Kmers_to_Text(Kmers):
    k= len(Kmers[0])
    text=''
    n=len(Kmers)
    for i in range(n):
        if i==0:
            text+=Kmers[i]
        else:
            text+=Kmers[i][-1]
    return text
kmers=['ACCGA',
'CCGAA',
'CGAAG',
'GAAGC',
'AAGCT']

Kmers_to_Text(kmers)


# In[3]:


#25 Overlap Graph
def OverlapGraph(Kmers):
    Graph=[]
    k=len(Kmers[0])
    for i in Kmers:
        for n in Kmers:
            if i!=n and i[:-1]==n[(1-k):]:
                Graph.append(n+' -> '+i)
    return Graph  
kmers=['ATGCG',
'GCATG',
'CATGC',
'AGGCA',
'GGCAT']
a=OverlapGraph(kmers)
for i in a:
    print(i)


# In[4]:


def de_bruijn(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i+k-1], st[i+1:i+k]))
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    left_edges=[]
    right_edges=[]
    Graph=[]
    n=len(edges)
    for i in range(n):
        left_edges.append(edges[i][0])
        right_edges.append(edges[i][1])

    for i in range(n):
        if left_edges[i]  in left_edges[:i]:
            repeat_index=left_edges.index(left_edges[i])
            Graph[repeat_index]+=','+right_edges[i]
        else:
            Graph.append(left_edges[i]+' -> '+ right_edges[i])
    return Graph  
st='AAGATTCTCTAC'
k=4
a=de_bruijn(st, k)
df = pd.DataFrame(a)
df.to_clipboard(index=False,header=False)
a


# In[6]:


#Problem 27 from Kmers to deBuijn Graph
kmers=['GAGG',
'CAGG',
'GGGG',
'GGGA',
'CAGG',
'AGGG',
'GGAG']

def Kmers_to_deBruijn(kmers):
    edges=[]
    leftedges=[]
    rightedges=[]
    Graph=[]
    n=len(kmers)
    k= len(kmers[0])
    #make list of lef/right edges
    for i in range(n):
        leftedges.append(kmers[i][:-1])
        rightedges.append(kmers[i][1:])
    l=len(leftedges)
    
    for i in range(l):
        if leftedges[i] not in leftedges[:i]:
            Graph.append(leftedges[i]+' -> '+rightedges[i])
        else:
            index=leftedges.index(leftedges[i])
            Graph[index]+=','+rightedges[i]
    return Graph
a=Kmers_to_deBruijn(kmers)
#copy answer to clipboard
df = pd.DataFrame(a)
df.to_clipboard(index=False,header=False)
a


# In[ ]:





# In[ ]:




