# data_analysis_lecture

## Record of data analysis code

This repository stores a simple record of commonly used data analysis code.

### 1) Load data

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

### 2) Inspect data

```python
df.head()
df.info()
df.describe(include="all")
```

### 3) Clean missing values

```python
df = df.dropna()
```

### 4) Group and aggregate

```python
summary = df.groupby("category")["value"].mean()
print(summary)
```