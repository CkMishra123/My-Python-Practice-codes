#1. Reindexing and filling missing values using "forward fill " method
import pandas as pd
x=pd.Series([10,20,30], index=[1,2,3])
print(x)
print(x.reindex([1,2,3,4,5], method="ffill"))

#2. Reindexing and forward fill V/S method
import pandas as pd
import numpy as np
y=pd.Series([100,300,500],index=[1,3,5])
print(y)
print(y.reindex([1,2,3,4,5]), "fill_value=0")
print(y.reindex([1,2,3,4,5], method="ffill"))

#3. Index methods combined
import pandas as pd
a=pd.Series([100,200,400,104],index=[10,20,30,40])
print(a)
index=a.index.insert(4,25) #inserting new index at position 4
print(index)
print(index.delete(0))    #deleting index value at 0th position
print(index.drop(20))    #Drop by value i.e. this removes the actual value not position
print(index)                  # Final index answer

#4. Index properties  and Logic
import pandas as pd
idx=pd.Index([5,10,10,15])
print(idx)
print(idx.is_unique) #boolean condition for unique or not (True/False)
print(idx.is_monotonic_increasing) # check whether its monotonic increasing or not
#A monotonic increasing value is something that goes up or stays flat, but never goes down
print(idx.unique())  #To print the unique index 

#5. Forward fill with limit
import pandas as pd
y=pd.Series([1, None,None, 4])
print(y)
print(y.ffill())     #Every NaN takes the previous value
print(y.ffill(limit=1))    #Only 1 NaN can be filled after each valid value


#6.Filtering Logic
import pandas as pd
a=pd.Series(['shirt', 'jeans', 'watch', 'shoes'])
print(a)
print(a.isin(['shirt','watch','mobile']))  #Keeps Only matching values from the series a


#7. MultiIndexing and level filtering
import pandas as pd
b=pd.Series([('Math', 1), ('Math', 2), ('Sci', 1), ('Sci', 2)])
print(b.unique())   #print only unique values
print(b.reindex(['Math'], level=0))  #Filters only level 0 = 'Math' and Keeps all values of level 1 (1,2)

#8. Reindex Columns and fill_value
import pandas as pd
a={"A":[1,2,3],"B":["x","y","z"]}
b=pd.DataFrame(a,columns=["B","A"])  #By specifying the column we can alter and modify the order of columns
print(b)
print(b.reindex(columns=['A', 'B', 'C']))  #C will created as new column but their values will be NaN
t=b.reindex(columns=['A','B','C'], fill_value=-1)  #It will fill the value in column C with -1
t.loc[1,'C']=2   # .iloc[row,col] is used to access using position
print(t)    #.loc[row,col] is used to Acess using label

#9. Reindexing
import pandas as pd
df = pd.DataFrame({'A': [10, 20, 30], 'B': [100, 200, 300]}, index=[1, 3, 5])
df=pd.DataFrame(df)
print(df)
#Changing indexes
print(df.reindex([1,2,3,4,5]))
#Fill missing values
print(df.reindex([1,2,3,4,5], fill_value=0))
#Using method "ffill"
print(df.reindex([1,2,3,4,5], method="ffill"))
#limit on the filling of values
print(df.reindex([1,2,3,4,5], method="ffill", limit=1)) #limit works on consecutive NaNs only  and limit counts continuous gaps, not total NaNs"
 

#10.Miscellaneous Concept problem
import pandas as pd
s = pd.Series([10, None, 30], index=[1,2,4]) #Reindex to [1,2,3,4]
print(s.reindex([1,2,3,4], method="ffill")) #Fill missing using ffill
print(s.is_monotonic_increasing) #Check monotonicity
print(s.is_unique)         #Check is_unique or not
print(s.unique())     #writing only unique values























