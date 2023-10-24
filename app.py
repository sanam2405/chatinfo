import preprocessor,helper
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Specifying the path to your local .txt file
chat_file_path = "./chat.txt"
group_chat_file_path = "./group_chat.txt"

# Reading the content of the file
with open(chat_file_path, 'r', encoding='utf-8') as file:
    chat_data = file.read()

with open(group_chat_file_path, 'r', encoding='utf-8') as file:
    group_chat_data = file.read()

df_chat = preprocessor.preprocess(chat_data)
df_group_chat = preprocessor.preprocess(group_chat_data)

# Preprocessing
df_chat['user'] = df_chat['user'].replace("<My Crush's Name>", "Crush")
df_group_chat['user'] = df_group_chat['user'].replace("Manas Bsnl", "Manas Pratim Biswas")
df_group_chat['user'] = df_group_chat['user'].replace("<My Crush's Name>", "Crush")
df_group_chat['message'] = df_group_chat['message'].str.replace("<My Crush's Name>", "RP", regex=False)

# print(df_chat.head(10))
# print(df_group_chat.head(10))

df = pd.concat([df_chat, df_group_chat])
# print(df.head(20))

# selected_user = input("Enter the user : Manas Pratim Biswas, Crush or Overall... ")

selected_user = ["Manas Pratim Biswas", "Crush", "Overall"]

# Overall Statistics 
for current_user in selected_user:
    num_messages, words, num_media_messages, num_links = helper.fetch_stats(current_user,df)
    avg_word_per_msg = words/num_messages
    total_emojis = helper.emoji_helper(current_user,df)[1].sum()
    unique_emojis = len(helper.emoji_helper(current_user,df))
    most_used_emoji = helper.emoji_helper(current_user,df)[0][0]
    reply_time = helper.time_to_reply(current_user,df)

    if(current_user=="Overall"):
        reply_time = (helper.time_to_reply("Manas Pratim Biswas",df) + helper.time_to_reply("Crush",df))/2

    print(f"Statistics for {current_user}: ")
    print(f"Total Messages : {num_messages}")
    print(f"Total Words : {words}")
    print(f"Average words per message : {avg_word_per_msg:.3f}")
    print(f"Mean time taken to reply : {helper.format_time_diff(reply_time)}")
    print(f"Total emojis : {total_emojis}")
    print(f"Total unique emojis : {unique_emojis}")
    print(f"Most used emoji : {most_used_emoji}")
    print(f"Total Media : {num_media_messages}")
    print(f"Total Links : {num_links}")
    helper.print_line()

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


for current_user in selected_user:
    # emoji analysis
    emoji_df = helper.emoji_helper(current_user,df)
    emoji_df = emoji_df.rename(columns={0: 'Emoji'})
    emoji_df = emoji_df.rename(columns={1: 'Frequency'})
    print(f"Top 25 Emojis {current_user}")
    print(emoji_df.head(25))

    # # Define the filename for the README.md file
    # filename = f"{current_user}_emoji.md"

    # # Generate the markdown table
    # markdown_table = emoji_df.to_markdown(index=False)

    # # Write the markdown table to the README.md file
    # with open(filename, 'w') as file:
    #     file.write(markdown_table)
    
    