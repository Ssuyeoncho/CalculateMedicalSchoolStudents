import pandas as pd

df_1=pd.read_excel('disease data.xlsx',sheet_name='disease ratio')
df_2=pd.read_excel('disease data.xlsx',sheet_name='disease type')

disease_ratio={}
disease_type={}

for i in df_1.index:
    x=df_1['disease code'][i]
    disease_ratio[x]=[]
    for j in range(10):
        a=j*10
        b=j*10+9
        c=str(a)+'~'+str(b)
        disease_ratio[x].append(df_1[c][i])


department=['내과','소아청소년과','산부인과','정형외과','일반외과','안과']
check=df_2.isna()
for i in department:
    disease_type[i]=[]
    for j in df_2.index:
        if check[i][j]:
            break
        disease_type[i].append(df_2[i][j]) 

print(disease_ratio)
print()
print(disease_type)
