
# ToDo Dark - Progressive Web App (PWA)

**ToDo Dark** is a sleek, dark-themed To-Do List application built with Flask and enhanced with Progressive Web App (PWA) features. It supports session-based task management and offline functionality, making it both lightweight and practical.

## 🚀 Features

- 📝 Add and delete tasks easily.
- 🔒 Session-based storage using Flask-Session.
- ⚙️ Offline support with Service Workers.
- 📱 Installable as a standalone app via PWA.
- 🌙 Responsive, dark-themed user interface.

## 🗂 Project Structure

```
todo-dark/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    ├── script.js
    ├── sw.js
    └── manifest.json
```

### Key Files

- **`app.py`**: Main Flask application.
- **`templates/index.html`**: UI template for the To-Do list.
- **`static/style.css`**: Custom dark mode styling.
- **`static/script.js`**: Registers and manages Service Worker.
- **`static/sw.js`**: Caches static files for offline use.
- **`static/manifest.json`**: Defines PWA metadata for installation.

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/todo-dark.git
   cd todo-dark
   ```

2. Set up the virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📦 PWA Features

- **Service Worker**: Caches key assets for offline availability.
- **Manifest File**: Enables installation as a web app.
- **Caching Strategy**: Ensures smooth user experience even when offline.

## 🛠 Development

- Modify UI: `templates/index.html`, `static/style.css`
- Add Features: Edit `app.py`

## 🚀 Deployment

To run in a production environment, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 app:app
```

You can deploy on platforms such as Heroku, AWS, or any Flask-compatible hosting service.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
