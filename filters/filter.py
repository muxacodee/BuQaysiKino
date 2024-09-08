def is_valid_id(movie_id):
    try:
        int(movie_id)
        return True
    except ValueError:
        return False

