from flask import Flask,redirect,url_for,json,jsonify
from flask_dance.contrib.github import make_github_blueprint,github

app=Flask(__name__)

github_blueprint= make_github_blueprint(client_id='ID',client_secret='Key')
app.register_blueprint(github_blueprint,url_prefix='/github_login')
@app.route('/github')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    account_info=github.get('/user')

    if account_info.ok:
        account_info_json=account_info.json()
        return '<h1>Your Github Name {}'.format(account_info_json['login'])
    return '<h1>Request</h1>'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)