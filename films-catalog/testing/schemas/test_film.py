from unittest import TestCase

from schemas.film import FilmSchema, FilmSchemaCreate


class ShortUrlCreateTestCase(TestCase):
    def test_film_can_be_created_from_create_schema(self) -> None:
        short_url_in = FilmSchemaCreate(
            title="some-slug",
            description="some-description",
            budget=900,
            box_office=950,
            slug="slug",
        )

        short_url = FilmSchema(
            **short_url_in.model_dump(),
        )
        self.assertEqual(
            short_url_in.slug,
            short_url.slug,
        )
        self.assertEqual(
            short_url_in.title,
            short_url.title,
        )
        self.assertEqual(
            short_url_in.description,
            short_url.description,
        )
