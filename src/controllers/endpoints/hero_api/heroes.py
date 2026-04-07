from flask import request
from flask_api import status
from flasgger import swag_from

from src.controllers.endpoints.hero_api.output_schemas import GetHeroOutputSchema
from src.controllers.models.hero_filters import HeroFilters
from src.controllers.models.new_hero import NewHero
from src.controllers.utils.base_api import BaseApi
from src.database.database import session
from src.services.hero_service import HeroService


class HeroesApi(BaseApi):
    @swag_from('../../swagger/hero/heroes/get.yaml')
    def get(self) -> tuple[list[GetHeroOutputSchema], int]:
        heroes = HeroService(session).get_heroes_by_filters(HeroFilters(**request.args))
        return [GetHeroOutputSchema(
            id=hero.id,
            name=hero.name,
            suit_color=hero.suit_color,
            has_cape=hero.has_cape,
            last_mission=hero.last_mission,
            is_retired=hero.is_retired,
        ).model_dump() for hero in heroes], status.HTTP_200_OK

    @swag_from('../../swagger/hero/heroes/post.yaml')
    def post(self) -> tuple[dict[str, str], int]:
        hero = HeroService(session).create_hero(NewHero(**request.get_json()))
        session.commit()
        return {'message': 'Created hero successfully', 'id': hero.id}, status.HTTP_201_CREATED
