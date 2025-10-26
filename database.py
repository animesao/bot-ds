import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base
import json
import os

Base = declarative_base()

class ServerSettings(Base):
    __tablename__ = 'server_settings'
    id = sa.Column(sa.Integer, primary_key=True)
    guild_id = sa.Column(sa.BigInteger, unique=True, nullable=False)
    welcome_channel_id = sa.Column(sa.BigInteger, nullable=True)
    welcome_message = sa.Column(sa.Text, default="Welcome {user} to {server}!")
    banned_words = sa.Column(sa.Text, default=json.dumps(["badword1", "badword2"]))
    spam_threshold = sa.Column(sa.Integer, default=5)
    auto_mute_warnings = sa.Column(sa.Integer, default=3)

class User(Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.BigInteger, unique=True, nullable=False)
    guild_id = sa.Column(sa.BigInteger, nullable=False)
    xp = sa.Column(sa.Integer, default=0)
    level = sa.Column(sa.Integer, default=0)
    warnings = sa.Column(sa.Integer, default=0)
    muted_until = sa.Column(sa.DateTime, nullable=True)

class Database:
    def __init__(self, db_path='bot.db'):
        self.engine = sa.create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def get_or_create_server_settings(self, guild_id):
        session = self.get_session()
        settings = session.query(ServerSettings).filter_by(guild_id=guild_id).first()
        if not settings:
            settings = ServerSettings(guild_id=guild_id)
            session.add(settings)
            session.commit()
        session.close()
        return settings

    def get_or_create_user(self, user_id, guild_id):
        session = self.get_session()
        user = session.query(User).filter_by(user_id=user_id, guild_id=guild_id).first()
        if not user:
            user = User(user_id=user_id, guild_id=guild_id)
            session.add(user)
            session.commit()
        session.close()
        return user

    def update_user_xp(self, user_id, guild_id, xp_gain):
        session = self.get_session()
        user = session.query(User).filter_by(user_id=user_id, guild_id=guild_id).first()
        if user:
            user.xp += xp_gain
            user.level = user.xp // 100  # Simple level formula
            session.commit()
        session.close()

    def add_warning(self, user_id, guild_id):
        session = self.get_session()
        user = session.query(User).filter_by(user_id=user_id, guild_id=guild_id).first()
        if user:
            user.warnings += 1
            session.commit()
        session.close()

    def get_top_users(self, guild_id, limit=10):
        session = self.get_session()
        users = session.query(User).filter_by(guild_id=guild_id).order_by(User.xp.desc()).limit(limit).all()
        session.close()
        return users
