

# import pandas as pd

# data1 = {'tb1_col1':  [1,2,3,4,5],
#         }

# data2 = {'tb2_col1':  [3,2,1]
#         }

# df1 = pd.DataFrame (data1)
# df2 = pd.DataFrame (data2)

# # x = df1['tb1_col1']
# # result = x + 2
# # print(result)
# # print("----------------------------------------------------------")

# # y = 4
# # result = y + 2
# # print(result)
# # print("----------------------------------------------------------")

# # print("\n")
# # print(df1)
# # print("\n")
# # print("----------------------------------------------------------")
# # print("\n")
# # print(df2)
# # print("\n")
# # print("----------------------------------------------------------")
# # print("\n")

# df1['tmp'] = 1
# df2['tmp'] = 1

# new_df = pd.merge(df1, df2, on=['tmp'])
# new_df = new_df.drop('tmp', axis=1)

# print(new_df)
# print("\n")
# print("----------------------------------------------------------")
# print("\n")


# s1 = new_df['tb1_col1']==new_df['tb2_col1']
# s2 = new_df['tb1_col1'] < 5
# new_df = new_df[s2 | False]
# print(new_df)

sent = "   5   years   4  months  4   days     12:22:13    "
sent = sent.split()

idx = sent.index("seconds")
val = sent[idx-1]

print(val)