import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Specifying the path to your local .txt file
file_path = "./chat.txt"

# Reading the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Preprocessing
df = preprocessor.preprocess(data)
df['user'] = df['user'].replace("Your Crush's Name", "Crush")

# print(df.head(10))
# print(user_list)

def print_line():
    print("-----------------------------------------------------------------------------------------------------")

# selected_user = input("Enter the user : Manas Pratim Biswas, Crush or Overall... ")

selected_user = ["Manas Pratim Biswas", "Crush", "Overall"]

# Overall Statistics 
for current_user in selected_user:
    num_messages, words, num_media_messages, num_links = helper.fetch_stats(current_user,df)
    print(f"Statistics for {current_user}: ")
    print(f"Total Messages : {num_messages}")
    print(f"Total Words : {words}")
    print(f"Total Medias : {num_media_messages}")
    print(f"Total Links : {num_links}")
    print_line()

# Statistical Plots
for current_user in selected_user:

    # monthly timeline
    timeline = helper.monthly_timeline(current_user,df)
    fig,ax = plt.subplots()
    ax.plot(timeline['time'], timeline['message'],color='green', label=current_user)
    plt.xticks(rotation='vertical')
    plt.title(f"Monthly Timeline {current_user}")
    ax.legend()
    plt.show()

for current_user in selected_user:

    # daily timeline
    daily_timeline = helper.daily_timeline(current_user, df)
    fig, ax = plt.subplots()
    ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black', label=current_user)
    plt.xticks(rotation='vertical')
    plt.title(f"Daily Timeline {current_user}")
    # ax.legend()
    plt.show()

for current_user in selected_user:

    # activity map
    busy_day = helper.week_activity_map(current_user,df)
    fig,ax = plt.subplots()
    ax.bar(busy_day.index,busy_day.values,color='purple',label=current_user)
    plt.xticks(rotation='vertical')
    plt.title(f"Most busy day {current_user}")
    # ax.legend()
    plt.show()

for current_user in selected_user:
   
    busy_month = helper.month_activity_map(current_user, df)
    fig, ax = plt.subplots()
    ax.bar(busy_month.index, busy_month.values,color='orange',label=current_user)
    plt.xticks(rotation='vertical')
    plt.title(f"Most busy month {current_user}")
    # ax.legend()
    plt.show()

for current_user in selected_user:

    user_heatmap = helper.activity_heatmap(current_user,df)
    fig,ax = plt.subplots()
    ax = sns.heatmap(user_heatmap,label=current_user)
    plt.title(f"Weekly Activity Map {current_user}")
    # ax.legend()
    plt.show()

for current_user in selected_user:

    # WordCloud
    df_wc = helper.create_wordcloud(current_user,df)
    fig,ax = plt.subplots()
    ax.imshow(df_wc)
    plt.title(f"Wordcloud {current_user}")
    plt.show()

for current_user in selected_user:

    # most common words
    most_common_df = helper.most_common_words(current_user,df)

    fig,ax = plt.subplots()

    ax.barh(most_common_df[0],most_common_df[1])
    plt.xticks(rotation='vertical')
    plt.title(f"Most commmon words {current_user}")
    # ax.legend()
    plt.show()