📌 Social Links Kanban


Social Links Kanban is a visually organized tool for managing and filtering social media links. Built with a sleek frontend and a powerful backend, this project allows you to add, prioritize, and organize links by platform, tags, and priority levels. Feel free to customize and add/change features as you wish.

Tired of bookmarking and forgetting it later? Introducing a simple and customizable social links library.

Preview

![image](https://github.com/user-attachments/assets/16a42ca2-fd0f-456e-b2d7-3e603d8b9a9e)


🌟 Features

    🐦 Add and organize links by platform: Twitter, Reddit, YouTube, Instagram.
    🔖 Categorize links with tags (e.g., Informative, Funny, Tech).
    🚦 Prioritize tasks using priority levels: Urgent, High, Medium, Low.
    🗑️ Delete or Rename links with an intuitive interface.
    🔍 Filter links by platform, tags, or priority.
    🧩 Easy-to-extend backend with FastAPI and SQLite.

📂 Project Structure

social-library/
├── backend/
│   └── main.py          # FastAPI backend
├── frontend/
│   └── index.html       # Kanban board frontend
├── requirements.txt     # Python dependencies
├── social_library.db    # SQLite database (optional)
└── README.md            # Project documentation


🚀 Getting Started

1. Clone the Repository

git clone https://github.com/your-username/social-library.git
cd social-library


2. Set Up the Backend
Install Python Dependencies

Make sure you have Python installed. Then, run:


pip install -r requirements.txt


Start the Server

Run the FastAPI server:

uvicorn backend.main:app --reload


Visit http://127.0.0.1:8000/docs to explore the API.


3. Set Up the Frontend

Simply open the frontend/index.html file in your browser:

frontend/index.html




🛠️ How to Use

    Add a Link: Enter a URL, choose a caption, tags, and priority, then click "Add Link".
    Filter Links: Use the filter dropdowns to find specific links by platform, tags, or priority.
    Manage Links:
        Rename: Modify captions, tags, or priorities directly.
        Delete: Remove unwanted links.

🧑‍💻 Tech Stack

    Frontend: Vanilla HTML, CSS, and JavaScript
    Backend: FastAPI (Python)
    Database: SQLite

📝 To-Do Features

Add user authentication.
Export links to a CSV file.
Implement drag-and-drop for reordering cards.
Deploy to a cloud platform (e.g., AWS, Herok


🤝 Contributing

Contributions are welcome! Here's how you can help:

    Fork the repository.
    Create a feature branch: git checkout -b feature-name.
    Commit your changes: git commit -m "Added a new feature".
    Push to the branch: git push origin feature-name.
    Open a pull request.

    


    
