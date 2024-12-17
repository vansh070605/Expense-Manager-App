from application import app, db

# Ensure database tables are created
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
