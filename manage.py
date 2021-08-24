from app import create_app
from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.shell

def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
    manager.run()