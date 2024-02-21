from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import mysql.connector

# connecting to database
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="notes_db"
)
cursor = db.cursor()

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
    
    # Implement GET method to fetch all
    def do_GET(self):
        if self.path == "/notes":
            cursor.execute("SELECT * FROM notes")
            all_notes = cursor.fetchall()
            self._set_headers()
            self.wfile.write(json.dumps(all_notes).encode())
        elif self.path.startswith("/note/"):
            notes_id = self.path.split("/")[-1]
            cursor.execute("SELECT * FROM notes WHERE id = %s", (notes_id))
            note = cursor.fetchone()
            if note:    
                self._set_headers()
                self.wfile.write(json.dumps(note).encode())
            else:
                self._set_headers(404)
        else:
            self._set_headers(404)

    # Implement POST method to add new notes
    def do_POST(self):
        if self.path == "/notes":
            get_content_length = int(self.headers['Content-Length'])
            note = json.loads(self.rfile.read(get_content_length))
            cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (note["title"], note["content"]))
            db.commit()
            self._set_headers(201)
        else:
            self._set_headers(404)


    # Implement PUT method to update a note
    def do_PUT(self):
        if self.path.startswith("/note/"):
            notes_id = self.path.split("/")[-1]
            get_content_length = int(self.headers['Content-Length'])
            note = json.loads(self.rfile.read(get_content_length))
            cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (note["title"], note["content"], notes_id))
            db.commit()
            self._set_headers()
        else:
            self._set_headers(404)

    # Implement DELETE method to delete a note
    def do_DELETE(self):
        notes_id = self.path.strip("/").split("/")[-1]
        cursor.execute("DELETE FROM notes WHERE id = %s", (notes_id,))
        db.commit()
        self._set_headers()

# runs server
def run(serverClass=HTTPServer, handlerClass=RequestHandler, port=8080):
    serverAddress = ('', port)
    httpd = serverClass(serverAddress, handlerClass)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()   