import numpy as np
import pandas as pd

data = pd.DataFrame({
    "x": np.arange(10),
    "y": np.random.randn(10)
})
print(data)


