import pandas as pd
pd.set_option('display.max_colwidth', -1)
project_data = pd.read_csv("jeopardy.csv")
print(project_data.head())

project_data.rename(columns = 
{'Show Number' : "show_number",
' Air Date' : "air_date",
' Round' : "round",
' Category' : "category",
' Value' : "value",
' Question' : "question",
' Answer' : "answer"},
inplace = True)

print(project_data.head())

def filter_strings(word_list):
    filtered_df = project_data[ project_data.apply(lambda row: all([word in row['question'] for word in word_list]), axis=1)]
    return filtered_df

filtered_df = filter_strings(['King', 'England'])
print(filtered_df.head())
print('filtered_df.index: ' + str(len(filtered_df.index)))