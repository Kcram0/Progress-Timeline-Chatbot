# Progress Timeline & Study Assistant Chatbot

## **About the Project**
The **Progress Timeline & Study Assistant Chatbot** is a comprehensive web application designed to help users organize, track, and optimize their study routines while providing personalized assistance through an AI chatbot. This project combines productivity tools with the power of artificial intelligence for seamless academic support.

---

## **Features**
### **Progress Timeline**
- **Dynamic Week Tracking**: Visualize progress for assignments, exams, and personal tasks.
- **Color-coded Markers**: Highlight milestones and completed tasks.
- **Leaderboard Gamification**: Track points and compete with peers for enhanced motivation.

### **Study Assistant Chatbot**
- **AI-Powered Assistance**: Offers help with academic questions, coding, assignment writing, and general study advice.
- **Persistent Chat History**: Saves previous conversations for easy reference.
- **Intuitive UI**: Simple interface designed for streamlined interaction using Streamlit.

### **Note-Taking & Organization**
- **Quick Notes**: Take and save notes directly from the interface.
- **Categorization**: Organize notes based on subject or priority.

---

## **Technologies Used**
### **Frontend**
- **HTML**: Used for structuring the pages.
- **CSS (styles.css)**: Handles the styling and visual aspects.
- **JavaScript (script.js)**: Implements interactive and dynamic features like user alerts and leaderboard updates.

### **Backend**
- **Python**: Manages logic and integrates AI capabilities.
- **SQLite (chat_history.db)**: Stores chatbot conversation history for persistence.
- **Streamlit**: Framework used to design the web app interface.

### **AI Integration**
- **Google Generative AI (Gemini API)**: Enables the chatbot’s functionality, providing high-quality AI assistance.
- **OAuth2.0 Authentication**: Ensures secure API access for Gemini.

### **Version Control**
- **Git**: Used for repository management.
- **GitHub**: Facilitates collaboration and sharing of the project.

---

## **Setup Instructions**
Follow these steps to run the project locally:

### **Prerequisites**
- Python (3.8 or higher) installed.
- Pip for Python dependency management.

### **Installation**
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/Progress-Timeline-Chatbot.git
    ```
2. Navigate to the project folder:
    ```bash
    cd Progress-Timeline-Chatbot
    ```
3. Set up your virtual environment:
    ```bash
    python -m venv myenv
    ```
4. Activate the virtual environment:
   - Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```
5. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Add your API key securely in a `.env` file:
    ```
    API_KEY=your_google_api_key
    ```

### **Run the Project**
Start the Streamlit app locally:
```bash
streamlit run Chatbot.py
