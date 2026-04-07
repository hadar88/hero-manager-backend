from flask_api import status
from flasgger import swag_from

from src.database.database import session
from src.controllers.utils.base_api import BaseApi
from src.services.hero_service import HeroService
from src.socketio import socketio_app


class RetireHeroApi(BaseApi):
    @swag_from('../../swagger/hero/retire/put.yaml')
    def put(self, hero_id: int) -> tuple[dict[str, str], int]:
        hero_service = HeroService(session)

        hero_service.retire_hero(hero_id)
        socketio_app.emit('retire', {'id': hero_id})

        return {"message": "Hero retired successfully!"}, status.HTTP_200_OK
