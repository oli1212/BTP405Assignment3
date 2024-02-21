Activity 3

1. Clone the repository in VS code.
2. Make sure docker desktop is installed
3. Using git bash terminal you must run this code:
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=A1245784512 -e MYSQL_DATABASE=noteData -d mysql:latest
4. Using: 
python server.py

Next use: 
GET: curl -X GET http://localhost:8080/notes

POST:curl -X POST http://localhost:8000/notes -H "Content-Type: application/json" -d "{"title": "New Note", "content": "This is a new note."}"

PUT:curl -X PUT http://localhost:8000/note/1 -H "Content-Type: application/json" -d "{"title": "Updated Note", "content": "This note has been updated."}"

DELETE:curl -X DELETE http://localhost:8000/note/1