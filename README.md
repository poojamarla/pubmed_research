# PubMed Research Paper Fetcher

## 📌 Description
This Python program fetches research papers from the **PubMed API**, filters papers with at least one author affiliated with a **pharmaceutical/biotech company**, and saves the results as a **CSV file**.

## 🚀 Features
✅ Fetches papers using the **PubMed API**  
✅ Filters out **academic authors** based on their affiliation  
✅ Saves results in a **structured CSV format**  
✅ Supports **command-line arguments** for query input, debug mode, and file output  
✅ Provides **debug mode** for detailed execution logs  

---

## 📌 Prerequisites
Before running the program, make sure you have:  
- **Python 3.8+** installed → [Download Here](https://www.python.org/downloads/)  
- **Git** installed → [Download Here](https://git-scm.com/downloads)  
- **Poetry** for dependency management → [Install Here](https://python-poetry.org/docs/)  

### **🔹 Verify Installations**
Run the following commands to check if everything is installed:  

`python --version`

`git --version`

`poetry --version`

---


## **📌 Installation**
1️⃣ Clone the Repository

`git clone https://github.com/your-username/pubmed_research_fetcher.git`

`cd pubmed_research_fetcher`

2️⃣ Install Dependencies Using Poetry

`poetry install`

3️⃣ Activate the Poetry Virtual Environment

`poetry shell`

---

## **📌 Usage**
1️⃣ Fetch Papers for a Specific Query

`python fetch_papers.py "cancer treatment"`

🔹 This will display the filtered papers in the terminal.

2️⃣ Save Results to a CSV File

`python fetch_papers.py "cancer treatment" -f results.csv`

🔹 This will create a results.csv file in the project directory.

3️⃣ Enable Debug Mode

`python fetch_papers.py "cancer treatment" -d`

🔹 Debug mode prints API responses and filtering details.

---

## **📌 Project Structure**
`pubmed_research_fetcher/`

`│── fetch_papers.py        # Main script`

`│── README.md              # Documentation`

`│── pyproject.toml         # Poetry dependency file`

`│── results.csv            # Output file (optional)`

---

## **📌 Troubleshooting**
❌ Issue: ModuleNotFoundError: No module named 'requests'

✅ Solution: Run poetry install to install dependencies.

❌ Issue: error: failed to push some refs to GitHub

✅ Solution: Run git pull origin main --rebase before pushing again.

---

## **📌 Contributing**
Want to improve this project? Feel free to:

1️⃣ Fork the repository

2️⃣ Create a new branch

3️⃣ Submit a pull request (PR)

---

## **📌 License**
This project is open-source and available under the MIT License.

---

## **📌 Final Steps**
✅ Copy this README.md into your GitHub repository

✅ Commit & push it to GitHub:

`git add README.md`

`git commit -m "Updated README"`

`git push origin main`
