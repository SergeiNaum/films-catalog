from unittest import TestCase

from schemas.film import FilmSchema, FilmSchemaCreate, FilmSchemaUpdate


class ShortUrlCreateTestCase(TestCase):
    def test_film_can_be_created_from_create_schema(self) -> None:
        film_schema_in = FilmSchemaCreate(
            title="some-slug",
            description="some-description",
            budget=900,
            box_office=950,
            slug="slug",
        )

        film_schema = FilmSchema(
            **film_schema_in.model_dump(),
        )
        self.assertEqual(
            film_schema_in.slug,
            film_schema.slug,
        )
        self.assertEqual(
            film_schema_in.title,
            film_schema.title,
        )
        self.assertEqual(
            film_schema_in.description,
            film_schema.description,
        )

    def test_film_can_be_updated_from_update_schema(self) -> None:
        film_schema = FilmSchema(
            title="some-slug",
            description="some-description",
            budget=900,
            box_office=950,
            slug="slug",
        )
        film_schema_in = FilmSchemaUpdate(
            title="slug-update",
            description="description-update",
            budget=1,
            box_office=2,
        )
        for field_name, value in film_schema_in:
            setattr(film_schema, field_name, value)

        self.assertEqual(
            film_schema_in.title,
            film_schema.title,
        )
        self.assertEqual(
            film_schema_in.description,
            film_schema.description,
        )
