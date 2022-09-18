from app import manager
from app import app, Flask

app = Flask(__name__)

if __name__ == '__main__':
    manager.run()

