import numpy as np
def calculate(l):

  if len(l)==9:
    m=np.array(l)
    n=np.array([m[:3],m[3:6],m[6:9]])
  
    mean_rows=n.mean(axis=1)
    mean_columns=n.mean(axis=0)
    
    var_rows=n.var(axis=1)
    var_columns=n.var(axis=0)
  
    std_rows=n.std(axis=1)
    std_columns=n.std(axis=0)
  
    max_rows=n.max(axis=1)
    max_columns=n.max(axis=0)
  
    min_rows=n.min(axis=1)
    min_columns=n.min(axis=0)
  
    sum_rows=n.sum(axis=1)
    sum_columns=n.sum(axis=0)
    
    return{
      'mean':[mean_columns, mean_rows, n.mean()],
      'variance':[var_columns, var_rows, n.var()],
      'standard deviation':[std_columns, std_rows, n.std()],
      'max':[max_columns, max_rows, n.max()],
      'min':[min_columns, min_rows, n.min()],
      'sum':[sum_columns, sum_rows, n.sum()]
      }
   
  else:
    return("The list does not have 9 digits")
  
  
  