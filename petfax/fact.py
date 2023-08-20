from flask import ( Blueprint, render_template, request, redirect ) 

bp = Blueprint('fact', __name__, url_prefix="/facts")

# Takes user to the form page to submit a fact
@bp.route('/new')
def new(): 
    return render_template('/facts/new.html')

# Takes the Users submitted fact, and redirects them to the fact index page
@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')

    return render_template('/facts/index.html')