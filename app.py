from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database configuration
def get_db_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='',
                           database='reservasi_tiket',
                           cursorclass=pymysql.cursors.DictCursor)

# Home route
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        connection = get_db_connection()
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
                connection.commit()
                flash('Registration successful! Please login.', 'success')
                return redirect(url_for('login'))
            except pymysql.err.IntegrityError:
                flash('Username already exists!', 'danger')
                return redirect(url_for('register'))
            finally:
                connection.close()
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            user = cursor.fetchone()
            connection.close()

            if user and check_password_hash(user['password_hash'], password):
                session['username'] = user['username']
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid credentials!', 'danger')
                return redirect(url_for('login'))
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Please log in first!', 'danger')
        return redirect(url_for('login'))

    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM reservations")
        reservations = cursor.fetchall()
        connection.close()
    return render_template('dashboard.html', reservations=reservations)

# Create reservation route
@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'username' not in session:
        flash('Please log in first!', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        nama = request.form['nama']
        kategori_destinasi = request.form['kategori_destinasi']
        kota_destinasi = request.form['kota_destinasi']
        jumlah_orang = request.form['jumlah_orang']
        tanggal = request.form['tanggal']

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO reservations (nama, kategori_destinasi, kota_destinasi, jumlah_orang, tanggal)
                VALUES (%s, %s, %s, %s, %s)
            """, (nama, kategori_destinasi, kota_destinasi, jumlah_orang, tanggal))
            connection.commit()
            connection.close()
        flash('Reservation created successfully!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('create.html')

# Update reservation route
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if 'username' not in session:
        flash('Please log in first!', 'danger')
        return redirect(url_for('login'))

    connection = get_db_connection()
    with connection.cursor() as cursor:
        if request.method == 'POST':
            nama = request.form['nama']
            kategori_destinasi = request.form['kategori_destinasi']
            kota_destinasi = request.form['kota_destinasi']
            jumlah_orang = request.form['jumlah_orang']
            tanggal = request.form['tanggal']
            cursor.execute("""
                UPDATE reservations
                SET nama = %s, kategori_destinasi = %s, kota_destinasi = %s, jumlah_orang = %s, tanggal = %s
                WHERE id = %s
            """, (nama, kategori_destinasi, kota_destinasi, jumlah_orang, tanggal, id))
            connection.commit()
            connection.close()
            flash('Reservation updated successfully!', 'success')
            return redirect(url_for('dashboard'))

        cursor.execute("SELECT * FROM reservations WHERE id = %s", (id,))
        reservation = cursor.fetchone()
        connection.close()
    return render_template('update.html', reservation=reservation)

# Delete reservation route
@app.route('/delete/<int:id>')
def delete(id):
    if 'username' not in session:
        flash('Please log in first!', 'danger')
        return redirect(url_for('login'))

    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM reservations WHERE id = %s", (id,))
        connection.commit()
        connection.close()
    flash('Reservation deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)