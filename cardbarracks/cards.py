import itertools

class UnknownCardFormat:
    pass


class Card:
    HEIGHT = 81
    WIDTH = 56
    BGCOLOR = (.8, .8, .8)

    def __init__(self, grunt):
        self.grunt = grunt
        return super().__init__()


class Use_me_Card(Card):
    def render(self, renderer):
        renderer.string(5, 5, 5.5, 36, self.grunt.name)
        renderer.string(43, 5, 5.5, 8, str(self.grunt.points), label="Pts")

        renderer.string(5, 12, 4, 22.5, self.grunt.force)
        renderer.string(28.5, 12, 4, 22.5, self.grunt.desc)

        renderer.image(5, 18, 22.5, 22.5, self.grunt.image)

        renderer.string(28.5, 18, 5.5, 10.5, str(self.grunt.elan), label="Elan")
        renderer.string(40.5, 18, 5.5, 10.5, str(self.grunt.movement), label="Move")

        # renderer.string(26, 20, 10, 4, "Type: " + self.grunt.type)

        renderer.box(5, 45, 4, 14.666, "Wing.", 1)
        renderer.box(20.833, 45, 4, 14.666, "Struck", 1)
        renderer.box(36.166, 45, 4, 14.666, "Killed", 1)
        for n, w in enumerate(self.grunt.weapons):
            renderer.string(28.5, 24.5+n*5, 4, 22, "{} {}".format(*w))

        # renderer.string(5, 44, 10, 4, "Notes")
        renderer.text(5, 50, self.WIDTH - 10, self.HEIGHT - 55, 4, self.grunt.notes, label="Notes")


def get_class(cardformat):
    if cardformat == "use_me":
        return Use_me_Card
    else:
        raise UnknownCardFormat()
