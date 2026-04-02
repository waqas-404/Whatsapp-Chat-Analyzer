import re
import pandas as pd

def preprocess(data):
    # Supports both:
    # 12/03/2024, 21:45 -
    # 12/03/2024, 9:45 pm -
    # 12/03/24, 9:45 PM -
    
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s\w{2}\s-\s'
    
    date = re.findall(pattern, data)
    messages = re.split(pattern, data)[1:]
    
    data = pd.DataFrame({'message_date':date, 'user_message':messages})
    
    data['message_date'] = data['message_date'].str.replace('\u202f',' ')
    data['message_date'] = pd.to_datetime(data['message_date'],format = '%m/%d/%y, %I:%M %p - ')
    
    users = []
    messages = []

    for message in data['user_message']:
        # Check if the message has a colon
        if ": " in message:
            possible_user, msg = message.split(": ", 1)
            # Use regex to check if this is a valid username (letters, spaces, maybe dots)
            if re.match(r'^[\w\s\.]+$', possible_user):
                users.append(possible_user)
                messages.append(msg)
            else:
                users.append("Group Notification")
                messages.append(message)
        else:
            users.append("Group Notification")
            messages.append(message)
            
    data['users']= users
    data['messages'] = messages
    
    data['only_date'] = data['message_date'].dt.date
    data['year'] = data['message_date'].dt.year
    data['month_num'] = data['message_date'].dt.month
    data['month'] = data['message_date'].dt.month_name()
    data['day'] = data['message_date'].dt.day
    data['day_name'] = data['message_date'].dt.day_name()
    data['hour'] = data['message_date'].dt.hour
    data['minute'] = data['message_date'].dt.minute
    
    data.drop(columns = ['user_message','message_date'],inplace=True)
    
    
    period = []
    for hour in data['hour']:
        start = hour
        end = (hour + 1) % 24
        period.append(f"{start:02d}-{end:02d}")

    data['period'] = period
    
    return data

    # messages = re.split(pattern, data)[1:]
    # dates = re.findall(pattern, data)

    # df = pd.DataFrame({
    #     'user_message': messages,
    #     'message_date': dates
    # })

    # # Clean WhatsApp special spaces
    # df['message_date'] = df['message_date'].str.replace('\u202f', ' ', regex=False)
    # df['message_date'] = df['message_date'].str.strip()

    # # Remove trailing " -"
    # df['message_date'] = df['message_date'].str.replace(r'\s-\s$', '', regex=True)

    # # Try multiple possible datetime formats
    # possible_formats = [
    #     '%d/%m/%Y, %I:%M %p',   # 12/03/2024, 9:45 PM
    #     '%d/%m/%y, %I:%M %p',   # 12/03/24, 9:45 PM
    #     '%d/%m/%Y, %H:%M',      # 12/03/2024, 21:45
    #     '%d/%m/%y, %H:%M',      # 12/03/24, 21:45
    #     '%m/%d/%Y, %I:%M %p',   # 03/12/2024, 9:45 PM
    #     '%m/%d/%y, %I:%M %p',   # 03/12/24, 9:45 PM
    #     '%m/%d/%Y, %H:%M',      # 03/12/2024, 21:45
    #     '%m/%d/%y, %H:%M'       # 03/12/24, 21:45
    # ]

    # df['message_date_parsed'] = pd.NaT

    # for fmt in possible_formats:
    #     mask = df['message_date_parsed'].isna()
    #     df.loc[mask, 'message_date_parsed'] = pd.to_datetime(
    #         df.loc[mask, 'message_date'],
    #         format=fmt,
    #         errors='coerce'
    #     )

    # df['message_date'] = df['message_date_parsed']
    # df.drop(columns=['message_date_parsed'], inplace=True)

    # # Optional: remove rows that couldn't be parsed
    # df = df.dropna(subset=['message_date']).reset_index(drop=True)

    # df.rename(columns={'message_date': 'date'}, inplace=True)

    # users = []
    # messages = []

    # for message in df['user_message']:
    #     entry = re.split(r'([^:]+?):\s', message, maxsplit=1)

    #     if len(entry) >= 3:
    #         users.append(entry[1].strip())
    #         messages.append(entry[2].strip())
    #     else:
    #         users.append('group_notification')
    #         messages.append(message.strip())

    # df['user'] = users
    # df['message'] = messages
    # df.drop(columns=['user_message'], inplace=True)

    # # Date features
    # df['only_date'] = df['date'].dt.date
    # df['year'] = df['date'].dt.year
    # df['month_num'] = df['date'].dt.month
    # df['month'] = df['date'].dt.month_name()
    # df['day'] = df['date'].dt.day
    # df['day_name'] = df['date'].dt.day_name()
    # df['hour'] = df['date'].dt.hour
    # df['minute'] = df['date'].dt.minute



    # return df