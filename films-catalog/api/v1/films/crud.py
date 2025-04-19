from pydantic import BaseModel, Field
from schemas.film import (
    FilmSchema,
    FilmSchemaCreate,
    FilmSchemaPartialUpdate,
    FilmSchemaUpdate,
)


class FilmStorage(BaseModel):
    slug_to_film: dict[str, FilmSchema] = Field(default_factory=dict)

    def get(self) -> list[FilmSchema]:
        return list(self.slug_to_film.values())

    def get_by_slug(self, slug: str) -> FilmSchema | None:
        return self.slug_to_film.get(slug)

    def create(self, film_schema_create: FilmSchemaCreate):
        film = FilmSchema(**film_schema_create.model_dump())
        self.slug_to_film[film.slug] = film
        return film

    def delete_by_slug(self, slug: str) -> FilmSchema | None:
        self.slug_to_film.pop(slug, None)

    def delete(self, film_schema: FilmSchema):
        self.delete_by_slug(slug=film_schema.slug)

    def update(
        self,
        film_schema: FilmSchema,
        film_schema_in: FilmSchemaUpdate,
    ) -> FilmSchema:
        # updated_film = film_schema.model_copy(
        #     update=film_schema_in.model_dump(),
        # )
        # self.slug_to_film[updated_film.slug] = updated_film
        for field_name, value in film_schema_in:
            setattr(film_schema, field_name, value)
        # self.slug_to_film[film_schema.slug] = short_url
        return film_schema

    def partial_update(
        self,
        film_schema: FilmSchema,
        film_schema_in: FilmSchemaPartialUpdate,
    ) -> FilmSchema:
        for field_name, value in film_schema_in.model_dump(exclude_unset=True).items():
            setattr(film_schema, field_name, value)

        return film_schema


film_storage = FilmStorage()

film_storage.create(
    FilmSchemaCreate(
        slug="Django",
        title="Django_Unchaned",
        description="In 1858 Texas, several male African American slaves are being 'driven' by the Speck Brothers,"
        "Ace and Dicky.",
        budget=100_000_000,
        box_office=426_000_000,
    ),
)

film_storage.create(
    FilmSchemaCreate(
        slug="Aliens",
        title="Aliens",
        description="Ellen Ripley has been in stasis for 57 years aboard a shuttlecraft after destroying her spaceship,"
        "the Nostromo, to escape an alien creature that slaughtered her crew",
        budget=18_500_000,
        box_office=183_300_000,
    ),
)
