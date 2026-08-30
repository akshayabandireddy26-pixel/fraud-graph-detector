git init
cat << 'EOF' > README.md
# Fraud Graph Detector API

A lightweight, high-performance FastAPI service designed to detect suspicious circular money flows (money laundering loops) using graph-based cycle detection algorithms (Depth First Search).

## Features
* **Graph Engine:** Uses adjacency lists and DFS with a recursion stack to detect cycles.
* **FastAPI Backend:** Provides automatic interactive documentation via Swagger UI.
* **Production Ready:** Easily deployable to cloud platforms like Render.

## API Endpoints
* `POST /check-transactions`: Submits a batch of transactions to verify if any cyclical money transfers exist.
EOF
git add .
git commit -m "Initial commit with Fraud Graph Detector and README"

## Live Demo & Testing 
https://fraud-graph-detector.onrender.com/docs
