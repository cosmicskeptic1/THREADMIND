from scoring import total_score


class OutfitEngine:

    def __init__(
        self,
        wardrobe,
        occasion="College",
        season="Summer"
    ):

        self.wardrobe = wardrobe
        self.occasion = occasion
        self.season = season

    def set_preferences(
        self,
        occasion,
        season
    ):

        self.occasion = occasion
        self.season = season

    def generate_outfits(self):

        outfits = []

        tops = self.wardrobe.get_tops()
        bottoms = self.wardrobe.get_bottoms()
        shoes = self.wardrobe.get_shoes()

        for top in tops:

            for bottom in bottoms:

                for shoe in shoes:

                    score = total_score(
                        top,
                        bottom,
                        shoe,
                        self.occasion,
                        self.season
                    )

                    outfit = {
                        "top": top,
                        "bottom": bottom,
                        "shoes": shoe,
                        "score": score
                    }

                    outfits.append(outfit)

        outfits.sort(
            key=lambda outfit: outfit["score"],
            reverse=True
        )

        return outfits

    def get_best_outfits(self, number=5):

        outfits = self.generate_outfits()

        return outfits[:number]