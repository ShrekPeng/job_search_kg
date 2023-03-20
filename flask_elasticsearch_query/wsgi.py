# 导入flask app实例
from flask_elasticsearch_query import app

# 运行flask app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
