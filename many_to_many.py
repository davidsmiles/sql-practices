from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///many.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


association = db.Table('association',
                db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                db.Column('channel_id', db.Integer, db.ForeignKey('channels.channel_id')))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    subscriptions = db.relationship('Channel', secondary=association, backref=db.backref('subscribers', lazy='dynamic'))


class Channel(db.Model):
    __tablename__ = 'channels'
    channel_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


db.create_all()

# users = [User(name='David'), User(name='Emma'), User(name='Peter'), User(name='Oke')]
# for user in users:
#     db.session.add(user)
#     db.session.commit()
#
# channels = [Channel(name='NairaMarley'), Channel(name='REST Api'), Channel(name='Zlatan'), Channel(name='Netflix')]
# for channel in channels:
#     db.session.add(channel)
#     db.session.commit()
#
# channels[0].subscribers.append(users[0])
# channels[0].subscribers.append(users[1])
# channels[0].subscribers.append(users[3])
#
# db.session.commit()
#
# users[1].subscriptions.append(channels[0])
# users[1].subscriptions.append(channels[1])
# users[1].subscriptions.append(channels[2])
#
#
# db.session.commit()
#
# for user in channels[0].subscribers:
#     print(f'{user.name} is subscribed to {channels[0].name}')
#
# for channel in users[1].subscriptions:
#     print(f'{channel.name} is watched by {users[1].name}')