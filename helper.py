from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_sats(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
    
    num_messages = data.shape[0]
    
    num_words = (data['messages'].str.count(' ') + 1).sum()
    
    num_media = data[data['messages'].isin(['<Media omitted>\n', '<Media omitted>'])].shape[0]
    
    num_links = data['messages'].apply(lambda x: len(extract.find_urls(str(x)))).sum()
        
    return num_messages, num_words,num_media, num_links


def most_busy_users(data):
    x = data['users'].value_counts().head()
    new_df = round((data['users'].value_counts()/(data.shape[0]))*100,2).reset_index().rename({'users':'name','count':'percent'})
    name = x.index
    count = x.values
    
    return name, count, new_df


def create_worldcloud(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
        
    s = open('stop_hinglish.txt', 'r',encoding='utf-8')
    stop_words = s.read()
        
    temp = data[~data['messages'].str.contains('Media omitted', na=False)]
    temp = temp[temp['users'] != 'Group Notification']
    
    def remove_stopwords(message):
        y=[]
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)
    
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color = 'white')
    temp['messages'] = temp['messages'].apply(remove_stopwords)
    df_wc = wc.generate(temp['messages'].str.cat(sep=" "))

    return df_wc


def most_common_words(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
        
    
    s = open('stop_hinglish.txt', 'r',encoding='utf-8')
    stop_words = s.read()
        
    temp = data[~data['messages'].str.contains('Media omitted', na=False)]
    temp = temp[temp['users'] != 'Group Notification']

    words = []
    for message in temp['messages']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    new_df = pd.DataFrame(Counter(words).most_common(20))
    return new_df
    

def emoji_helper(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
        
    emojis = []
    for message in data['messages']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    
    return emoji_df


def monthly_timeline(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
        
    timeline = data.groupby(['year','month_num','month']).count()['messages'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + '-' + str(timeline['year'][i]))
    timeline['time'] = time
    
    return timeline

def daily_timeline(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
        
    daily_timeline = data.groupby(['only_date']).count()['messages'].reset_index()
    
    return daily_timeline

def daily_activity_map(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
    
    return data['day_name'].value_counts()

def monthly_activity_map(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['users']==selected_user]
    
    return data['month'].value_counts()

def activity_heatmap(selected_user, data):
    if selected_user != 'Overall':
        data = data[data['user'] == selected_user]

    if data.empty:
        return pd.DataFrame()

    user_heatmap = data.pivot_table(
        index='day_name',
        columns='period',
        values='messages',
        aggfunc='count',
        fill_value=0
    )

    # Optional: keep weekdays in natural order
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    user_heatmap = user_heatmap.reindex(day_order)

    return user_heatmap


# extract = URLExtract()


# def fetch_stats(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     num_messages = df.shape[0]

#     words = []
#     for message in df['message']:
#         words.extend(str(message).split())

#     # handle both with and without newline
#     num_media_messages = df[df['message'].isin(['<Media omitted>\n', '<Media omitted>'])].shape[0]

#     links = []
#     for message in df['message']:
#         links.extend(extract.find_urls(str(message)))

#     return num_messages, len(words), num_media_messages, len(links)


# def most_busy_users(df):
#     x = df['user'].value_counts().head()
#     new_df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index()
#     new_df.columns = ['name', 'percent']
#     return x, new_df


# def create_wordcloud(selected_user, df):
#     with open('stop_hinglish.txt', 'r', encoding='utf-8') as f:
#         stop_words = set(f.read().split())

#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     temp = df[df['user'] != 'group_notification']
#     temp = temp[~temp['message'].isin(['<Media omitted>\n', '<Media omitted>'])]

#     if temp.empty:
#         return None

#     def remove_stop_words(message):
#         y = []
#         for word in str(message).lower().split():
#             if word not in stop_words:
#                 y.append(word)
#         return " ".join(y)

#     temp = temp.copy()
#     temp['message'] = temp['message'].apply(remove_stop_words)

#     text = temp['message'].str.cat(sep=" ").strip()

#     if not text:
#         return None

#     wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
#     df_wc = wc.generate(text)
#     return df_wc


# def most_common_words(selected_user, df):
#     with open('stop_hinglish.txt', 'r', encoding='utf-8') as f:
#         stop_words = set(f.read().split())

#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     temp = df[df['user'] != 'group_notification']
#     temp = temp[~temp['message'].isin(['<Media omitted>\n', '<Media omitted>'])]

#     words = []

#     for message in temp['message']:
#         for word in str(message).lower().split():
#             if word not in stop_words:
#                 words.append(word)

#     most_common = Counter(words).most_common(20)
#     most_common_df = pd.DataFrame(most_common)

#     return most_common_df


# def emoji_helper(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     emojis = []

#     for message in df['message']:
#         for c in str(message):
#             if c in emoji.EMOJI_DATA:
#                 emojis.append(c)

#     emoji_df = pd.DataFrame(Counter(emojis).most_common())

#     return emoji_df


# def monthly_timeline(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     if df.empty:
#         return pd.DataFrame(columns=['year', 'month_num', 'month', 'message', 'time'])

#     timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

#     time = []
#     for i in range(timeline.shape[0]):
#         time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

#     timeline['time'] = time

#     return timeline


# def daily_timeline(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     if df.empty:
#         return pd.DataFrame(columns=['only_date', 'message'])

#     daily_timeline = df.groupby('only_date').count()['message'].reset_index()

#     return daily_timeline


# def week_activity_map(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     return df['day_name'].value_counts()


# def month_activity_map(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     return df['month'].value_counts()


# def activity_heatmap(selected_user, df):
#     if selected_user != 'Overall':
#         df = df[df['user'] == selected_user]

#     if df.empty:
#         return pd.DataFrame()

#     user_heatmap = df.pivot_table(
#         index='day_name',
#         columns='period',
#         values='message',
#         aggfunc='count',
#         fill_value=0
#     )

#     # Optional: keep weekdays in natural order
#     day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     user_heatmap = user_heatmap.reindex(day_order)

#     return user_heatmap