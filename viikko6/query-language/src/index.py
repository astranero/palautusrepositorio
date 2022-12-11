from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


class QueryBuilder:

    def __init__(self, all=All()):
        self._matchers = all

    def playsIn(self, team):
        return QueryBuilder(And(self._matchers, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matchers, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matchers, HasFewerThan(value, attr)))

    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2))

    def build(self):
        return self._matchers


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (query
               .playsIn("NYR")
               .hasAtLeast(
                   10, "goals")
               .hasFewerThan(20, "goals")
               .build())

    m1 = (
        query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
        query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
