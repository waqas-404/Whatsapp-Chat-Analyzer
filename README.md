# 📊 WhatsApp Chat Analyzer

A robust and interactive **WhatsApp Chat Analyzer** built using Python and Streamlit. This application enables users to extract meaningful insights from exported WhatsApp chats through advanced data analysis and visualizations.

🔗 **Live Demo:** [whatsapp-chat-analyzer-m.streamlit.app](https://whatsapp-chat-analyzer-m.streamlit.app/)

---

## 🚀 Overview

The WhatsApp Chat Analyzer processes raw chat data and transforms it into actionable insights such as user activity, message trends, emoji usage, and more. It is designed with an intuitive interface and efficient backend processing for seamless analysis.

---

## ✨ Key Features

- **Comprehensive Statistics**
  - Total messages, words, media, and links shared

- **User-Level Analysis**
  - Identify most active participants
  - Individual contribution breakdown

- **Temporal Analysis**
  - Daily and monthly timelines
  - Activity trends over time

- **Activity Insights**
  - Most active days and months
  - Weekly heatmaps

- **Text Analysis**
  - Word frequency distribution
  - Custom stopword filtering (Hinglish supported)

- **WordCloud Visualization**
  - Graphical representation of commonly used words

- **Emoji Analysis**
  - Most frequently used emojis with counts

- **URL Analysis**
  - Extraction and counting of shared links

---

## 🛠️ Technology Stack

| Category          | Tools & Libraries                        |
|-------------------|------------------------------------------|
| Frontend          | Streamlit                                |
| Backend           | Python                                   |
| Data Processing   | Pandas, NumPy                            |
| Visualization     | Matplotlib, Seaborn, Altair              |
| Text Processing   | WordCloud, Emoji, URLExtract             |
| Machine Learning  | Scikit-learn (optional enhancements)     |

---

## 📁 Project Structure

```
.
├── .gitignore
├── main.py              # Streamlit application entry point
├── main.ipynb           # Development and experimentation notebook
├── helper.py            # Analysis and visualization functions
├── preprocessor.py      # Data cleaning and preprocessing logic
├── stop_hinglish.txt    # Custom stopwords for text filtering
└── requirements.txt     # Project dependencies
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

- **Windows**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run main.py
```

After running, the application will open automatically in your browser.

---

## 📥 Usage Guide

1. Open **WhatsApp**
2. Select a chat
3. Click on **Export Chat**
4. Choose **Without Media**
5. Upload the exported `.txt` file into the application

---

## 📊 Insights Generated

- Message volume and trends
- User engagement patterns
- Peak activity periods
- Frequently used words and emojis
- Communication behavior insights

---

## 🔮 Future Enhancements

- Sentiment Analysis (NLP-based)
- Multi-language support
- Real-time chat analytics
- Advanced data visualizations
- Deployment (Cloud/Web hosting)

---

## 🤝 Contributing

Contributions are welcome and appreciated. To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute with proper attribution.

---

## ⭐ Acknowledgment

If you find this project useful, consider giving it a **star ⭐** on GitHub to support the work.
