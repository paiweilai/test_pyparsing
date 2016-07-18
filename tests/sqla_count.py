something1
x = session.query(x).filter(y).count()
something2
y = session.query(
    models.User, models.X,
).filter(
    models.User.time > start_time,
    models.User.id == user_id,
).count()
def something3():
    x = session.query(
        models.Review,
    ).filter(
        models.Review.time < end_time,
    ).count()
something4
x = session.query(x, y).filter(bla).count()
x = session.query(x.X, y).filter(y > user_id).count()
x = session.query(
    x.X, y.Y
).filter(x.X == 5).count()
something5
