from password import password

class Config(object):
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://postgres:{password}@localhost:5432/post_vk"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'jfkjuriwpcm39cfj!odmfnvnklie!349amdmwom'
