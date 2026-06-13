# 🌸 Iris Flower Classifier

A simple Machine Learning web application that classifies Iris flowers into one of three species — **Setosa**, **Versicolor**, or **Virginica** — using **Logistic Regression**, **GridSearchCV**, and **Streamlit**.

---

## 🚀 Features

* Predicts the species of an Iris flower based on four measurements.
* Uses Logistic Regression for classification.
* Hyperparameter tuning with GridSearchCV.
* Feature scaling using StandardScaler.
* Simple Streamlit-based web interface.
* Trained on the Iris Dataset from Scikit-Learn.

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-Learn
* Streamlit
* Pickle

---

## 📂 Project Structure

```text
Iris-Flower-Classifier/
│
├── app.py               # Streamlit web application
├── src.ipynb            # Model training notebook
├── model.pkl            # Trained Logistic Regression model
├── scaler.pkl           # Saved StandardScaler
├── requirements.txt     # Project dependencies
└── README.md
```

---

## 📊 Model Training Pipeline

1. Load the Iris dataset.
2. Create a DataFrame from the dataset.
3. Explore the target distribution using visualization.
4. Split the dataset into training and testing sets.
5. Scale the feature values using StandardScaler.
6. Train a Logistic Regression model.
7. Use GridSearchCV to find the best hyperparameters.
8. Evaluate the model on the test set.
9. Save the trained model and scaler using Pickle.

---

## 🌺 Input Features

The model uses the following flower measurements:

* Sepal Length (cm)
* Sepal Width (cm)
* Petal Length (cm)
* Petal Width (cm)

---

## 🎯 Target Classes

| Class ID | Species    |
| -------- | ---------- |
| 0        | Setosa     |
| 1        | Versicolor |
| 2        | Virginica  |

---

## 📈 Model Performance

The model achieves approximately **100% accuracy** on the test dataset.

```text
Accuracy: 100%
```

> Note: Exact accuracy may vary slightly depending on train-test split and hyperparameters.

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/iris-flower-classifier.git
cd iris-flower-classifier
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Open the Streamlit application in your browser.
2. Enter the flower measurements:

   * Sepal Length
   * Sepal Width
   * Petal Length
   * Petal Width
3. Click the **Predict** button.
4. The model will predict one of the following species:

   * Setosa
   * Versicolor
   * Virginica

---

## 📷 Example

### Input

```text
Sepal Length: 5.1
Sepal Width: 3.5
Petal Length: 1.4
Petal Width: 0.2
```

### Output

```text
Setosa
```

---

© 2026 Kunal Singh
