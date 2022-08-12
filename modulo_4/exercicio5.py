import pandas as pd
import numpy as np
  
df = pd.Series(['Sport', 'Flamengo', 'PSG', 'SantaRosa',
                'Marginal', np.nan, 'CruzZera'], dtype=pd.StringDtype())
  
print(df.str.lower(),'\n')
print(df.str.upper(),'\n')
print(df.str.strip())
