# MapFlow 🌍
[Live Demo](https://mapflow.onrender.com)

MapFlow is an interactive pathfinding and graph visualization tool that enables users to explore cities visualize popular pathfinding algorithms. 

### 🛠️ Technologies Used
Frontend:
HTML, CSS, JavaScript (Canvas API)
Backend:
Python (Flask, Flask-SocketIO)
Pathfinding Algorithms:
Dijkstra's, A*, BFS, DFS
Deployment:
Hosted on Render

### 📖 How to Use
Visit the live demo: [MapFlow](https://mapflow.onrender.com)
Select a city from the provided options (e.g., Paris, Rome, Chicago). Larger cities require time to load and perform algorithms.

Click on two nodes to set your start and end points.
Start node: Highlighted in green.
End node: Highlighted in red.
Choose an algorithm.
Reset the graph or switch algorithms anytime.

### 🔧 Local Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/mapflow.git  
cd mapflow  
Install Dependencies:

Make sure Python is installed.
Install required Python libraries:
bash
Copy code
pip install flask flask-socketio  
Run the Application:

bash
Copy code
python app.py  
Open in Browser:
Navigate to http://localhost:5000 in your browser.

