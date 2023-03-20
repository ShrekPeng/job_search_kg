# 指定socket文件的位置和权限
bind = "unix:/home/username/myproject/myproject.sock"
umask = 0o007

# 指定wsgi模块和应用实例名
wsgi_app = "wsgi:app"

# 指定工作进程数
workers = 2

# 指定日志文件路径
accesslog = "/home/ec2-user/es_flask_demo/flask_elasticsearch_query/access.log"
errorlog = "/home/ec2-user/es_flask_demo/flask_elasticsearch_query/error.log"