import json
from  collections import defaultdict
from matplotlib import pyplot as plt
from matplotlib import style

def list_duplicates(seq):
   tally=defaultdict(list)
   for i,item in enumerate(seq):
      tally[item].append(i)
   return((key,locs) for key,locs in tally.items() if len(locs)>1)

def extract(file):
    json_file = open(file)
    data = json.load(json_file)
    dow=[]
    time=[]
    conf=[]
    for p,q,r in data :
       for k,v in p.items():
          dow.append(v)
       for t,h in q.items():
          time.append(h)
       for a,b in r.items():
          for c in b.items():
             conf.append(b["Large"])
    x={}
    y={}
    for c in (list_duplicates(dow)):
        #print(c)
        x.update({c[0]:c[1]})
        
    for k,v in x.items():
       t_room = {}
       for p in v:
          t_room.update({time[p]:conf[p]})
       y.update({k:t_room})
    
    m ={'Monday':{},'Tuesday':{},'Wednesday':{},'Thursday':{},'Friday':{}}
    for k,v in m.items():
        m.update({k:y[k]})
    for k,v in m.items():
        s={i:v[i] for i in sorted(v)}
        m.update({k:s})
    
    return m

ext = extract("F5_Week1.txt")

X=[[],[],[],[],[]]
Y=[[],[],[],[],[]]
i=0
for k,v in ext.items():
    for p,q in v.items():
        X[i].append(p)
        Y[i].append(q)
    i=i+1
    
#style.use('ggplot')
#plt.bar(X[0],Y[0],align='center')
#plt.bar(X[1],Y[1],color='g',align='center')
#plt.bar(X[2],Y[2],color='b',align='center')
#plt.bar(X[3],Y[3],color='yellow',align='center')
#plt.bar(X[4],Y[4],color='pink',align='center')


#style.use('ggplot')
plt.plot(X[0],Y[0], color='red', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='red', markersize=12)
plt.plot(X[1],Y[1],color='g', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='green', markersize=12)
plt.plot(X[2],Y[2],color='b', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='blue', markersize=12)
plt.plot(X[3],Y[3],color='yellow',linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='yellow', markersize=12)
plt.plot(X[4],Y[4],color='pink', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='pink', markersize=12)


plt.title('Booking Info')
plt.ylabel('rooms')
plt.xlabel('Time')
plt.show()


