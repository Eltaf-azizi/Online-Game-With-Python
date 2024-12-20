<h1 align = "center">Online Game With Python</h1>

This repository contains two Python projects: an Online Multiplayer Game and an Online Chat Application. Both projects showcase real-time functionality using Python, sockets, and additional frameworks. The game was developed during a 12-hour coding livestream, while the chat application was created in a live session to experiment with socket-based communication and Flask for the front end.

## Online Multiplayer Game

### Overview
This project is a real-time multiplayer game created with Python and Pygame, allowing players to connect to a server and interact within the game environment. Built in a 12-hour live coding session, the goal was to create a fully functional game that users could join and play together.

### Features

 - Multiplayer gameplay using socket connections
 - Real-time interactions and smooth gameplay
 - Basic Pygame interface for user engagement

## Getting Started

#### 1. Clone the repository:

    git clone <your-repo-link>
    cd <project-folder>
    
#### 2. Install dependencies: Ensure you have Python and pip installed, then install Pygame:

    pip install pygame

#### 3. run the game server
    python server.py
    
#### 4. Start the game client: In a new terminal, run:

    python client.py

## Online Chat Application
### Overview
This online chat application uses Flask for the front end and a Python socket server for managing real-time communication. Initially developed in a live coding session, this project demonstrates basic chat functionalities with the potential for additional features.

### Features

 - Real-time messaging between users
 - Simple Flask-based front end
 - Basic user interface for easy interactions

## Getting Started

#### 1. Clone the repository:

    git clone <your-repo-link>
    cd <project-folder>
#### 2. Install dependencies:

    pip install flask
    
#### 3. Run the chat server and Flask app:

    python server.py
    python app.py
Access the chat application: Open a browser and navigate to http://localhost:5000.

## Technologies Used
 - **Python:** Primary programming language
 - **Pygame:** Game development for the multiplayer game
 - **Flask:** Web framework for the chat application
