import numpy as np

def calculate(list):
  if len(list)<9: #Check for list with less than 9 elements
    raise ValueError("List must contain nine numbers.")
  calculations = {'mean':[],'variance':[],'standard deviation':[],'max':[],'min':[],'sum':[]} #Define dictionary
  arr = np.array(list) #Convert list to numpy array
  arr = np.reshape(arr,(3,3)) #Reshape array to 3 x 3

  for x in range(2): #Calculate each value for axis 1 and 2, covert to list and append to dictionary
    calculations['mean'].append(np.mean(arr,axis=x).tolist())
    calculations['variance'].append(np.var(arr,axis=x).tolist())
    calculations['standard deviation'].append(np.std(arr,axis=x).tolist())
    calculations['max'].append(np.max(arr,axis=x).tolist())
    calculations['min'].append(np.min(arr,axis=x).tolist())
    calculations['sum'].append(np.sum(arr,axis=x).tolist())
  
  #Calculate flattened values, covert to list and append
  calculations['mean'].append(np.mean(arr,axis=None).tolist())
  calculations['variance'].append(np.var(arr,axis=None).tolist())
  calculations['standard deviation'].append(np.std(arr,axis=None).tolist())
  calculations['max'].append(np.max(arr,axis=None).tolist())
  calculations['min'].append(np.min(arr,axis=None).tolist())
  calculations['sum'].append(np.sum(arr,axis=None).tolist())

  #print(calculations)

  return calculations
