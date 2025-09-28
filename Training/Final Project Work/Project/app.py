from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
from logger import Logger
from student import student
from feedback import feedback as Feedback
from admin import admin as Admin
from os import path as Path

class DuplicateFeedbackError (Exception):
    pass

app = Flask(__name__)
app.secret_key = "secret"   # needed for sessions & flash

logger = Logger("StudentFeedbackApp")

BASE_DIR = Path.dirname(Path.abspath(__file__))
LOG_FILE = Path.join(BASE_DIR, "app.log")

# ----------------------------
# REGISTER ROUTE
# ----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        new_student = student()

        try:
            new_student.Registration(name, email, password)
            logger.write_log(f"Registration successful for email={email}", level="info")
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))

        except Exception as e:
            logger.write_log(f"Duplicate registration attempt for email={email}", level="warning")
            flash("Email already registered!", "danger")

    return render_template("register.html")


# ----------------------------
# LOGIN ROUTE
# ----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        session["email"] = email
        student_login = student()

        if student_login and student_login.Login(email, password):
            logger.write_log(f"Login successful for email={email}", level="info")
            flash("Login successful!", "success")
            return redirect(url_for("submit_feedback", email=email))
        else:
            logger.write_log(f"Login failed for email={email}", level="warning")
            flash("Invalid email or password!", "danger")

    return render_template("login.html")


# ----------------------------
# ROUTE: Submit Feedback
# ----------------------------
@app.route("/submit_feedback", methods=["GET", "POST"])
def submit_feedback():
    email = request.args.get("email") 
    if "email" not in session or session["email"] != email:
        flash("Student not logged in. Please login.", "danger")
        logger.write_log("Unauthorized access attempt to submit feedback.", level="warning")
        return redirect(url_for("login"))
    studentfeedback = Feedback()
    student_id = studentfeedback.GetStudentID(email)
    if not student_id:
        flash("Student not found. Please login again.", "danger")
        logger.write_log(f"Student ID not found for email={email}", level="error")
        return redirect(url_for("login"))
    courses = studentfeedback.GetCourses()  # Fetch all courses for dropdown
    print(courses)

    if request.method == "POST":
        #student_id = int(request.form["student_id"])
        course_id = int(request.form["course_id"])
        rating = int(request.form["rating"])
        comments = request.form["comments"]

        try:
            # Duplicate check
            existing = studentfeedback.CheckDuplicateFeedback(student_id, course_id)
            if existing:
                flash("Feedback already submitted for this course.", "danger")
                logger
                raise DuplicateFeedbackError("Feedback already submitted for this course.")

            # Insert feedback
            studentfeedback.saveFeedback(student_id, course_id, rating, comments)

            logger.write_log(f"Feedback submitted: student={student_id}, course={course_id}", level="info")
            flash("Feedback submitted successfully!", "success")
            return redirect(url_for("login"))

        except DuplicateFeedbackError as e:
            logger.write_log(f"Duplicate feedback attempt: student={student_id}, course={course_id}", level="warning")
            flash(str(e), "danger")
        except Exception as e:
            logger.write_log(f"Feedback submission failed: {str(e)}", level="error")
            flash("An error occurred while submitting feedback.", "danger")

    return render_template("feedback_form.html", courses=courses)


# Admin login
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = Admin()

        if admin and admin.Login(username, password):
            session["is_admin"] = True
            logger.write_log(f"Admin logged in: {username}", level="info")
            return redirect(url_for("view_feedback"))
        else:
            logger.write_log(f"Failed admin login attempt: {username}", level="warning")
            flash("Invalid username or password", "danger")

    return render_template("admin_login.html")

# ----------------------------
# REGISTER ROUTE
# ----------------------------
@app.route("/admin/register", methods=["GET", "POST"])
def admin_register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        admin = Admin()

        try:
            admin.Registration(name, password)
            logger.write_log(f"Admin Registration successful for name ={name}", level="info")
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("admin_login"))

        except Exception as e:
            logger.write_log(f"Duplicate registration attempt for name={name}", level="warning")
            flash("Name already registered!", "danger")

    return render_template("admin_register.html")


# Admin view feedback
@app.route("/admin/view_feedback")
def view_feedback():
    logger.write_log("Admin accessed view_feedback route.", level="info")
    if not session.get("is_admin"):
        logger.write_log("Unauthorized access attempt to view feedback.", level="warning")  
        flash("Unauthorized! Please login as admin.", "danger")
        return redirect(url_for("admin_login"))

    feedbacks = Feedback().GetAllFeedback()
    print (feedbacks)
    logger.write_log(f"Fetched {len(feedbacks)} feedback entries.", level="info")

    return render_template("view_feedback.html", feedbacks=feedbacks)

# Admin download log
@app.route("/admin/download_log")
def download_log():
    logger.write_log("Admin accessed download_log route.", level="info")
    if not session.get("is_admin"):
        logger.write_log("Unauthorized access attempt to download log.", level="warning")
        flash("Unauthorized! Please login as admin.", "danger")
        return redirect(url_for("admin_login"))

    if Path.exists(LOG_FILE):
        
        logger.write_log(f"Log file path: {LOG_FILE}", level="info")
        logger.write_log("Log file downloading by admin.", level="info")
        return send_file(LOG_FILE, as_attachment=True)
    else:
        flash("Log file not found!", "danger")
        logger.write_log("Log file not found!", level="error")
        return redirect(url_for("view_feedback"))




if __name__ == '__main__':
    app.run(debug=True)