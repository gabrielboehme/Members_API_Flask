from flask import Flask, g, request, jsonify
from database_config import get_db
from functools import wraps


app = Flask(__name__)

#Database config
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

#Authentication
api_user = 'rootadmin'
api_pass = 'goodpass'


def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        auth = request.authorization

        if auth and auth.username == api_user and auth.password == api_pass:

            return f(*args, **kwargs)

        else:
           
            return jsonify({'message' : 'Authentication failed!'}), 403

    return decorated

#Routes

#Return all members
@app.route('/member',methods=['GET'])
@protected
def get_members():

    #Getting members from db
    db = get_db()
    members_cur = db.execute('select id, name, email, level from members')
    members = members_cur.fetchall()

    #Transforming values to json
    values = []

    for member in members: #looping in the db and for each member creates a dict with values
        member_dict = {}
        member_dict['id'] = member['id']
        member_dict['name'] = member['name']
        member_dict['email'] = member['email']
        member_dict['level'] = member['level']

        values.append(member_dict)

    members_json = jsonify({"members" : values}) #return json with all members

    return members_json

#Return specific member - arg = id
@app.route('/member/<int:member_id>',methods=['GET'])
def get_member(member_id):

    #Get member in the db
    db = get_db()
    member_cur = db.execute('select id, name, email, level from members where id = ?',[member_id])
    member = member_cur.fetchone()

    if member:
        #Transform to json formact
        member_json_string = {
            'id' : member['id'],
            'name' : member['name'],
            'email' : member['email'],
            'level' : member['level']
            }
        member_json = jsonify(member_json_string)
        
        return member_json
    
    else:
        return jsonify({'message' : 'Member does not Exist'})

#Inserts a new member to db - args = id, name, email, level (json)
@app.route('/member',methods=['POST'])
def add_member():

    #Get member info from request
    new_member = request.get_json()
    name = new_member['name']
    email = new_member['email']
    level = new_member['level']

    #Insert member info into db
    db = get_db()
    db.execute('insert into members (name, email, level) values (?, ?, ?)', [name, email, level])
    db.commit()

    #Return user data to confirm
    member_cur = db.execute('select id, name, email, level from members where name = ?',[name])
    new_member_json = member_cur.fetchone()

    db_id = new_member_json['id']
    db_name = new_member_json['name']
    db_email = new_member_json['email']
    db_level = new_member_json['level']

    member_json_string = {'member': {'id':db_id,'name':db_name,'email':db_email,'level':db_level}}
    member_json = jsonify(member_json_string)

    return member_json

#Updates a member informations
@app.route('/member/<int:member_id>',methods=['PUT','PATCH'])
def edit_member(member_id):

    #Getting member information
    member_data = request.get_json()
    name = member_data['name']
    email = member_data['email']
    level = member_data['level']

    #Updating member data in db
    db = get_db()
    db.execute('update members set name = ?, email = ?, level = ? where id = ?',[name, email, level, member_id])
    db.commit()

    #Get info from db
    member_cur = db.execute('select id, name, email, level from members where id = ?',[member_id])
    member_db_data = member_cur.fetchone()

    #Jsonify
    member_json_string = {'member': {'id' : member_db_data['id'], 'name' : member_db_data['name'], 'email' : member_db_data['email'], 'level' : member_db_data['level']}}
    member_json = jsonify(member_json_string)
    
    return member_json

@app.route('/member/<int:member_id>',methods=['DELETE'])
def del_member(member_id):

    #Delete from db
    db = get_db()
    db.execute('delete from members where id = ?',[member_id])
    db.commit() 

    #Return message

    message = {'message': 'Member has been deleted.'}

    return message

if __name__ == '__main__':
    app.run(debug=True)