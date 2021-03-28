class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

def find_right(node,x):
    queue=[]
    queue.append(node)
    while queue:
        q_len=len(queue)
        if x in queue:
           index=queue.index(x)
           try:
              return queue[index+1]
           except Exception as e:
              pass
        while q_len:
            m=queue.pop(0)
            if m.left:
               queue.append(m.left)
            if m.right:
               queue.append(m.right)
            q_len=q_len-1

if __name__=="__main__":
   node=Node(12)
   node.left=Node(6)
   node.right=Node(22)
   node.left.left=Node(4)
   node.left.right=Node(10)
   node.left.left.left=Node(1)
   node.left.left.right=Node(5)
   node.right.left=Node(18)
   node.right.right=Node(25)
   node.right.left.left=Node(15)
   node.right.left.right=Node(20)
   print("The right most node of 15 is:")
   print(find_right(node,node.right.left.left).value)



