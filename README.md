# 📚 Folio - Book Recommendation System

Folio is a beautifully designed **Content-Based Book Recommendation System** built using **Python**, **Machine Learning**, and **Streamlit**.  
It recommends books similar to a selected title using **Cosine Similarity** and **Count Vectorization**, delivering fast and intelligent suggestions through an interactive web interface.

---

## ✨ Features

- 📖 **Instant Book Recommendations** based on selected title  
- 🎨 **Elegant UI** inspired by bookstore design using custom CSS  
- ⚡ **Fast Recommendation Engine** with optimized processing  
- 🧠 **Machine Learning-based Content Filtering**  
- 📚 **Book Cover Display** for better visual experience  
- 🌐 **Interactive Streamlit Web Application**  

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **Pickle**
- **Machine Learning (NLP Techniques)**

---

## 📂 Project Structure

```bash
├── Book_recommendation_app.py      # Streamlit web application
├── Book_recommendation_train.py    # Model training script
├── books.pkl                       # Processed dataset
├── similarity1.pkl                 # Cosine similarity matrix
├── books.xls                       # Original dataset
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Data Preprocessing
The dataset is cleaned and prepared by:
- Handling **missing values**
- Removing **duplicate book entries**
- Combining important features into a single **tags column**

---

### 2️⃣ Feature Extraction
The text data is converted into numerical format using:

```python
CountVectorizer()
```

---

### 3️⃣ Similarity Calculation
Book similarity is computed using:

```python
cosine_similarity(vectors)
```

This helps identify how closely two books are related.

---

### 4️⃣ Recommendation System
When a user selects a book:
- The system calculates similarity scores  
- Sorts results in descending order  
- Returns **Top 5 Recommended Books**

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/book-recommendation-system.git
```

### Step 2: Navigate to Project Directory
```bash
cd book-recommendation-system
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Train the Model
```bash
python Book_recommendation_train.py
```

### Step 5: Run the Application
```bash
streamlit run Book_recommendation_app.py
```

---

## 📸 Application Preview

- Select your favorite book  
- Click on **Recommend**  
- Get **Top 5 Similar Books Instantly**

---

## 🧠 Machine Learning Concepts Used

- **Natural Language Processing (NLP)**
- **Count Vectorization**
- **Cosine Similarity**
- **Content-Based Filtering**

---

## 📈 Future Improvements

- 🔹 Add **Collaborative Filtering**
- 🔹 Implement **User Login System**
- 🔹 Add **Ratings & Reviews System**
- 🔹 Use **Deep Learning Models**
- 🔹 Deploy on **Cloud Platforms (AWS/Streamlit Cloud)**

---

## 👩‍💻 Author

**Developed by:** Mallareddygari Gayathri 
AI & ML Engineer

---

## 📜 License

This project is licensed under the **MIT License** and is open-source.
