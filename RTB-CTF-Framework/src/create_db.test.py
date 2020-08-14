from FlaskRTBCTF import db, create_app
from FlaskRTBCTF.main.models import Settings


app = create_app()


with app.app_context():
    db.create_all()

    db.session.add(Settings(dummy=False))

    db.session.commit()
