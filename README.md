<div align="center">
  <h2 align="center">Medical Chatbot</h2>
  <div align="left">
	
![Repo Views](https://visitor-badge.laobi.icu/badge?page_id=SpencerVJones/MedicalChatbot)
</div>

  <p align="center">
   A simple rule-based medical chatbot that suggests possible diseases based on user-input symptoms. Built using real-world symptom-disease data and TF-IDF vector similarity.
    <br />
    <br />
    <a href="https://github.com/SpencerVJones/MedicalChatbot/issues">Report Bug</a>
    ·
    <a href="https://github.com/SpencerVJones/MedicalChatbot/issues">Request Feature</a>
  </p>
</div>


<!-- PROJECT SHIELDS -->
<div align="center">

![License](https://img.shields.io/github/license/SpencerVJones/MedicalChatbot?style=for-the-badge)
![Contributors](https://img.shields.io/github/contributors/SpencerVJones/MedicalChatbot?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/SpencerVJones/MedicalChatbot?style=for-the-badge)
![Stargazers](https://img.shields.io/github/stars/SpencerVJones/MedicalChatbot?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/SpencerVJones/MedicalChatbot?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/SpencerVJones/MedicalChatbot?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/SpencerVJones/MedicalChatbot?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TFIDF-yellowgreen?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-%E2%9C%94%EF%B8%8F-green.svg?style=for-the-badge)
![Text Similarity](https://img.shields.io/badge/Cosine-Similarity-blue?style=for-the-badge)
![Rule-Based](https://img.shields.io/badge/Diagnosis-Rule--Based-lightgrey?style=for-the-badge)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-%E2%9C%94%EF%B8%8F-orange.svg?style=for-the-badge)

</div>



## 📑 Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Features](#features)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [How to Use](#how-to-use)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
	- [Contributors](#contributors)
- [License](#license)
- [Contact](#contact)

## Overview
This chatbot takes user-described symptoms and returns the most likely disease by matching against a medical dataset using text vectorization and cosine similarity. It's a lightweight, explainable alternative to black-box AI models, ideal for demos or educational use.

## Technologies Used
- Python 3.10+
- Pandas
- NumPy
- Scikit-learn
- NLTK
- TF-IDF Vectorization
- Cosine Similarity

## Dataset
-   **Source**: [Disease-Symptom Description Dataset (Kaggle)](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)
-   **Structure**: Each row lists a disease and up to 17 associated symptoms
-   **Preprocessing**: Combines symptoms into a single string per row for TF-IDF vectorization

## Features
- Simple CLI chatbot interface
- Real symptom-to-disease similarity matching
- Confidence-based response logic
- Real medical dataset used for training
- Lightweight and fast (no GPU required)

## Demo
Coming Soon!

## Project Structure
```bash
MedicalChatbot/  
├── Medical Chatbot/  
│ ├── real_chatbot.py # Main chatbot script  
│ ├── dataset.csv # Downloaded from Kaggle  
│ └── README.md
```
## Testing
Coming Soon!

## Getting Started
### Prerequisites
- Python 3.10+
- `pip install pandas numpy scikit-learn nltk`
### Installation
- `git clone https://github.com/SpencerVJones/MedicalChatbot.git`
- Download the dataset and place it as `dataset.csv` in the same folder
###  How to Use
 - `python real_chatbot.py`
 
## Usage
-   Enter symptoms separated by spaces
-   See the chatbot's predicted disease and confidence
-   Type `exit` to quit
 
## Roadmap
 - [ ] Add synonym handling and spelling correction
 - [ ] Expand support for symptom questions (e.g., "What should I do if...")
 - [ ] Streamlit or Flask UI
 - [ ] Naive Bayes classification backend
 - [ ] Export results to JSON or logs

See open issues for a full list of proposed features (and known issues).
 
 
## Contributing
Contributions are welcome! Feel free to submit issues or pull requests with bug fixes, improvements, or new features.
- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

### Contributors
<a href="https://github.com/SpencerVJones/MedicalChatbot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SpencerVJones/MedicalChatbot"/>
</a>


## License
Distributed under the MIT License. See LICENSE for more information.



## Contact
Spencer Jones
📧 [SpencerVJones@outlook.com](mailto:SpencerVJones@outlook.com)  
🔗 [GitHub Profile](https://github.com/SpencerVJones)  
🔗 [Project Repository](https://github.com/SpencerVJones/MedicalChatbot)
