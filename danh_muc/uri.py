from flask import Blueprint

from Controller.test_controller import ApiController
# from celery_construct import create_task

NewsId = Blueprint('NewsId', __name__)


@NewsId.route('/test_celery', methods=['GET'])
def get_x():
    return ApiController.handle_task()

