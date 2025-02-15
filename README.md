# 🏰 Job Scraper - Extract Job Postings from Career Pages 🚀  

A FastAPI & JavaScript-based tool that extracts job listings from career pages and displays them in a structured format. Simply enter a job page URL, and the backend will fetch details like role, experience, skills, and description using Llama-3.3-70B AI.  

## ✨ Features  

✅ Extract job postings from career pages 📝  
✅ Uses FastAPI + LangChain for AI-powered data extraction 🤖  
✅ Fetches role, experience, skills, and job description 🔍  
✅ Frontend to input URL & display structured job details 🎨  
✅ Supports multiple career websites 🌎  

## 🛠 Tech Stack  

- **Backend:** FastAPI, LangChain, Groq API, Web Scraper  
- **Frontend:** HTML, JavaScript (Fetch API)  
- **Deployment:** Uvicorn (for FastAPI server)  

## 🚀 Getting Started  

### 1⃣ Clone the Repository  

```sh  
git clone https://github.com/yourusername/job-scraper.git  
cd job-scraper  
```

### 2⃣ Install Dependencies  

```sh  
pip install -r requirements.txt  
```

### 3⃣ Run FastAPI Backend  

```sh  
uvicorn main:app --reload  
```

### 4⃣ Open the Frontend  

Open `index.html` in your browser and enter a job page URL.  

## 🎯 API Usage  

### 📌 Endpoint:  

```http  
GET /fetch-job/?url=<job_page_url>  
```

### 👥 Example Request  

```sh  
curl -X GET "http://127.0.0.1:8000/fetch-job/?url=https://careers.nike.com/principal-software-engineer/job/R-46010"  
```

### 📤 Example Response  

```json  
{
  "status": "success",  
  "data": {  
    "role": "Principal Software Engineer",  
    "experience": "Minimum 12+ years of experience in software engineering, with a strong focus on cloud computing, architecture, and multi-cloud engineering.",  
    "skills": [  
      "Deep expertise in multiple cloud platforms (AWS, Azure, Google Cloud), including design, development, and deployment across these environments.",  
      "Strong technical leadership skills, with experience guiding cross-functional teams and influencing technical direction.",  
      "Knowledge of cloud governance principles, strategy, risk, compliance.",  
      "Excellent communication and collaboration skills, with the ability to work effectively with both technical and non-technical stakeholders.",  
      "Innovative problem-solving skills, with a track record of developing creative solutions to complex technical challenges."  
    ],  
    "description": "We are seeking a Principal Engineer at Nike to be instrumental in shaping our technology strategy. Your expertise in multi-cloud engineering will not only help us stay ahead of the curve in this rapidly changing landscape but also contribute significantly to our overall success."  
  }  
}  
```

## 🖥 Frontend Integration  

The frontend uses JavaScript (Fetch API) to send requests to the backend and display job details dynamically.  

## 📌 Contributing  

1. Fork the repo  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit your changes (`git commit -m "Add new feature"`)  
4. Push to the branch (`git push origin feature-branch`)  
5. Open a Pull Request 🚀  

## 🐝 License  

This project is licensed under the MIT License.  

## ⭐ Support & Feedback  

If you find this project useful, please ⭐ the repo! Feedback & contributions are always welcome. 🚀✨  

