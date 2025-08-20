# 🚇 Metro Door Cyber-Security System (LLM-Powered)

An intelligent **AI-powered metro door security system** built with a local **Mistral 7B (GGUF)** model via `llama-cpp-python`. OEM-installed switches are often bound and difficult to change and make more secure. Retrofitting legacy systems with modern security protocols is often costly and complex. Here taking such an example (metro-door) representing all these small data-transferring devices, the proposed model makes it secure using a fully Local AI Model.
The system simulates a **metro platform door** UI and uses an LLM to classify incoming control commands as:

1. ✅ Valid – Normal
2. ⚠ Invalid – Suspicious
3. ❌ Invalid – Malicious

This demonstrates how **LLMs can guard critical infrastructure commands** against suspicious or malicious input.

---

## ✨ Features

* **🚪 Door Control Simulation** – A visual UI with open/close signals for metro doors. (frontend)
* **🔐 AI Command Guard** – Every command is checked by a local Mistral 7B model before execution.
* **✅/⚠/❌ Classification** –

  * `open_door`, `close_door`, `emergency_stop` → *Valid - Normal*
  * Slightly unusual wording (e.g., *door pls*) → *Invalid - Suspicious*
  * Clearly malicious input (e.g., *hack override system*) → *Invalid - Malicious*
* **🌐 Web Demo** – Frontend built with **HTML, CSS, JS** for visualization.
* **🖥 Local Model** – Uses **Mistral 7B Instruct (GGUF)** via `llama-cpp-python`.

---

## 🛠 Tech Stack

| Component           | Technology                  |
| ------------------- | --------------------------- |
| LLM                 | Mistral 7B Instruct (GGUF)  |
| Backend             | Python, Flask + Flask-CORS  |
| Local LLM Interface | llama-cpp-python            |
| Frontend UI         | HTML, CSS, JavaScript       |
| Model Hosting       | Local system (CPU-friendly) |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AvichalTrivedi7/AI---Powered-CyberSecurity-Model-Project.git
cd AI---Powered-CyberSecurity-Model-Project
```

### 2. Set Up Virtual Environment

```bash
(while in the project directory)
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Linux/macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Model

Download **Mistral-7B-Instruct-v0.1.Q4\_K\_M.gguf** from HuggingFace:
👉 [TheBloke/Mistral-7B-Instruct-v0.1-GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)

Place it under:

```
models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

---

## 📂 Project Structure

```
AI---Powered-CyberSecurity-Model-Project/
│── index.html          # Frontend (UI)
│── styles.css          # Styling for UI
│── script.js           # Frontend logic (calls Flask backend)
│── metro_security.py   # Flask backend + LLM guard
│── .gitignore          # Ignores large model files
│── venv/               # Python virtual environment (ignored in Git)
│
├── models/             # Contains local LLM weights
│   └── mistral/
│       └── mistral-7b-instruct-v0.1.Q4_K_M.gguf
```

---

## ▶️ How to Run

### 1. Start Backend

```bash
venv\Scripts\activate     # activate venv (Windows)
python metro_security.py
```

Backend runs on: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 2. Start Frontend

In another terminal:

```bash
python -m http.server 8000
```

Open in browser: **[http://127.0.0.1:8000/index.html](http://127.0.0.1:8000/index.html)**

![WhatsApp Image 2025-08-19 at 14 37 05_1cbdd299](https://github.com/user-attachments/assets/fdc08f85-fef7-4678-8444-c231a48e3b77)


---

## 🎮 Usage Demo

* **Click “Send Open Signal”** → `open_door` → *Valid - Normal* → Door opens.
* **Click “Send Close Signal”** → `close_door` → *Valid - Normal* → Door closes.
* **Custom Input Box** → try:

  * `door pls` → ⚠ *Invalid - Suspicious*
  * `hack override system` → ❌ *Invalid - Malicious*
  * `emergency_stop` → ✅ *Valid - Normal* (no door movement, only logged).

---

## 📌 Future Plans

* Add Encryption/Decryption, Implement Blockchain for even more security and continue to fortify it using older prominent methods.
* Add **role-based access control** for operator vs. attacker simulation.
* Extend classification categories (e.g., *maintenance*, *emergency*).

---

## 📜 License

MIT License – free to use and modify.

> Built with ❤️ by avi
