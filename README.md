<div align="center">
  
  <img src="assets/mockup.png" alt="Movie Recommendation System 3D Mockup" width="100%">

  <br/><br/>
  
  # 🎬 Movie Recommendation System
  
  <p align="center">
    A stunning, full-stack content-based recommendation engine powered by <b>AI & Cosine Similarity</b>.
  </p>
  
  <p align="center">
    <img src="https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white" alt="Angular" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
    <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
  </p>

</div>

<br/>

## ✨ Features

<table>
  <tr>
    <td width="50%" style="padding: 20px;">
      <h3 align="center">🧠 Smart Recommendations</h3>
      <p align="center">Advanced NLP pipeline & cosine similarity matrix predicting films based on plot, genres, cast, and directors across 4,800+ movies.</p>
    </td>
    <td width="50%" style="padding: 20px;">
      <h3 align="center">⚡ Blazing Fast API</h3>
      <p align="center">Built entirely on Python's FastAPI to instantly stream similarities with near-zero latency and high concurrency.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" style="padding: 20px;">
      <h3 align="center">🎨 Premium UI/UX</h3>
      <p align="center">Gorgeous glassmorphism user interface designed with Angular 21 & TailwindCSS v4 with rich 3D gradients.</p>
    </td>
    <td width="50%" style="padding: 20px;">
      <h3 align="center">📱 Fully Responsive</h3>
      <p align="center">Adapts seamlessly to any screen size—from ultrawide desktop monitors to mobile devices with optimized cards.</p>
    </td>
  </tr>
</table>

---

## 🏗️ Architecture Stack

<table>
  <tr>
    <td width="50%" valign="top" style="padding: 20px;">
      <h3 align="center">⚙️ Backend Pipeline (FastAPI)</h3>
      <ul>
        <li><b>Merge Data:</b> Combines TMDB 5k movies & credits</li>
        <li><b>Extraction:</b> JSON nested data (Top-3 Cast, Director)</li>
        <li><b>NLP:</b> Stopword removal & Porter Stemming</li>
        <li><b>Matrix:</b> 5000-dimensional <code>CountVectorizer</code></li>
        <li><b>Compute:</b> Dense Cosine Similarity Matrix</li>
      </ul>
    </td>
    <td width="50%" valign="top" style="padding: 20px;">
      <h3 align="center">💻 Frontend App (Angular)</h3>
      <ul>
        <li><b>Architecture:</b> Standalone component ecosystem</li>
        <li><b>State:</b> Modern Angular Signals for deep reactivity</li>
        <li><b>Services:</b> <code>MovieService</code> with RxJS observables</li>
        <li><b>Styles:</b> TailwindCSS v4 with auto dark/light mode</li>
        <li><b>Icons:</b> Scalable animated SVG elements</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🚀 Quick Start

<table>
  <tr>
    <td width="50%" valign="top" style="padding: 20px;">
      <h3 align="center">1️⃣ Start the Backend API</h3>
      <pre><code>cd Backend
pip install fastapi uvicorn pandas numpy scikit-learn nltk
uvicorn main:app --reload</code></pre>
      <p align="center"><i>Runs internally at <code>http://localhost:8000</code></i></p>
    </td>
    <td width="50%" valign="top" style="padding: 20px;">
      <h3 align="center">2️⃣ Start the Frontend App</h3>
       <pre><code>cd Frontend/MovieRecommendationSystem
npm install
ng serve</code></pre>
      <p align="center"><i>Launch your UI at <code>http://localhost:4200</code></i></p>
    </td>
  </tr>
</table>

<br/>

---

<div align="center">
  <p>Crafted with 💜 for movie lovers and developers alike.</p>
</div>
