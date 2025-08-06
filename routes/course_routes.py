# routes/course_routes.py

from flask import Blueprint, request, jsonify
from models import db, CourseTemplate
from sqlalchemy.exc import SQLAlchemyError

course_bp = Blueprint('course', __name__, url_prefix='/courses')


@course_bp.route('/', methods=['GET'])
def get_all_courses():
    courses = CourseTemplate.query.all()
    result = [
        {
            'id': course.id,
            'name': course.name,
            'par_values': course.par_values,
            'created_by': course.created_by
        }
        for course in courses
    ]
    return jsonify(result), 200


@course_bp.route('/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    course = CourseTemplate.query.get(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    result = {
        'id': course.id,
        'name': course.name,
        'par_values': course.par_values,
        'created_by': course.created_by
    }
    return jsonify(result), 200


@course_bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    name = data.get('name')
    par_values = data.get('par_values')
    created_by = data.get('created_by')

    if not name or not par_values:
        return jsonify({'error': 'Course name and par values are required'}), 400

    new_course = CourseTemplate(name=name, par_values=par_values, created_by=created_by)
    try:
        db.session.add(new_course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully', 'id': new_course.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500


@course_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = CourseTemplate.query.get(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    data = request.get_json()
    course.name = data.get('name', course.name)
    course.par_values = data.get('par_values', course.par_values)
    course.created_by = data.get('created_by', course.created_by)

    try:
        db.session.commit()
        return jsonify({'message': 'Course updated successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500


@course_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = CourseTemplate.query.get(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    try:
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500
