from flask_api import status
from flasgger import swag_from

from src.controllers.utils.base_api import BaseApi


class IndexApi(BaseApi):
    @swag_from('../swagger/index/get.yaml')
    def get(self) -> tuple[str, int]:
        return "Running Hero Manager Backend", status.HTTP_200_OK
