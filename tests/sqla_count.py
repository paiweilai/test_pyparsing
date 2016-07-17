something1
x = session.query(x).filter(y).count()
something2
y = session.query(
    models.User,
).filter(
    models.User.time > start_time,
    models.User.id == user_id,
).count()
something3
    x = session.query(
        models.Review,
    ).filter(
        models.Review.time < end_time,
    ).count()
something4
