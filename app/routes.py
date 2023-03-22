from app import app

@app.route('/home')
def homePage():
    return{
        'Hello there' : 'Annoyed'
    }

@app.route('/')
def landingPage():
    return{
        'you have' : 'LANDED'
    }
