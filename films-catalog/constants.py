from schemas.film import FilmSchema

FILMS = [
    FilmSchema(
        id=1,
        title="Django_Unchaned",
        description="In 1858 Texas, several male African American slaves are being 'driven' by the Speck Brothers,"
        "Ace and Dicky.",
        budget=100_000_000,
        box_office=426_000_000,
    ),
    FilmSchema(
        id=2,
        title="Aliens",
        description="Ellen Ripley has been in stasis for 57 years aboard a shuttlecraft after destroying her spaceship,"
        "the Nostromo, to escape an alien creature that slaughtered her crew",
        budget=18_500_000,
        box_office=183_300_000,
    ),
]
