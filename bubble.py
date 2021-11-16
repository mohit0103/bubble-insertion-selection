#bubble sort 
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

def bubble_sort(p):
  for i in range(len(p)-1,0,-1):
    for j in range (i):
      if p[j]>p[j+1]:
        temp = p[j]
        p[j] = p[j+1]
        p[j+1] = temp

bubble_sort(p)
print(p)

#insertion sort
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

def insertion(p):
  for i in range(len(p)):
    temp = p[i]
    j = i-1
    while j>=0 and p[j]>temp:
      p[j+1] = p[j]
      j-=1
      p[j+1] = temp

insertion(p)
print(p)

#selection sort
l = int(input("enter nos in list: "))
p=[]
for i in range(l):
  p.append(int(input("")))

def selectionSort(p, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            if p[i] < p[min_idx]:
                min_idx = i
         
        (p[step], p[min_idx]) = (p[min_idx], p[step])

size = len(p)
selectionSort(p, size)
print(p)
