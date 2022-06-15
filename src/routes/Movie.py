from flask import Blueprint, jsonify, request
import uuid
import datetime

# Entities

from models.entities.Movie import Movie


# Models

from models.MovieModel import MovieModel

main=Blueprint('movie_blueprint',__name__)

@main.route('/')
def get_movies():
    try:
        movies=MovieModel.get_movies()
        return jsonify(movies)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/<id>')
def get_movie(id):
    try:
        movie=MovieModel.get_movie(id)
        if movie != None:
            return jsonify(movie)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500

@main.route('/add', methods=['POST'])
def add_movie():
    try:
        title = request.json['title']

        if title == "" or len(title) > 50:
            return jsonify({'message':"check the input data, title needs 1 character as minimum and 50 character as maximum..."}), 404

        duration = int(request.json['duration'])

        if len(str(duration)) <= 0 or len(str(duration)) > 4:
            return jsonify({'message':"check the input data, duration needs 1 minute minimum and 999 minutes maximum..."}), 404

        released = request.json['released']

        # Valido Fecha, si da error va directo a except
        datetime.datetime.strptime(released, '%Y-%m-%d')
        
        movie=Movie(str(id),title,duration,released)

        affected_rows = MovieModel.add_movie(movie)
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':"Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message':str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie=Movie(id)

        affected_rows = MovieModel.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':"No movie deleted"}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:

        title = request.json['title']

        if title == "" or len(title) > 50:
            return jsonify({'message':"check the input data, title needs 1 character as minimum and 50 character as maximum..."}), 404

        duration = int(request.json['duration'])

        if len(str(duration)) <= 0 or len(str(duration)) > 4:
            return jsonify({'message':"check the input data, duration needs 1 minute minimum and 999 minutes maximum..."}), 404

        released = request.json['released']

        # Valido Fecha, si da error va directo a except
        datetime.datetime.strptime(released, '%Y-%m-%d')


        movie=Movie(id,title,duration,released)

        affected_rows = MovieModel.update_movie(movie)
        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message':"No movie updated"}), 404
    except Exception as ex:
        return jsonify({'message':str(ex)}), 500