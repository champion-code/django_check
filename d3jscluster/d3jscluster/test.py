
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print os.path.join(BASE_DIR, 'static')
print os.path.join(os.path.dirname(__file__), '../static/').replace('\\','/')
