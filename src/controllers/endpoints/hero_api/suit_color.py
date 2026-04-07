from flask import request
from flask_api import status

from src.database.database import session
from src.controllers.utils.base_api import BaseApi
from src.services.hero_service import HeroService

class ChangeSuitColorApi(BaseApi):
    def put(self, hero_id: int):
        data = request.get_json()
        HeroService(session).update_hero_suit_color(hero_id, data.get('suitColor'))
        session.commit()
        return {'message': 'Updated successfully'}, status.HTTP_200_OK